#coding:utf-8
#@Time : 2020/7/6 21:08
#@Author : 鲁乃源
#@File : reer.py
#@Software : PyCharm
import re

ex = "<b style='color: #00cfbc'>(.*?)</b><br><span>"
text = """<b style='color: #00cfbc'>双生暗影</b><br><span>提升法术强度和移动速度</span><br><span><stats>+70法术强度<br>+7%移动速度<br>+10%冷却缩减</stats><br><br><unique>唯一主动—幽魂索命：</unique>召唤2个可怖的幽魂去猎取附近的英雄，并在接触到目标后使其显形并萦绕于目标。<br><br>被萦绕的敌人会被减速40%，持续时间基于幽魂已行走的距离，最多可持续5秒。(90秒冷却时间)。</span><br><span>价格:</span> <span style='color: #ffc659'>2400 (650)</span>"""

print(re.findall(ex,text)[0])