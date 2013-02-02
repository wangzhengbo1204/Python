#-*- coding:utf-8 -*-
'''
Created on 2011-11-11

@author: GFTOwenWang
'''
import uuid


def test_func1():
    print uuid.uuid3(uuid.NAMESPACE_URL,'http://www.lianheratings.com.cn/UploadFiles/B0395-GSZQ0172-GZ2010－1.pdf')
    print uuid.uuid5(uuid.NAMESPACE_URL,'ft:\\192.1\\test\\b.txt')
        
    print len('4b1a67d5-0c0f-11e1-ae55-f04da239d837')
    
    
def test_func2():
    u1= uuid.UUID('4b1a67d5-0c0f-11e1-ae55-f04da239d837')
    a = u1.int
    print type(a)
    print len(unicode(a))
    print a
    
if __name__ == '__main__':
    test_func1()