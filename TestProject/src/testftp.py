#-*- coding:utf-8 -*-
'''
Created on 2012-8-13

@author: GFTOwenWang
'''
import ftplib
from gftdata.share.ftputil import FTPHost


class MySession(ftplib.FTP):
    def __init__(self, host, userid, password, port):
        """Act like ftplib.FTP's constructor but connect to another port."""
        ftplib.FTP.__init__(self)
        self.connect(host, port)
        self.login(userid, password)
        
def test_func1():
    #ftphost = FTPHost("192.168.1.135","zzy", "zzy")
    ftphost = FTPHost("180.166.0.130:40001","zzy", "zzy")
    print 'ok'
    
def test_func2():
    #ftphost = FTPHost("192.168.1.135","zzy", "zzy")
    ftphost = FTPHost("180.166.0.130","zzy", "zzy",port=40001,session_factory=MySession)
    print 'ok'
    
    
if __name__ == "__main__":
    test_func1()