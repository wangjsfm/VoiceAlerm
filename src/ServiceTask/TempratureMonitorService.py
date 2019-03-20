#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/3/20 11:00'

import  requests
import  pandas as pd
from  src.Config.AppParammeters import OpcApiUrl,UpperWaterWall_Area_1,\
    TeampratureDiffThrosh,LowerWaterWall_Area_1

from src.Dao.TempratureDao import tempreatureDiffHandle



#温差监控
def tempratureDiffMonit(VoiceText):
    opc_real_data = requests.get(OpcApiUrl).json()  # 获取OPC_API 接口软件实时数据
    pd_opc_real_data = pd.DataFrame(opc_real_data)  # 转为pandas的DataFrame数据格式，以便处理

    # 上部水冷壁处理
    alermData1 = tempreatureDiffHandle(pd_opc_real_data, UpperWaterWall_Area_1, TeampratureDiffThrosh, '1号机组，')
    # 下部水冷壁处理
    alermData2 = tempreatureDiffHandle(pd_opc_real_data, LowerWaterWall_Area_1, TeampratureDiffThrosh, '1号机组，')

    voieTextAppend(VoiceText,alermData1)
    voieTextAppend(VoiceText,alermData2)


#将报警文本，添加至主进的变量中
def voieTextAppend(voiceText,text):
    if text  != None:
        print(text)
        voiceText.append(text)  # 添加
