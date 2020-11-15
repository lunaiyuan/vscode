#-*- codeing = utf-8 -*-
#@Time : 2020/6/5 15:27
#@Author : 鲁乃源
#@File : guess.py
#@Software : PyCharm
import requests
from bs4 import BeautifulSoup as soup
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
name = '狂浪'
url = f'https://music.163.com/#/search/m/?s={name}type=1'
response = requests.get(url=url , headers = headers)
page_text = soup.find_all(response,a href)
print(page_text)
url = 'http://music.163.com/song/media/outer/url?id=1331819040.mp3'