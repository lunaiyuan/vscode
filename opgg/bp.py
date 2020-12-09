#-*- codeing = utf-8 -*-
#@Time : 2020/7/8 21:53
#@Author : 鲁乃源
#@File : bp.py
#@Software : PyCharm
import json

def get_data():
    with open('./data.txt','r+',encoding='utf-8')as t:
        txt = json.load(t)
        return txt





def main():
    txt = get_data()


if __name__ == '__main__':
    main()