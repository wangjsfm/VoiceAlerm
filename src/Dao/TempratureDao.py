#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/3/21 16:59'

import pandas as pd



### 区域温度监控
#areaName:区域名
#opc_real_data：实时数据
#curveFun :折线函数
#presure：相应区域压力，用以生成报警定值
def AreaEstimate(areaName,opc_real_data,alermValue,VoiceText):

    opc_client_api_data = getUrlDataHandle(opc_real_data, areaName)#获取指定区域数据
    pd_filter_data = opc_client_api_data[['ItemID', 'Name', 'Value']]  # 获取指定字段的数据

    # 从opc中获取 单条数据
    for index, row in pd_filter_data.iterrows():
        tagName = row['ItemID']
        tagDesc = row['Name']
        tagValue = round(float(row['Value']), 2)

        if tagValue < 0.00001:  # 防止数据为负值
            tagValue = 0

        alermText = TempratureEstimate(alermValue, tagValue, tagDesc)
        VoiceText.append(alermText)





#温度点超温判断
#curveFun :折线函数
#tempr: 温度点 值
#presure:压力
#temprDesc:温度点 描述
def TempratureEstimate(alarmValuea,tagValue,tagDesc):

    result = None
    if tagValue >alarmValuea:
        result = (tagDesc + ',超温').replace('管子壁温', '')

    print("当前值： "+ str(tagValue)+'  定值： '+str(alarmValuea)+'  点名：'+result)
    return result

#从OPC接口软件中获取数据,并拿出指定区域的数据
def getUrlDataHandle(opc_real_data,area):

        pd_opc_real_data = pd.DataFrame(opc_real_data)  # 转为pandas的DataFrame数据格式，以便处理
        pd_condition_data = pd_opc_real_data[pd_opc_real_data['GroupName'] == area]  # 获取指定区域的数据

        return pd_condition_data


