#根据每日的日期计算零花钱总数
#记录扣除的每一笔交易
#计算剩余的零花钱
#可以添加扣除的零花钱
#################引入模块#########################
import datetime
#################引入结束#########################
#起始日期 2020/11/01
d1 = datetime.datetime.strptime('2020-11-01 00:00:00', '%Y-%m-%d %H:%M:%S')

d2 = datetime.datetime.now()
delta = (d2 - d1).days


global all_money
all_money = 44 + (int(delta) * 4)
def change_money(use_money):
    global useed_money
    with open("used_money.txt","r") as t:
        
        useed_money = int(t.readline())
        useed_money = useed_money + use_money
        if all_money-useed_money >= 0:
            with open("used_money.txt","w+") as t:  
                t.write(str(useed_money))
                print_money()
        else:
            print(f'余额不足,当前剩余金额{all_money}.')

def print_money():
    print(f"当前累计金额{all_money},剩余{all_money-useed_money}")


change_money(50)



