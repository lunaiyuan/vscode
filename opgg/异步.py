#-*- codeing = utf-8 -*-
#@Time : 2020/7/3 23:34
#@Author : 鲁乃源
#@File : main.py
#@Software : PyCharm
import requests
import re
from lxml import etree
import json
import aiohttp
import asyncio
from functools import partial

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
async def get_main_web(url):
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
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    async with aiohttp.ClientSession() as sess:

        await asyncio.sleep(1)
        async with await sess.get(url,headers=headers) as response:

            page_text0 = await response.text()




        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                   'Accept-Encoding': 'gzip, deflate,br',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'Connection': 'close',
                   'Host': 'www.op.gg',
                   'Sec-Fetch-Mode': 'navigate',
                   'Sec-Fetch-Site': 'none',
                   'Sec-Fetch-User': '?1',
                   'Upgrade-Insecure-Requests': '1',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
                   }
        url1 = url + '/item?'
        url2 = url+'/matchup?'
        await asyncio.sleep(1)
    #async with aiohttp.ClientSession() as sess:
        async with await sess.get(url1,headers=headers) as response:
            page_text1 = await response.text()
    #async with aiohttp.ClientSession() as sess:
        await asyncio.sleep(1)
        async with await sess.get(url2,headers=headers) as response:
            page_text2 = await response.text()
    return page_text0,page_text1,page_text2
def jieximainweb(nw,t):
    name = nw[1]
    w = nw[2]
    try:
        page_text0 = t.result()[0]  #主页面
        #page_text1 = t.result()[1]  #出装
        page_text2 = t.result()[2]  #克制
    except :
        print(name,w)
    tree = etree.HTML(page_text0)
    summons = ['Teleport', 'Flash', 'Dot', 'Exhaust', 'Boost', 'Heal', 'Smite', 'Haste', 'Barrier']
    #解析召唤师技能

    sss = []
    def get_sums_win_pick():
        s1 = []
        s2 = []
        sums = tree.xpath('//table[@class="champion-overview__table champion-overview__table--summonerspell"]/tbody[1]/tr')
        try :

            sum2 = sums[1]
            sum2_1 = sum2.xpath('.//li[1]/img/@src')[0]
            sum2_2 = sum2.xpath('.//li[3]/img/@src')[0]
            pic2 = sum2.xpath('.//td[@class="champion-overview__stats champion-overview__stats--pick"]/strong/text()')[0]
            win2 = sum2.xpath('.//td[@class="champion-overview__stats champion-overview__stats--win"]/strong/text()')[0]
            sss.append(1)
            sum2s = [sum2_1, sum2_2]
        except :

            sum2s = ''
        sum1 = sums[0]
        sum1_1 = sum1.xpath('.//li[1]/img/@src')[0]
        sum1_2 = sum1.xpath('.//li[3]/img/@src')[0]
        pic1 = sum1.xpath('.//td[@class="champion-overview__stats champion-overview__stats--pick"]/strong/text()')[0]
        win1 = sum1.xpath('.//td[@class="champion-overview__stats champion-overview__stats--win"]/strong/text()')[0]
        sum1s  = [sum1_1,sum1_2]


        for summon in summons:
            for s in sum1s:
                if summon in s:
                    s1.append(summon)
                else:
                    pass
        if sum2s:
            for summon in summons:
                for s in sum2s:
                    if summon in s:
                        s2.append(summon)
                    else:
                        pass
            ss2 = [s2,[pic2,win2]]
            s = {'召唤师技能': [[s1, [pic1, win1]], ss2]}
        else:
            s = {'召唤师技能': [s1, [pic1, win1]]}
        #str1 = s1,'选取率为:'+pic1,'胜率为:'+win1
        #str2 = s2,'选取率为:'+pic2,'胜率为:'+win2

        return s
    #解析技能升级
    def get_skills():
        skills = tree.xpath('//table[@class="champion-skill-build__table"]//tr[2]/td')
        skill1 = []
        count = 0
        # 解析出技能的顺序
        for skill in skills:
            s = skill.xpath('./text()')[0]
            s = "".join(s.split())
            count += 1
            # 第一个技能加满时
            if count == 9:
                cq = skill1.count('Q')
                cw = skill1.count('W')
                ce = skill1.count('E')

                count_all = {cq: "Q", cw: "W", ce: "E"}
                cts = list(count_all.keys())
                ss = max(cts)
                s = count_all[ss]

            # 第二个技能加满时
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
        # 解析出技能胜率
        pics = tree.xpath('//td[@class="champion-overview__stats champion-overview__stats--pick"]/strong/text()')[2]


        if sss:
            wins = tree.xpath('//td[@class="champion-overview__stats champion-overview__stats--win"]/strong/text()')[2]
        else :
            wins = tree.xpath('//td[@class="champion-overview__stats champion-overview__stats--win"]/strong/text()')[1]


        return [skill1, [pics, wins]]
    #解析曲线
    def get_quxian():
        win = tree.xpath('//div[@class="champion-box champion-box--trend"]/div[@class="champion-box-content"]/script/text()')[2]
        ex = '"y":(.*?),"r'
        wins = re.findall(ex, win)
        return  wins
    #解析出装
    #def get_build():
        # tree = etree.HTML(page_text1)
        # buildsd = {}
        # # 核心出装：
        # buildsd = {}
        # mainblist = []
        # mainpwlist = []
        # mbuilds = tree.xpath('/html/body/div/div[1]/div[1]/div/table/tbody/tr')
        # for tr in mbuilds:
        #     builds = tr.xpath('./td/ul/li[@class="champion-stats__list__item tip"]/@title')
        #     slist = []
        #     for title in builds:
        #         ex = "<b style='color: #00cfbc'>(.*?)</b><br><span>"
        #         item = re.findall(ex, title)[0]
        #         slist.append(item)
        #     mainblist.append(slist)
        #     pick = tr.xpath('./td[2]/text()')[0]
        #     pick = "".join(pick.split())
        #     win = tr.xpath('./td[3]/text()')[0]
        #     mainpwlist.append([pick, win])
        # biglist = []
        # for c in range(len(mainblist)):
        #     biglist.append([mainblist[c], mainpwlist[c]])
        # buildsd['核心出装'] = [biglist]
        #
        # # 鞋子：
        # xieblist = []
        # xiepwlist = []
        # biglist = []
        # xiebuilds = tree.xpath('/html/body/div/div[1]/div[2]/div/table/tbody/tr')
        # for tr in xiebuilds:
        #     build = tr.xpath('.//div[@class="champion-stats__single__item"]//span/text()')[0]
        #     xieblist.append(build)
        #     pick = tr.xpath('.//td[2]/text()')[0]
        #     pick = "".join(pick.split())
        #     win = tr.xpath('.//td[3]/text()')[0]
        #     biglist.append([build, [pick, win]])
        # buildsd['鞋子'] = biglist
        # ###############################################################################
        # # 出门装
        # firstlist = []
        # firstpwlist = []
        # biglist = []
        # firstbulids = tree.xpath('/html/body/div/div[1]/div[3]/div/table/tbody/tr')
        # for tr in firstbulids:
        #     builds = tr.xpath('./td/ul/li[@class="champion-stats__list__item tip"]/@title')
        #     slist = []
        #     for title in builds:
        #         ex = "<b style='color: #00cfbc'>(.*?)</b><br><span>"
        #         item = re.findall(ex, title)[0]
        #         slist.append(item)
        #     firstlist.append(slist)
        #     pick = tr.xpath('./td[2]/text()')[0]
        #     pick = "".join(pick.split())
        #     win = tr.xpath('./td[3]/text()')[0]
        #     firstpwlist.append([pick, win])
        # biglist = []
        # for c in range(len(firstpwlist)):
        #     biglist.append([firstlist[c], firstpwlist[c]])
        # buildsd['出门装'] = [biglist]
        # return buildsd
    #解析克制
    def get_counter():

        tree = etree.HTML(page_text2)
        datalist = tree.xpath('//div[@class="champion-matchup-champion-list__item  champion-matchup-champion-list__item--active"]')
        for itme in tree.xpath('//div[@class="champion-matchup-champion-list__item "]'):
            datalist.append(itme)
        alldata = []
        for data in datalist:
            data_champion_name = data.xpath('./@data-champion-name')[0]
            winrate = float(data.xpath('./@data-value-winrate')[0])
            alldata.append([data_champion_name,winrate])
        return alldata



    #[data_champion_name, data_champion_key, winrate]
    s = {}

    s = get_sums_win_pick()
    #s['技能'] = get_skills()
    #s['装备'] = get_build()
    s['克制'] = get_counter()
    s['曲线'] = get_quxian()
    all_data = nw[0]
    all_data[w][name] = s
    print(f'已下载{name}{w}')
