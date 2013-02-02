#-*- coding:utf-8 -*-
'''
Created on 2012-11-30 @author: GFTOwenWang
'''


def func1():
    filename = ur"D:\Kettle\RepositoryTest\tutorial\list.csv"
    f = open(filename, "rb")
    lines = f.readlines()
    #for line in lines[::-1]:
    for line in lines:
        print line
        
    print "-"*20
    for line in lines[::-1]:
        print line
        
def func2():
    filename = ur"D:\Kettle\RepositoryTest\tutorial\list.csv"
    f = open(filename, "ab")
    line = "a,b\r\n"
    f.write(line)
    
    f.close()
    
    
    
        
        
if __name__ == "__main__":
    func1()