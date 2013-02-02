#-*- coding:utf-8 -*-
'''
Created on 2012-1-5

@author: GFTOwenWang
'''
import socket
print socket.gethostname()

localIP = socket.gethostbyname(socket.gethostname())#这个得到本地ip
print "local ip:%s "%localIP

ipList = socket.gethostbyname_ex(socket.gethostname())
for i in ipList:
    if i != localIP:
       print "external IP:%s"%i
       
print '=='
myname = socket.getfqdn(socket.gethostname())
myaddr = socket.gethostbyname(myname)
print myname
print myaddr