#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/3/20 10:05'

import pyttsx3

#语音报警类，初始化引擎
class VoiceInitClass:

    def __init__(self):
        self.engine =pyttsx3.init()
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate - 71)  # 播放速度
        volume = self.engine.getProperty('volume')
        self.engine.setProperty('volume', volume + 0.9)  # 播放音量  0-1.0

    def getEngine(self):
       return   self.engine
