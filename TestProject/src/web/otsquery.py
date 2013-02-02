#-*- coding:utf-8 -*-
'''
Created on 2013-1-18 @author: GFTOwenWang
'''
import urllib
import urllib2
import cookielib
import os


def func5():
    
    
    cookie = cookielib.CookieJar()
    httpcookie = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(httpcookie, urllib2.HTTPHandler)
    
    url = "http://www.12306.cn/otsquery/query/queryRemanentTicketAction.do;jsessionid=0B54615B2527CF44DED68D3C3C99ED53?method=init"
    r = opener.open(url, data=None, timeout=20)
    
    postdata = (("orderRequest.from_station_name",u"上海"),
                ("orderRequest.to_station_name",u"杭州"),
                ("orderRequest.train_date","2013-1-4"),
                ("orderRequest.start_time_str","00:00--24:00"),
                ("orderRequest.trainCodeText",""),
                ("trainClassArr","QB,D,Z,T,K,QT"),
                ("trainPassType","QB,GL,SF"))
    #request = urllib2.Request(url, urllib.urlencode(postdata))
    pd = urllib.urlencode(postdata)
    
    opener.addheaders = [('User-agen', 'MSIE/6.0')]
        
    url = "http://www.12306.cn/otsquery/query/queryRemanentTicketAction.do?method=queryTrain"
    r = opener.open(url, data=pd, timeout=20)
    #r = opener.open(url)
    
    s = r.read()
    f=open(ur'd:\a.html',"wb")
    f.write(s)
    f.close()
    print s.decode('utf-8')
    
if __name__ == '__main__':
    func5()
    