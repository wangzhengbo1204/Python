#-*- coding:utf-8 -*-
'''
Created on 2011-9-29

@author: GFTOwenWang
'''

import urllib,urllib2,cookielib
#def post3():
#    #formail.sina.com.cn
#    
#    cj=cookielib.CookieJar()
#    url_login='http://mail.sina.com.cn/cgi-bin/login.cgi'
#    body=(('logintype','login'),('u','username'),
#    ('psw','********'))
#    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#    #opener.addheaders=[('User-agent','Opera/9.23')]
#    opener.addheaders=[('User-agent',
#    'Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)')]
#    urllib2.install_opener(opener)
#    req=urllib2.Request(url_login,urllib.urlencode(body))
#    u=urllib2.urlopen(req)
#    print u.read().decode('utf-8').encode('gbk')
    
    
def post3():
    #formail.sina.com.cn
    
    cj=cookielib.CookieJar()
    url_login='http://192.168.1.22:8080/lavazza_doc/adminUserAction.do'
    body=(('logintype','login'),('u','admin'),
    ('psw','22222222'))
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    #opener.addheaders=[('User-agent','Opera/9.23')]
    opener.addheaders=[('User-agent',
    'Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)')]
    urllib2.install_opener(opener)
    req=urllib2.Request(url_login,urllib.urlencode(body))
    u=urllib2.urlopen(req)
    print u.read().decode('utf-8').encode('gbk')
    
    u = urllib2.urlopen("http://192.168.1.22:8080/lavazza_doc/upload/000/000/000000030")
    s= u.read()
    file = open(r'd:\doc3.pdf', 'wb')
    file.write(s)
    
def post4():
    #formail.sina.com.cn
    
    cj=cookielib.CookieJar()
    url_login='http://192.168.1.22:8080/lavazza_doc/adminUserAction.do'
    body=(('logintype','login'),('u','admin'),
    ('psw','22222222'))
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    #opener.addheaders=[('User-agent','Opera/9.23')]
    opener.addheaders=[('User-agent',
    'Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)')]
    urllib2.install_opener(opener)
    req=urllib2.Request(url_login,urllib.urlencode(body))
    u=urllib2.urlopen(req)
    print u.read().decode('utf-8').encode('gbk')
    
    file = open(r'd:\doc3.pdf', 'rb')
    s = file.read()
    u = urllib2.urlopen("http://192.168.1.22:8080/lavazza_doc/fileinfo.api?med=upload&uploadFile=%s"%'abc')
    print u
    #file.write(s)
    
    
    
if __name__ == '__main__':
    #post3()
    post4()
    