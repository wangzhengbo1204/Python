#-*- coding:utf-8 -*-
'''
Created on 2011-11-30

@author: GFTOwenWang
'''
import chardet

def test_func():
    try:
        a= 1/0
    except ValueError:
        print 'catch'
    else:
        print 'else'
        

def test_func2():
    filepath = ur"D:\GFT\FileServer\RawFiles\Web\2012-02-06\迈博汇金研报.html"
    file = open(filepath, 'rb')
    s= file.read()
    a = chardet.detect(s)
    s2=s.decode('gbk', 'ignore')
    print s2
    
def func3():
    a= 5
    try:
        b=0
        c=a/b
    except Exception as ex:
        raise ex
    else:
        print "c:%s" % c
    finally:
        print "here is finally"
    
    
    
if __name__ == '__main__':
    #test_func()
    #test_func2()
    func3()