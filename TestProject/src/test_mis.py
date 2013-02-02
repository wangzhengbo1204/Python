# -*- coding:utf-8 -*-
'''
Created on 2011-8-18

@author: GFTOwenWang
'''
import os
import psyco
from datetime import datetime
from gftdata.share.utility.exc import exception2unicode

# 打印该文件的路径， 如：D:\My document\Eclipse4\TestProject\src\test_mis.py
print __file__
import pkg_resources
print 'ok'


def test_error_msg():
    try:
        raise ValueError(u'abc中国')
    except ValueError as ex:
        error_msg = exception2unicode(ex)
        print error_msg
        
def test_func1():
    filepath = ur'D:\GFT\DataTeam\MAC\Genius XML\4'
    list_filename= os.listdir(filepath)
    i = 171
    for filename in list_filename:
        basename = os.path.splitext(filename)[0]
        print i, ",", basename
        i+=1
        
def test_func2():
    filename = u'abc'
    for c in u'\\/:*?"<>→|':
        print c
        if filename.find(c)>-1:
            filename = filename.replace(c, ' ')
    
    print filename
    
def test_func3():
    list_file = os.listdir(r"D:\My document\Eclipse4\DataAutoGen\src\dataautogen\triggers\mac\MEI_IdtNumericValues")
    for f in list_file:
        if f.endswith('.py'):
            print f[:-3]
            
def test_func4():
    import time ;
     
    print 'here'
    #dtBegin =  time.time() ;
    dtBegin = datetime.now()
    d1 = 1.0 ;
    newNum = 1.0 ;
    curCount = 0 ;
    while newNum < 30000.0 :
        if curCount % 2 == 0 :
            d1 = d1 * newNum ;
        else :
            d1 = d1 / newNum ;
        newNum = newNum + 0.0015 ;
        curCount = curCount + 1 ;
     
    #dtEnd = time.time() ;
    dtEnd = datetime.now()
     
    print (dtEnd - dtBegin) ;
     
    #print("结果:%.8f 耗时%.3f" % ( d1 , dtEnd-dtBegin )) ; 
    print( newNum) ;
 
#psyco.bind(test_func4)

def test_func5():
    f = open(ur"d:\temp\windidt.txt","rb")
    dict_idts = {}
    for line in f:
        fields = line.split("\t")
        if fields[0]:
            if fields[0] not in dict_idts:
                dict_idts[fields[0]] = []
                dict_idts[fields[0]].append(fields[1])
            else:
                if fields[1] not in dict_idts[fields[0]]:
                    dict_idts[fields[0]].append(fields[1])
                    
    for key, value in dict_idts.items():
        if len(value)>1:
            print key, value

def test_func6():
    a=[]
    for i in a:
        if i>5:
            print i
        else:
            break
    else:
        print 'else do'
        
def func7():
    #a = os.listdir(r'd:\test')
    #a = os.listdir(r'\\192.168.1.40\datatec')
    a = os.listdir(r'//192.168.1.40/datatec')
    print [str(b) for b in a]
    
def func8():
    from test_log import test_func1
    print dir(test_func1)
    
def func9():
    #s = u"公司2002年度业绩预测完成情况 四季度市场形势继续向好"
    s=u'''1、已确认的一次性收益:      (1)本公司已出售所持有的"西北轴承(000595)144万股股票,增加2007年度收益约1546万元。      (2)本公司常意工模具厂土地资产被常州市土地收购储备中心收储获得5619万元补偿款,扣除帐面净值约2225万元及需交的税费后增加2007年度收益约2300万元。      (3)本公司已公告出售的所持有的"福田汽车(600166)1000万股股票作为交易性金融资产截止报告期末已出售550万股,增加2007年度收益8675万元。      2、未确认的一次性收益:本公司尚余450万股作为交易性金融资产的"福田汽车(600166)敼善保凑?福田汽车"2007年10月22日收盘价14.16元/股计算增加2007年度收益约5850万元。因二级市场股价存在波动,截止2007年12月31日“福田汽车(600166)”收盘价格与2007年10月22日收盘价格会有所变动,届时视具体收益金额确定是否进行业绩修正披露。'''
    
    #s1 = s.encode("gbk","ignore")
    s1 = s.encode("gbk")
    print s1.decode('gbk')

def func10():
    #s=u"以2000年6月30日总股本14705.88万股为基数,每10股配2股(以1999年6月30日总股本8100万股为基数,每10股配3股。  "
    s=u"以2000年6月30日总股本14705.88万股为基数,每10股配2股(以1999年6月30日总股本8100万股为基数,每10股配3股。  "
    s1 = s.encode("gbk")
    print s1
    
def func11():
    a=u'莫仲堃'
    print a
    
if __name__ == '__main__':
    #test_error_msg()
    #test_func6()
    func11()
    
    pass

    