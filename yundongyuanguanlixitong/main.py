'''
Author: wang
Date: 2021-01-29 12:50:31
LastEditTime: 2021-01-29 13:53:05
LastEditors: Please set LastEditors
Description: wang
FilePath: \Desktopd:\.git\vscode\yundongyuanguanlixitong\main.py
'''


def 录入(name, all_result):

    result = {}
    for x in xiangmu:
        chengji = input(f'请输入项目“{x}”的成绩：')
        result[x] = chengji
    all_result[name] = result


def 修改(name, all_result):
    result = all_result[name]
    print(result)

    t = 0
    for x in xiangmu:
        t += 1
        print(t, x)
    x = int(input('请输入要修改的项目编号：'))
    x_key = xiangmu[x - 1]
    x = input('请输入要修改的值:')
    result[x_key] = x


def 删除(name, all_result):
    all_result.pop(name)
    print(all_result)


def main():

    #name = input("请输入姓名")
    name = "d"
    #all_result = {}

    all_result = {
        'd': {
            '八字滑行（不带球）（秒）': '1',
            '八字滑行（带球）（秒）': '12',
            '射门': '13',
            '6圈（分钟）': '14',
            '折线滑（秒）': '15',
            '躺举杠铃': '16',
            '握力器（左）': '17',
            '握力器（右）': '18',
            '曲臂悬挂': '19',
            '仰卧起坐': '20',
            '引体向上': '21',
            '模拟滑行': '22',
            '十字（秒）': '23',
            '三点（秒）': '24',
            '传球': '25',
            '侧躺（30°）': '26'
        }
    }
    录入(name, all_result)
    修改(name, all_result)
    删除(name, all_result)


xiangmu = [
    '八字滑行（不带球）（秒）', '八字滑行（带球）（秒）', '射门', "6圈（分钟）", '折线滑（秒）', '躺举杠铃', '握力器（左）',
    '握力器（右）', '曲臂悬挂', '仰卧起坐', '引体向上', '模拟滑行', '十字（秒）', '三点（秒）', '传球', '侧躺（30°）'
]

main()