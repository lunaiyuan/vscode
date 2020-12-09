'''
Author: your name
Date: 2020-12-08 19:40:35
LastEditTime: 2020-12-09 02:23:55
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \.git\vscode\flask\myweb\severs.py
'''
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
