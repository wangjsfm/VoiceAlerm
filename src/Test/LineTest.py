#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/3/21 9:43'

import matplotlib.pyplot as plt
import numpy as np
from src.Config import ModelData





class TempreturePointFit:

    kList = []
    bList = []

    #初始化时就将K、B参数设置好
    #输入参数是，首尾多两条数据
    def __init__(self,x,y):
        self.x = x
        if len(x) == len(y):
            for i in range(len(x)):
                if i + 1 < len(x):
                    k = (y[i] - y[i + 1]) / (x[i] - x[i + 1])
                    b = y[i] - (x[i] * k)
                    self.kList.append(k)
                    self.bList.append(b)
        else:
            raise ValueError('输入数据长度，不一致')

    #根据返回温度定值  y= k x +b 分段函数
    def curveFunction(self,presure):

        for i in range(len(self.x)):
            if i + 1 < len(self.x):
                if self.x[i] <= presure <= self.x[i + 1]:
                    y = self.kList[i] * presure + self.bList[i]
                    return y

    def curve2(self,presure):
        for i in range(len(self.x)):
            if i + 1 < len(self.x):
                if self.x[i] <= presure <= self.x[i + 1]:
                    y = self.kList[i] * presure + self.bList[i]
                    return y




if __name__ == '__main__':

    tf = TempreturePointFit(ModelData.x3,ModelData.y3)
    y = tf.curveFunction(26.06)
    yList = []
    xList = np.arange(0,30,0.1)
    for item in xList:
        yList.append(tf.curveFunction(item))


    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(1)
    plt.plot(ModelData.x3,ModelData.y3)

    plt.figure(2)
    plt.title(ModelData.title3 + ' 拟合的折线函数')
    plt.plot(xList,yList)

    plt.show()
    # yList = []
    # xList = np.arange(0, 40, 0.1)
    # for item in xList:
    #     yList.append(modelMap['highTemperatureReheaterModle'].curveFunction(item))
    #
    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.figure(1)
    #
    # plt.title( ModelData.title4)
    #
    # plt.plot(ModelData.x12, ModelData.y12)
    #
    # plt.figure(2)
    # plt.title(ModelData.title3 + ' 拟合的折线函数')
    #
    # plt.plot(xList, yList)
    # plt.show()