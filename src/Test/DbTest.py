#coding=utf-8
#Version: V 1.0
author: 'WangSheng'
date: '2019/3/20 15:15'

import redis

#redis123456
if __name__ == '__main__':
    pool = redis.ConnectionPool(host='localhost', port=6379, password='redis123456', db=1, decode_responses=True)
    r = redis.StrictRedis(connection_pool=pool)


    # print(r.hkeys())


    keys = r.keys()
    for item in keys:
        print(str(item).replace(':1:',''))


