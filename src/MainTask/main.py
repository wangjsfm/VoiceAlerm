#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/3/20 8:31'

import  threading,time
from src.ServiceTask.VoiceService import VoiceTask
from src.ServiceTask.TemDiffMonitorService import tempratureDiffMonit
from src.ServiceTask.ModInitService import TempModelInit
VoiceText= ['系统已上线，开始监测锅炉壁温....',]


def test(vo):
    while True:
        print(vo)
        time.sleep(2)

if __name__ == '__main__':

    #各区域模型
    areaModelMap = TempModelInit()

    voieThread = threading.Thread( target=VoiceTask, args=(VoiceText,) )
    diffMonitorThread = threading.Thread(target=tempratureDiffMonit, args=(VoiceText,))
    # testThread = threading.Thread( target=test, args=(VoiceText,) )

    voieThread.start()
    # testThread.start()
    diffMonitorThread.start()


