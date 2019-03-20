#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/3/20 11:00'

import  requests,time
import  pandas as pd
from  src.Config.AppParammeters import OpcApiUrl,UpperWaterWall_Area_1,\
    TeampratureDiffThrosh,LowerWaterWall_Area_1,MonitorCyclTime

from src.Dao.TempratureDao import tempreatureDiffHandle



#温差监控
def tempratureDiffMonit(VoiceText):

    while True:

        opc_real_data = requests.get(OpcApiUrl).json()  # 获取OPC_API 接口软件实时数据
        pd_opc_real_data = pd.DataFrame(opc_real_data)  # 转为pandas的DataFrame数据格式，以便处理

        # 上部水冷壁处理
        alermData1 = tempreatureDiffHandle(pd_opc_real_data, UpperWaterWall_Area_1, TeampratureDiffThrosh, '1号炉，')
        # 下部水冷壁处理
        alermData2 = tempreatureDiffHandle(pd_opc_real_data, LowerWaterWall_Area_1, TeampratureDiffThrosh, '1号炉，')

        voieTextAppend(VoiceText,alermData1)
        voieTextAppend(VoiceText,alermData2)
        time.sleep(MonitorCyclTime)


#将报警文本，添加至主进的变量中
def voieTextAppend(voiceText,text):
    if text  != None:

        text = str(text)
        #前墙上部水冷壁出口从炉左向炉右数第31根管子壁温
        text = text.replace('部水冷壁出口从炉左向炉右数第', '').replace('管子壁温','')
        #侧墙上部右侧水冷壁出口从炉前向炉后数第24根管子壁温
        text = text.replace('部右侧水冷壁出口从炉前向炉后数第','').replace('管子壁温','')
        #侧墙下部左侧水冷壁出口从炉前向炉后数第24根管子壁温
        text = text.replace('部左侧水冷壁出口从炉前向炉后数第','').replace('管子壁温','')

        print(text)
        voiceText.append(text)  # 添加
