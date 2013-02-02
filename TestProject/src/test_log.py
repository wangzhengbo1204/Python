'''
Created on 2011-7-8

@author: GFTOwenWang
'''
import StringIO
import sys, traceback
from gftdata.share.utility.log import Log

def test_func1():
    '''
    test_func1 name
    '''
    Log.debug('it is debug')
    Log.info('it is info')
    
    Log.warn('it is warn')
    
    Log.error('it is error')
    
    Log.debug('it is debug')
    Log.info('it is info')
    
    Log.warn('it is warn')
    
    Log.error('it is error')
    
    Log.live("it is live")
    
def test_func2():
    a=0
    try:
        b=1/a
    except Exception as ex:
        raise ex
    
    return b

def test_func3():
    b = 0
    try:
        b= test_func2()
    except Exception as ex:
        Log.error("test_func2 error", None, ex)
        print '='*20
        s = StringIO.StringIO()
        traceback.print_exc(file = s)
        print s.getvalue()
        print '='*20
        raise

    print b
    
def test_func4():
    try:
        test_func3()
    except Exception as ex:
        print '-'*20
        s = StringIO.StringIO()
        traceback.print_exc(file = s)
        print s.getvalue()
        print '-'*20
        
def test_trace():
    s = StringIO.StringIO()
    traceback.print_exc(file = s)
    return s.getvalue()
    
def test_func5():
    b = 0
    try:
        b= test_func2()
    except Exception as ex:
        Log.error("test_func2 error", None, ex)
        print '='*20
        s = test_trace()
        print s
        print '='*20
        raise

    print b
    
def test_func6():
    try:
        test_func5()
    except Exception as ex:
        print '-'*20
        s = test_trace()
        print s
        print '-'*20
        
def test_func7():
    while True:
        Log.info('it is info')
    
if __name__ == "__main__":
    test_func7()
    
    