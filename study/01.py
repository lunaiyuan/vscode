'''
Author: Pilzz
Date: 2020-11-02 15:02:13
LastEditTime: 2020-11-07 21:06:59
FilePath: \siming\数据可视化\01.py
'''
#import matplotlib.pyplot as plt

#squares = [1,4,9,16,25]
#plt.plot(squares,linewidth = 5)
# plt.show()
""" 
# plot 绘制线
squares = [1,4,9,16,25]  
plt.plot(squares,linewidth = 5)                         #设置左边数字
plt. title("Squares",fontsize = 24)                     #设置标题
plt.xlabel("value",fontsize = 14)                       #设置下方标题
plt.ylabel("squares of value",fontsize = 14)            #设置左边标题
plt.tick_params(axis="both",labelsize = 14)             #设置刻度
plt.show() 
"""
""" 
squares = [1,4,9,16,25]
input_value = [1,2,3,4,5]
plt.plot(input_value,squares,linewidth = 5)
plt.title("Squares",fontsize = 24)
plt.xlabel('value',fontsize = 14)
plt.ylabel('squares',fontsize = 14)
plt.tick_params(axis="both",labelsize = 14)
plt.show()
 """
# scatter 绘制点
""" 
x_value = range(1,1001)
y_value = [x**2 for x in x_value]

plt.scatter(x_value,y_value,s = 10,edgecolors= "none",c=y_value,cmap=plt.cm.Blues)
plt.scatter(x_value,x_value,s = 10,edgecolors= "none",c=y_value,cmap=plt.cm.Blues)

plt.title("squares",fontsize = 24)
plt.xlabel("value",fontsize = 14)
plt.ylabel("value of squares",fontsize = 14)
plt.tick_params(axis="both",labelsize = 10)
plt.show() """

# test
""" xValue = range(1, 5001)
yValue = [x**3 for x in xValue]

plt.scatter(xValue, yValue, s=10, edgecolors="none")
plt.xlabel("value", fontsize=14)
plt.ylabel("3squares", fontsize=14)
plt.title("3squares", fontsize=24)
plt.tick_params(axis="both", labelsize=10)
plt.show() """

a = "h汉t汉t汉p汉s://汉m汉3347.g汉i汉t汉h汉u汉b汉.i汉o"
b = a.replace("汉", "")
print(b)