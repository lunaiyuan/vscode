#-*- codeing = utf-8 -*-
#@Time : 2020/7/3 23:34
#@Author : 鲁乃源
#@File : main.py
#@Software : PyCharm
import requests
import re
from lxml import etree
import time
import os
import json
import aiohttp
import asyncio

session = requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
def get_champion_list():
    url = 'https://www.op.gg/champion/statistics'
    session.get(url='https://www.op.gg/l=zh_CN',headers=headers)
    page_text = session.get(url=url,headers=headers).text
    tree =etree.HTML(page_text)
    div_list = tree.xpath('//div[@class="champion-index__champion-list"]/div')
    return div_list
def get_url_name(div_list):
    champins = {}
    for div in div_list:

        try:
            name = div.xpath('./a/div[@class="champion-index__champion-item__name"]/text()')[0]
            web = div.xpath('./a/@href')[0]
            weizhi = div.xpath('./a//span/text()')
        except:
            name = div.xpath('./div[@class="champion-index__champion-item__name"]/text()')[0]
            web = 'rip'
            weizhi = 'rip'
        finally:
            champins[name] = [web,weizhi]
    return champins
def get_web(champins):
    summons = ['Teleport', 'Flash', 'Dot', 'Exhaust', 'Boost', 'Heal', 'Smite', 'Haste', 'Barrier']
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'close',
    'Host': 'www.op.gg',
    'Referer': 'https://www.op.gg/champion/statistics',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    weizhi_trans = {'上单':'top','打野':'jungle','中单':"mid",'下路':'bot','辅助':'support'}
    shuju = {}
    shuju['中单'] = {}
    shuju['上单'] = {}
    shuju['打野'] = {}
    shuju['下路'] = {}
    shuju['辅助'] = {}

    #遍历所有英雄
    cs = 0
    all_cs = len(champins.keys())
    print('正在初始化设置')
    for name,lists in champins.items():
        cs += 1
        weizhi = lists[1]
        if lists[0] != 'rip':
            #获得英雄详情页面
            for w in weizhi:
                if w in weizhi_trans.keys():
                    url = 'https://www.op.gg'+lists[0]+'/'+weizhi_trans[w]
                elif w in weizhi_trans.values:
                    url = 'https://www.op.gg'+lists[0]+'/'+w
                #获得页面编码数据
                page_text = session.get(url=url,headers=headers).text
                tree = etree.HTML(page_text)
                def get_sums_win_pick():
                    s1 = []
                    s2 = []
                    sums = tree.xpath(
                        '//table[@class="champion-overview__table champion-overview__table--summonerspell"]/tbody[1]/tr')
                    sum1 = sums[0]
                    sum2 = sums[1]
                    sum1_1 = sum1.xpath('.//li[1]/img/@src')[0]
                    sum1_2 = sum1.xpath('.//li[3]/img/@src')[0]
                    pic1 = \
                    sum1.xpath('.//td[@class="champion-overview__stats champion-overview__stats--pick"]/strong/text()')[
                        0]
                    win1 = \
                    sum1.xpath('.//td[@class="champion-overview__stats champion-overview__stats--win"]/strong/text()')[
                        0]
                    sum1s = [sum1_1, sum1_2]
                    sum2_1 = sum2.xpath('.//li[1]/img/@src')[0]
                    sum2_2 = sum2.xpath('.//li[3]/img/@src')[0]
                    pic2 = \
                    sum2.xpath('.//td[@class="champion-overview__stats champion-overview__stats--pick"]/strong/text()')[
                        0]
                    win2 = \
                    sum2.xpath('.//td[@class="champion-overview__stats champion-overview__stats--win"]/strong/text()')[
                        0]

                    sum2s = [sum2_1, sum2_2]

                    for summon in summons:
                        for s in sum1s:
                            if summon in s:
                                s1.append(summon)
                            else:
                                pass
                    for summon in summons:
                        for s in sum2s:
                            if summon in s:
                                s2.append(summon)
                            else:
                                pass
                    str1 = s1, '选取率为:' + pic1, '胜率为:' + win1
                    str2 = s2, '选取率为:' + pic2, '胜率为:' + win2
                    s = {'召唤师技能': [[s1, [pic1, win1]], [s2, [pic2, win2]]]}
                    return s

                def get_skills():
                    skills = tree.xpath('//table[@class="champion-skill-build__table"]//tr[2]/td')
                    skill1 = []
                    count = 0
                    #解析出技能的顺序
                    for skill in skills:
                        s = skill.xpath('./text()')[0]
                        s = "".join(s.split())
                        count += 1
                        #第一个技能加满时
                        if count == 9:
                            cq = skill1.count('Q')
                            cw = skill1.count('W')
                            ce = skill1.count('E')

                            count_all = {cq: "Q", cw: "W", ce: "E"}
                            cts = list(count_all.keys())
                            ss = max(cts)
                            s = count_all[ss]

                        #第二个技能加满时
                        if count == 13:
                            cq = skill1.count('Q')
                            cw = skill1.count('W')
                            ce = skill1.count('E')

                            count_all = {cq: "Q", cw: "W", ce: "E"}
                            cts = list(count_all.keys())
                            ss = max(cts)
                            cts.remove(ss)
                            ss = max(cts)
                            s = count_all[ss]

                        skill1.append(s)
                    #解析出技能胜率
                    pics = tree.xpath('//td[@class="champion-overview__stats champion-overview__stats--pick"]/strong/text()')[2]
                    wins = tree.xpath('//td[@class="champion-overview__stats champion-overview__stats--win"]/strong/text()')[2]
                    return [skill1,[pics,wins]]
                def get_build(url):
                    headers = {'Accept': '*/*',
                               'Accept-Encoding': 'gzip, deflate,br',
                               'Accept-Language': 'zh-CN,zh;q=0.9',
                               'Connection': 'close',
                               'Host': 'www.op.gg',
                               'Referer': 'https://www.op.gg/champion/neeko/statistics/mid',
                               'Sec-Fetch-Mode': 'cors',
                               'Sec-Fetch-Site': 'same-origin',
                               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
                               'X-NewRelic-ID': 'VQcEVlFSDBAHXFdRAwAAXg==',
                               'X-Requested-With': 'XMLHttpRequest'}
                    url = url + '/item?'
                    page_text = requests.get(url, headers=headers).text
                    tree = etree.HTML(page_text)
                    buildsd = {}
                    # 核心出装：
                    buildsd = {}
                    mainblist = []
                    mainpwlist = []
                    mbuilds = tree.xpath('/html/body/div/div[1]/div[1]/div/table/tbody/tr')
                    for tr in mbuilds:
                        builds = tr.xpath('./td/ul/li[@class="champion-stats__list__item tip"]/@title')
                        slist = []
                        for title in builds:
                            ex = "<b style='color: #00cfbc'>(.*?)</b><br><span>"
                            item = re.findall(ex, title)[0]
                            slist.append(item)
                        mainblist.append(slist)
                        pick = tr.xpath('./td[2]/text()')[0]
                        pick = "".join(pick.split())
                        win = tr.xpath('./td[3]/text()')[0]
                        mainpwlist.append([pick, win])
                    biglist = []
                    for c in range(len(mainblist)):
                        biglist.append([mainblist[c], mainpwlist[c]])
                    buildsd['核心出装'] = [biglist]

                    # 鞋子：
                    xieblist = []
                    xiepwlist = []
                    biglist = []
                    xiebuilds = tree.xpath('/html/body/div/div[1]/div[2]/div/table/tbody/tr')
                    for tr in xiebuilds:
                        build = tr.xpath('.//div[@class="champion-stats__single__item"]//span/text()')[0]
                        xieblist.append(build)
                        pick = tr.xpath('.//td[2]/text()')[0]
                        pick = "".join(pick.split())
                        win = tr.xpath('.//td[3]/text()')[0]
                        biglist.append([build, [pick, win]])
                    buildsd['鞋子'] = biglist
                    ###############################################################################
                    # 出门装
                    firstlist = []
                    firstpwlist = []
                    biglist = []
                    firstbulids = tree.xpath('/html/body/div/div[1]/div[3]/div/table/tbody/tr')
                    for tr in firstbulids:
                        builds = tr.xpath('./td/ul/li[@class="champion-stats__list__item tip"]/@title')
                        slist = []
                        for title in builds:
                            ex = "<b style='color: #00cfbc'>(.*?)</b><br><span>"
                            item = re.findall(ex, title)[0]
                            slist.append(item)
                        firstlist.append(slist)
                        pick = tr.xpath('./td[2]/text()')[0]
                        pick = "".join(pick.split())
                        win = tr.xpath('./td[3]/text()')[0]
                        firstpwlist.append([pick, win])
                    biglist = []
                    for c in range(len(firstpwlist)):
                        biglist.append([firstlist[c], firstpwlist[c]])
                    buildsd['出门装'] = [biglist]
                    return buildsd
                def get_counter(url):
                    url = url + '/matchup?'
                    headers = {'Accept': '*/*',
                               'Accept-Encoding': 'gzip, deflate,br',
                               'Accept-Language': 'zh-CN,zh;q=0.9',
                               'Connection': 'close',
                               'Host': 'www.op.gg',
                               'Referer': 'https://www.op.gg/champion/neeko/statistics/mid',
                               'Sec-Fetch-Mode': 'cors',
                               'Sec-Fetch-Site': 'same-origin',
                               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
                               'X-NewRelic-ID': 'VQcEVlFSDBAHXFdRAwAAXg==',
                               'X-Requested-With': 'XMLHttpRequest'}
                    page_text = requests.get(url, headers=headers).text
                    tree = etree.HTML(page_text)
                    datalist = tree.xpath('/html/body/div/div[2]/div[3]/div')
                    alldata = []
                    for data in datalist:
                        data_champion_name = data.xpath('./@data-champion-name')[0]
                        data_champion_key = data.xpath('./@data-champion-key')[0]
                        winrate = float(data.xpath('./@data-value-winrate')[0])
                        alldata.append([data_champion_name, data_champion_key, winrate])
                    return alldata
                #获得召唤师技能信息
                召唤师技能 = get_sums_win_pick() #s = {'召唤师技能':[[s1,[pic1,win1]],[s2,[pic2,win2]]]}
                #获得加点信息
                技能 = get_skills()              #{'技能':[skill1,[pics,wins]]}
                #获得出装信息
                装备 =get_build(url)          #{'核心出装': [[[['海克斯科技GLP-800', '双生暗影', '中娅沙漏'], ['24.85%', '56.95%']], 。。。
                #反制
                反制 = get_counter(url)       #alldata.append([data_champion_name, data_champion_key, winrate])


                #封装
                shuju[w][name] = [召唤师技能,技能,装备,反制]
                print(f'正在下载{name+w},{cs}/{all_cs}')
    return shuju
def wirte_data(shuju):
    print('开始写入数据')
    with open('./data.txt','w+',encoding='utf-8')as t:
        s = json.dumps(shuju,ensure_ascii=False)
        t.write(s)
    print('写入完成')
def main():

    div_list = get_champion_list()
    champins = get_url_name(div_list)
    shuju =get_web(champins)
    wirte_data(shuju)



if __name__ == '__main__':
    main()