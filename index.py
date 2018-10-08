#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: index.py
@time: 2018/9/17 15:34
'''
import web
import sys,os
import urllib
import json

#db = web.database(dbn='mysql',user='root',pw='123456',db='nagios_voice')

render = web.template.render('templates/')

urls = (
    #'/','index'
    #'/(.*)','index'
    #'/','index',
    '/','nagios_notification'

)

class index:
    '''
    def GET(self):
        name = 'Bob'
        return render.index(name)
    '''
    '''
    def GET(self,name):
        i = web.input(name=None)
        return render.index(name)
    '''
    '''
    def GET(self):
        todos = db.select('todo')
        return render.index(todos)
    '''

class nagios_notification:
    def POST(self):
        data = web.data()
        data = urllib.unquote(data)
        data_list = data.split(',')
        server_type = data_list[1].strip('+').strip('"').strip('"')
        business = data_list[2].strip('+').strip('"').strip(']').strip('"')
        if server_type == Hostname:
            if "_P" in business:
                print "点对点"
            elif "_M" in business:
                print "会议"
            elif "_C" in business:
                print "CDN"
            else:
                print "点对点"
        return render.index(server_type)

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()

