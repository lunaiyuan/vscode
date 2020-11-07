'''
Author: your name
Date: 2020-11-04 11:34:54
LastEditTime: 2020-11-07 11:33:20
LastEditors: your name
Description: In User Settings Edit
FilePath: \siming\数据可视化\02.py
'''
from random import choice
import matplotlib.pyplot as plt


class RandomWalk():
    def __init__(self, num_point=5000):
        #初始化
        self.num_point = num_point
        #开始于0
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        def get_STEP():
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            return x_step

        while len(self.x_value) < self.num_point:
            #决定前进的方向以及距离
            x_step = get_STEP()
            y_step = get_STEP()

            #拒绝原地
            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)


while True:
    rw = RandomWalk()
    rw.fill_walk()
    num_point = range(rw.num_point)
    plt.figure(figsize=(10, 6))
    plt.scatter(rw.x_value, rw.y_value, c=num_point, s=15)

    plt.show()

    keep_running = input("y/n?")
    if keep_running == "n":
        break