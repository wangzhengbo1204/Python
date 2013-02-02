'''
Created on 2012-3-27

@author: GFTOwenWang
'''
from datetime import datetime, date


def func1():
    a = "03-21"
    d1 = datetime.strptime(a, "%m-%d")
    print d1
    print d1.year, d1.month, d1.day
    
    
def func2():
    w = date.weekday(datetime.now())
    print w
    w = date.weekday(datetime.strptime("2012-03-26", "%Y-%m-%d"))
    print w
    
def func3():
    t = datetime.strptime("21:00:00", "%H:%M:%S")
    print t
    print t.time()
    c = cmp(t.time(), datetime.now().time())
    print c
    
    t = datetime.strptime("07:00:00", "%H:%M:%S")
    c = cmp(t.time(), datetime.now().time())
    print c
    
def func4():
    d = datetime.now().date()
    t = datetime.now().time()
    d2 = datetime.strptime("%s %s:%s:%s" %(d, t.hour, t.minute, t.second), "%Y-%m-%d %H:%M:%S")
    print d2
    
func1()
func2()
func3()
func4()

