# -*- coding:utf-8 -*-
'''
Created on 2012-3-2

@author: GFTOwenWang
'''
import json


class A(object):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
def func_dump():
    jd = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    print type(jd)
    print jd
    print jd[0]
    
    jd2 = json.dumps({"c":3,"b":2,"a":1}, sort_keys = True)
    print type(jd2)
    print jd2
    print jd2[0]
    
    jd3 = json.dumps([1,2,3,{'4': 5, '6': 7}], separators=(';',':'))
    print type(jd3)
    print jd3
    print jd3[0]
    
    jd4 = json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4)
    print type(jd4)
    print jd4
    print jd4["4"]
    
def func_dump2():
    from StringIO import StringIO
    io = StringIO()
    a=A("owen", '26')
    jd = json.dumps(a, io)
    print type(jd)
    print jd
    print jd[0]
    
def func_load():
    jd = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    print type(jd)
    print jd
    jd2 = json.loads(jd)
    print type(jd2)
    print jd2
    
    
if __name__ == "__main__":
    #func_dump2()
    func_load()
