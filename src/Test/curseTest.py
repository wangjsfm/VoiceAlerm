#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/3/21 9:03'

import matplotlib as plt
import  numpy as np


#屏式过热器45
x7 = [9.6,15.09,20.57,26.06,27.31]
y7 = [630,630,615,605,600,1]
title7 = '屏式过热器45 厂家提供数据'

#折线函数
def CurveFunFit(x,y):

    if len(x)!=0 & len(y)!= 0:
        if len(x) == len(y):
          pass

        else:
            raise ValueError('输入数据,长度不一致')
    else:
        raise ValueError('输入数据,不能为空')


if __name__ == '__main__':
    CurveFunFit(x7,y7)

