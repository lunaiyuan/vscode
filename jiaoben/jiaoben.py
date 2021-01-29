'''
Author: your name
Date: 2021-01-07 18:20:54
LastEditTime: 2021-01-10 15:09:25
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \vscode\jiaoben\jiaoben.py
'''

def m(k,t,n):
    ks = []
    res = max(m(k,n-1),m(t-k,n))+1
    