def wirte_data(shuju):
    print('开始写入数据')
    with open('./data.txt','w+',encoding='utf-8')as t:
        s = json.dumps(shuju,ensure_ascii=False)
        t.write(s)
    print('写入完成')

def main():
    tasks = []
    all_data = {}
    all_data['上单'] = {}
    all_data['打野'] = {}
    all_data['中单'] = {}
    all_data['下路'] = {}
    all_data['辅助'] = {}
    div_list = get_champion_list()
    champins = get_url_name(div_list)
    #champins = {'圣枪游侠': ['/champion/lucian/statistics', ['下路', '中单', '上单']]}
    weizhi_trans = {'上单':'top','打野':'jungle','中单':"mid",'下路':'bot','辅助':'support'}


    for name,lists in champins.items():


        weizhi = lists[1]
        if lists[0] != 'rip':
            #获得英雄详情页面
            for w in weizhi:
                if w in weizhi_trans.keys():
                    url = 'https://www.op.gg'+lists[0]+'/'+weizhi_trans[w]
                elif w in weizhi_trans.values:
                    url = 'https://www.op.gg'+lists[0]+'/'+w
                #获得主页面
                c = get_main_web(url)

                task = asyncio.ensure_future(c)
                task.add_done_callback(partial(jieximainweb,[all_data,name,w]))
                tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    wirte_data(all_data)
if __name__ == '__main__':
    main()