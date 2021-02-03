'''
Author: wang
Date: 2021-01-29 12:50:31
LastEditTime: 2021-02-03 17:04:02
LastEditors: Please set LastEditors
Description: wang
FilePath: \Desktopd:\.git\vscode\yundongyuanguanlixitong\main.py
'''
################import######################
import json
import xlwt


############################################
def judge(r):
    try:
        r = float(r)
        return r
    except:
        r = input('格式错误，请重新输入：')
        rs = judge(r)
        return rs


def 录入(name, all_result):
    result = {}
    while True:
        t = input('球员类型（1,2）：')
        if t == "1":
            result['球员类型'] = '球员'
            xm = xiangmu[0]
            break
        elif t == "2":
            result['球员类型'] = '守门员'
            xm = xiangmu[1]
            break
        else:
            print('格式错误，请重新输入！')

    for x in xm:
        r = input(f'请输入项目“{x}”的成绩：')
        r = judge(r)
        result[x] = r
    all_result[name] = result


def 修改(name, all_result):
    try:
        result = all_result[name]
    except:
        name = input('查无此人，请重新输入')
        修改(name, all_result)
        return

    play_type = result['球员类型']
    if play_type == "球员":
        xm = xiangmu[0]
    elif play_type == "守门员":
        xm = xiangmu[1]

    t = 0
    for k, v in result.items():
        t += 1
        print(t, k, v)

    x = input('请输入要修改的项目编号：')
    """ def judge_cout(x):
        try: 
            x = int(x)
            if 0<x<17:
                return x
            else:
                x = input("请重新输入正确编号：")
                judge_cout(x)
                return x
        except :
            x = input("请重新输入正确编号：")
            judge_cout(x)
            return x """
    try:
        if x == "1":
            if result['球员类型'] == '球员':
                result['球员类型'] == '守门员'
            else:
                result['球员类型'] == '球员'
        else:
            x = int(x)
            x_key = xm[x]
    except:
        print('请按照格式从新输入')
        修改(name, all_result)
        return
    #x = judge_cout(x)

    r = input('请输入要修改的值:')
    judge(r)
    result[x_key] = r


def 删除(name, all_result):
    all_result.pop(name)
    print(all_result)


