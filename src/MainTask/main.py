#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/3/20 8:31'

import  time,threading
from src.ServiceTask.VoiceService import VoiceTask

VoiceText= ['系统已上线，开始监测锅炉壁温....','进入系统了',
               '退出系统了']

if __name__ == '__main__':

    voieThread = threading.Thread(target=VoiceTask, args=(VoiceText,))
    voieThread.start()


