#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/3/20 10:25'

from src.Dao.VoiceEngine import  VoiceInitClass
import time

# from src.MainTask.main import VoiceText


def VoiceTask(voiceText):
    # 获取语音报警实例

    engine = VoiceInitClass().getEngine()
    try:

        while True: #程序一直监视

            if len(voiceText):
                while len(voiceText):
                    engine.say(voiceText[0])
                    voiceText.pop(0)  # 将已经移入报警引擎的数据 删除

                engine.runAndWait()  # 将报警信息加入 报警引擎

            time.sleep(5) #扫描间隔 1S

    except:
        engine.stop()
    pass