def 制表():
    book = xlwt.Workbook()
    #制作表头1
    sht1 = book.add_sheet("sheet1")
    sht1.write_merge(0, 1, 0, 0, "№")

    sht1.write_merge(0, 1, 1, 1, "姓名")

    sht1.write_merge(0, 0, 2, 3, '握力器')
    sht1.write_merge(0, 0, 4, 5, '躺举杠铃')
    sht1.write_merge(0, 0, 6, 7, '曲臂悬垂')
    sht1.write(0, 8, '仰卧起坐')
    sht1.write(0, 9, '引体向上')
    sht1.write(0, 10, '模拟滑行')

    sht1.write(1, 2, '左')
    sht1.write(1, 3, '右')
    sht1.write_merge(1, 1, 4, 5, '成绩')
    sht1.write_merge(1, 1, 6, 7, '成绩')
    sht1.write(1, 8, '成绩')
    sht1.write(1, 9, '成绩')
    sht1.write(1, 10, '成绩')
    #制作表头2
    sht2 = book.add_sheet("sheet2")
    sht2.write_merge(0, 2, 0, 0, "№")
    sht2.write_merge(0, 2, 1, 1, "姓名")
    sht2.write(0, 2, '8字滑行')
    sht2.write(0, 3, '8字滑行')
    sht2.write_merge(0, 1, 4, 4, '射门')
    sht2.write(0, 5, '6圈')
    sht2.write(0, 6, '折线滑')
    sht2.write(1, 2, '（不带球）（秒）')
    sht2.write(1, 3, '（带球）（秒）')
    sht2.write(1, 5, '（分钟）')
    sht2.write(1, 6, '（秒）')
    for t in range(2, 7):
        sht2.write(2, t, '成绩')
    #制作表头3
    sht3 = book.add_sheet("sheet3")
    sht3.write_merge(0, 1, 0, 0, "№")
    sht3.write_merge(0, 1, 1, 1, "姓名")
    sht3.write(0, 2, '十字（秒')
    sht3.write(0, 3, '三点（秒')
    sht3.write(0, 4, '传球')
    sht3.write(0, 5, '侧躺')
    sht3.write(0, 6, '积分数')
    sht3.write(0, 7, '评分')
    for t in range(2, 6):
        sht3.write(1, t, '成绩')

    #制作表头4
    sht4 = book.add_sheet("sheet4")
    sht4.write_merge(0, 1, 0, 0, "№")
    sht4.write_merge(0, 1, 1, 1, "姓名")
    sht4.write_merge(0, 0, 2, 3, "握力器")
    sht4.write(0, 4, '躺举杠铃')
    sht4.write(0, 5, '引体向上')
    sht4.write(0, 6, '仰卧起坐')
    sht4.write(0, 7, '曲臂悬垂')
    sht4.write(0, 8, '模拟滑行')
    sht4.write_merge(0, 0, 9, 10, "积分")
    sht4.write_merge(0, 0, 11, 12, "评分")
    sht4.write(1, 2, '左')
    sht4.write(1, 3, '右')
    for t in range(4, 9):
        sht4.write(1, t, '成绩')
    #填入数据
    with open('data.txt', 'r') as t:
        all_result = json.loads(t.read())
    row = 2
    no = 1
    for k, v in all_result.items():
        if v['球员类型'] == '球员':
            #填入表1数据
            sht1.write(row, 0, no)
            sht1.write(row, 1, k)
            line = 2
            for xm in xiangmu[0][:7]:
                if line == 4:
                    sht1.write_merge(row, row, 4, 5, v['躺举杠铃'])
                    sht1.write_merge(row, row, 6, 7, v['曲臂悬垂'])
                    line += 3
                else:
                    sht1.write(row, line, v[xm])
                line += 1
            row += 1

            #填入表2数据
            sht2.write(row, 0, no)
            sht2.write(row, 1, k)

            line = 2
            for xm in xiangmu[0][7:]:
                sht2.write(row, line, v[xm])
                line += 1
            no += 1
        elif v['球员类型'] == '守门员':
            #填入表3数据
            sht3.write(row, 0, no)
            sht3.write(row, 1, k)
            line = 2
            for xm in xiangmu[2][:4]:
                sht3.write(row, line, v[xm])
                line += 1
            #填入表4数据
            sht4.write(row, 0, no)
            sht4.write(row, 1, k)
            line = 2
            for xm in xiangmu[2][4:]:
                sht4.write(row, line, v[xm])
                line += 1

    book.save("成绩测试.xlsx")


xiangmu = [[
    '握力器（右）', '握力器（左）', '躺举杠铃', '曲臂悬垂', '仰卧起坐', '引体向上', '模拟滑行', '八字滑行（不带球）（秒）',
    '八字滑行（带球）（秒）', '射门', "6圈（分钟）", '折线滑（秒）'
],
           [
               '十字（秒)', '三点（秒）', '传球', '侧躺（30°）', '握力器（左）', '握力器（右）', '躺举杠铃',
               '引体向上', '仰卧起坐', '曲臂悬垂', '模拟滑行'
           ]]


def main():
    try:
        with open('data.txt', 'r') as t:
            all_result = json.loads(t.read())
    except:
        all_result = {}

    while True:
        x = input('增，改，删')

        if x == "1":
            name = input('名字')
            print(1)
            录入(name, all_result)
        elif x == "2":
            name = input('名字')
            修改(name, all_result)
        elif x == "3":
            name = input('名字')
            删除(name, all_result)
        else:
            exit()
        with open('data.txt', 'w') as t:
            a = json.dumps(all_result)
            t.write(a)
    #name = input("请输入姓名")

    #录入(name, all_result)
    #修改(name, all_result)
    #删除(name, all_result)
    #print(all_result)


#main()
制表()