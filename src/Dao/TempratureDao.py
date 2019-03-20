#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/3/20 11:11'


from django.core.cache  import cache
from datetime import datetime


#删除缓存并持久化
def removeCatch(areaTag):

    get_catch_data = cache.get(areaTag)
    if get_catch_data != None:
        print('删除缓存并持久化')
        cache.delete(areaTag)  # 报警结束 删除缓存




#   dataList：壁温数据
#   areaTage：所监测的区域名称
#   diffThresholdValuet：壁温温差定值
#   unit 机组号
def tempreatureDiffHandle(dataList,areaTage,diffThresholdValuet,unit):

    maxValue=[0,'','']  # 0：最大值，1：标签名，2:标签描述
    minvalue = [0,'','']   # 0：最小值，1：标签名，2:标签描述
    alermTextContent = None
    opc_client_api_data = dataList[dataList['GroupName'] == areaTage]  # 获取指定区域的数据
    pd_filter_data = opc_client_api_data[['ItemID', 'Name', 'Value']]  # 获取指定字段的数据
    flag = 0


    # 从opc中获取 区域最大值，最小值
    for index, row in pd_filter_data.iterrows():
        tagName = row['ItemID']
        tagDesc = row['Name']
        tagValue = round(float(row['Value']), 2)

        if tagValue < 0.01:  # 防止数据为负值
            tagValue = 0

        if flag == 0: #初始化 最大最小值

            minvalue[0] = tagValue
            minvalue[1] = tagName
            minvalue[2] = tagDesc

            maxValue[0] = tagValue
            maxValue[1] = tagName
            maxValue[2] = tagDesc

            flag =1


        if tagValue > maxValue[0]:  #判断当前数据是否为最大值
            maxValue[0] = tagValue
            maxValue[1] = tagName
            maxValue[2] = tagDesc
        elif tagValue < minvalue[0]:  #判断当前数据是否为最小值
            minvalue[0] = tagValue
            minvalue[1] = tagName
            minvalue[2] = tagDesc

    diffValue = round(maxValue[0] - minvalue[0] , 2)

    # 区域最大，最小差值大于定值，将数据更新（新建）至redis
    if  diffValue >  diffThresholdValuet:

        #存入redis缓存
        # alermRedisHandle(areaTage,diffValue,maxValue,minvalue )

        #生成报警信息
        alermTextContent = unit+str(maxValue[2])+','+str(minvalue[2])+',偏差'+str(diffValue)+'度'
        # print(alermTextContent)

    #无报警，删除对于区域缓存数据，并将缓存数据存入数据库
    else:
        #删除缓存及持久化
        # removeCatch(areaTage)
        pass

    #返回报警信息
    return  alermTextContent


















#报警数据存入redis缓存处理
def alermRedisHandle(areaTage,diffValue,maxValueList,minValueList):

    get_diffValue_catch = cache.get(areaTage)
    maxValue = maxValueList[0]
    minValue = minValueList[0]

    #新建一条缓存信息
    if get_diffValue_catch is None :
        cache.set(areaTage,{
            'maxTageName':maxValueList[1],
            'maxTageDesc': maxValueList[2],
            'maxTageValue':maxValue,
            'minTageName': minValueList[1],
            'minTageDesc': minValueList[2],
            'minTageValue':minValue,
            'beginDate': datetime.now(),
            'diffValue':diffValue, #偏差值
        },
         timeout=None,  # 永不超时
        )

    #更新缓存信息
    else:

        #若传入偏差值大于 redis缓存中的值，则更新缓存
        if diffValue > get_diffValue_catch['diffValue'] :
            get_diffValue_catch['diffValue'] = diffValue
        elif maxValue > get_diffValue_catch['maxTageValue'] :
            get_diffValue_catch['maxTageValue'] = maxValue
        elif minValue >get_diffValue_catch['minTageValue'] :
            get_diffValue_catch['minTageValue'] = minValue

        cache.set(areaTage, get_diffValue_catch, timeout=None)  # 更新数据到redis



