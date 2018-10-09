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

db = web.database(dbn='mysql',user='root',pw='123456',db='nagios_voice',host='localhost')

render = web.template.render('templates/')

urls = (
    #'/','index'
    #'/(.*)','index'
    #'/','index',
    '/','nagios_notification',
    '/index','nagios_view'

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
        db.insert('nagios_voice',server_type=server_type,business=business,status=0)
        return "data ok"

class nagios_view():
    def GET(self):
        status_list = []
        status = db.select('nagios_voice',what="id,server_type,business",where="status = 0")
        for item in status:
            status_list.append(item)
        if status_list:
            id_list = status_list[0].id
            server_type_list = status_list[0].server_type
            business_list = status_list[0].business
            db.update('nagios_voice', where='id=$id', vars={'id': id_list}, status=1)
            if "_P" in business_list:
                return render.index(server_type_list,"P")
            elif "_M" in business_list:
                return render.index(server_type_list,"M")
            elif "_C" in business_list:
                return render.index(server_type_list,"C")
            else:
                return render.index(server_type_list,"P")
        else:
            return render.index("aa","aa")

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()

