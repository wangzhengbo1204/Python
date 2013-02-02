#-*- coding:utf-8 -*-
'''
Created on 2011-8-14

@author: GFTOwenWang
'''
import urllib
import chardet
from urllib2 import HTTPError


def test_head():
    url = r'http://www.chinabond.com.cn/Info/11591991'
    request_header = urllib.urlopen(url)
    
    header_info = request_header.info()

    content_type_info = header_info.getheaders('Content-Type')
    content_type_info = unicode(content_type_info[0]).strip(' ')
    content_disposition = header_info.getheaders('Content-Disposition')
    #example:Content-Disposition: attachment;filename=?????????????��???1146.doc
    try:
        content_disposition_info = unicode(content_disposition[0], 'utf-8').split(';')
    except:
        encoding = chardet.detect(content_disposition[0])
        content_disposition_info = unicode(content_disposition[0], encoding['encoding']).split(';')
    if len(content_disposition_info) == 2:
        attachment = content_disposition_info[1].split('=')
        if attachment[0]== 'filename':
            filename = attachment[1]
            
    print filename
    
def test_open():
    import cookielib
    import urllib2
    try:
        url = u'http://www.safe.gov.cn/model_safe/tjsj/pic/'
        
        cookie = cookielib.CookieJar()
        httpcookie = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(httpcookie)
        opener.addheaders = [('User-agen', 'MSIE/6.0')]
        urllib2.install_opener(opener)
        file = opener.open(url, data=None, timeout=20)
        #file= urllib.urlopen(url)
        s= file.read()
        print s
    except HTTPError as ex:
        print ex
    

if __name__=="__main__":
    test_open()
    
