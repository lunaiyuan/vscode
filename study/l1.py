'''
Author: your name
Date: 2020-11-20 11:08:16
LastEditTime: 2020-11-21 14:56:50
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \.git\vscode\study\l1.py
'''


def move(n, a, b, c):
    if n == 1:
        print(f"{a} - {c}")
    else:
        move(n - 1, b, a, c)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(5, "A", "B", "C")
