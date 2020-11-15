#-*- codeing = utf-8 -*-
#@Time : 2020/6/24 17:57
#@Author : 鲁乃源
#@File : freemp3.py
#@Software : PyCharm
import requests
class Freemp3():
    def __init__(self,name):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
        self.name = name
    def get_download_url(self):
        url = f'http://api.migu.jsososo.com/search?keyword={self.name}'
        response = requests.get(url)

headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
name = '狂浪'
url = f'http://api.migu.jsososo.com/search?keyword={name}'
response = requests.get(url)
print(response)