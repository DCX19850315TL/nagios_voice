#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: temp.py
@time: 2018/10/8 15:02
'''
if server_type == "Hostname":
    if "_P" in business:
        return render.index("Hostname", "P")
        # print "点对点"
    elif "_M" in business:
        return render.index("Hostname", "M")
        # print "会议"
    elif "_C" in business:
        return render.index("Hostname", "C")
        # print "CDN"
    else:
        return render.index("Hostname", "P")
        # print "点对点"
# return render.index(server_type)
elif server_type == "Server":
    if "_P" in business:
        return render.index("Server", "P")
        # print "点对点"
    elif "_M" in business:
        return render.index("Server", "M")
        # print "会议"
    elif "_C" in business:
        return render.index("Server", "C")
        # print "CDN"
    else:
        return render.index("Server", "P")
else:
    pass

#id_list = []
#last_id = db.query("SELECT LAST_INSERT_ID()")
        #for item in last_id:
        #    id_list.append(item)
        #print id_list[0]
        #print type(id_list)