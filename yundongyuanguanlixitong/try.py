'''
Author: your name
Date: 2021-01-29 21:59:46
LastEditTime: 2021-02-03 16:53:32
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Desktopd:\.git\vscode\yundongyuanguanlixitong\try.py
'''
import json
with open('user.txt', "r") as t:
    user_json = json.loads(t.read())

    a = t.read()
    print(a, "1")
