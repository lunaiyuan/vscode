'''
Author: your name
Date: 2020-11-22 00:27:24
LastEditTime: 2020-11-22 11:00:04
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \.git\vscode\renlianshibie\1.py
'''
import requests
import base64
import json
'''
人脸对比
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
filename1 = "vscode/renlianshibie/p1.jpg"
filename2 = "vscode/renlianshibie/p2.jpg"
f1 = open(filename1, 'rb')
f2 = open(filename2, 'rb')
img_test1 = base64.b64encode(f1.read())
img_test2 = base64.b64encode(f2.read())

params = json.dumps([{
    "image": str(img_test1, 'utf-8'),
    "image_type": "BASE64",
    "face_type": "LIVE",
    "quality_control": "LOW"
}, {
    "image": str(img_test2, 'utf-8'),
    "image_type": "BASE64",
    "face_type": "LIVE",
    "quality_control": "LOW"
}])
access_token = '24.6b3b81faf430fb6fa054683dd528c333.2592000.1608569852.282335-23022308'

request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/json'}
response = requests.post(request_url, data=params, headers=headers)
js = response.json()
if js['error_msg'] == 'SUCCESS':
    score = js['result']['score']
    print('两张图片相似度：', score)
else:
    print('错误信息：', js['error_msg'])

import matplotlib.pyplot as plt
import tkinter.messagebox

tkinter.messagebox.showinfo('图片相似度',
                            "两个人的相似度为：%d" % js['result']['score'] + "%")
pc1 = plt.imread(filename1)
pc2 = plt.imread(filename2)
plt.imshow(pc1)
plt.show()
plt.imshow(pc2)
plt.show()
