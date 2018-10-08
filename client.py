#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: client.py
@time: 2018/9/29 14:26
'''
import os,sys
import httplib
import urllib
import json

data = sys.argv

def RequestUrl(host,port,source,params,timeout):

    headers = {"Content-type":"application/x-www-form-urlencoded"}

    try:
        conn = httplib.HTTPConnection(host,port,timeout)
        conn.request('POST',source,params,headers)
        response = conn.getresponse()
        content = response.read()
        print content
    except Exception,e:
        print e

if __name__ == "__main__":
    try:
        RequestData = urllib.urlencode({"data":json.dumps(data)})
        result = RequestUrl("10.160.92.65","8080","/",RequestData,30)
    except Exception,e:
        print e