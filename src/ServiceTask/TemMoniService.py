#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/3/21 16:54'

from src.Dao.TempratureDao import AreaEstimate
import  requests
from  src.Config.AppParammeters import OpcApiUrl
import time
from src.Config.AppParammeters import TemprCyclTime

####  壁温监控

#机组监控
def TempratureMonitor(model,VoiceText):

    while True:
        opc_real_data = requests.get(OpcApiUrl).json()  # 获取OPC_API 接口软件实时数据
        BoilerUnit_1(model,opc_real_data,20,VoiceText)
        time.sleep(TemprCyclTime)



## 1机组相关区域，监控
#model：模型 map类型
#opc_real_data :数据
#presure：相应区域压力
#VoiceText：语音报警容器
def BoilerUnit_1(model,opc_real_data,presure,VoiceText):
    #上部水冷壁
    AreaEstimate('HighTemperatureSuperheater45_Area_1',opc_real_data,model['highTemperatureSuperheaterModle45'].curveFunction(40),VoiceText)






## 2机组，相关监控
def BoilerUnit_2():
    pass


#



