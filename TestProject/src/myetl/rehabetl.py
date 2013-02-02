#-*- coding:utf-8 -*-
'''
Created on 2012-10-11

@author: GFTOwenWang
'''
import MySQLdb
import pygrametl

from datetime import datetime, date

from pygrametl.datasources import CSVSource,MergeJoiningSource
from pygrametl.tables import CachedDimension

def get_stocklist():
    dict_stock={}
    f = open("zaipai.txt","r")
    lines = f.readlines()
    for line in lines[1:]:
        list_field = line.strip().split("\t")
        stockcode = list_field[0][:-3]
        marketcode = list_field[0][-3:]
        if marketcode==".SZ":
            marketcode=102
        elif marketcode==".SH":
            marketcode=103
            
        delistdate = datetime.strptime(list_field[2],"%Y-%m-%d")
        dict_stock[stockcode] = [marketcode, delistdate]
        
    return dict_stock


def func1():
    pgconn = MySQLdb.Connect(host="192.168.1.42",port=3307, user="datatec",passwd="0.618", db="Data_Fundamental_Master_Genius",charset="utf8")
    connection = pygrametl.ConnectionWrapper(pgconn)
    connection.setasdefault()

    rehabdata = CSVSource(file(ur"d:\temp\ReHis000001.csv",'r',10000),delimiter=',')

    rehabdim=CachedDimension(name="SFM_StockAdjPrices",
                              key="RecordID",
                              attributes=("MarketCode",'StockListID',"TradeDate","PreClosePrice","OpenPrice","ClosePrice","HighPrice","LowPrice","PriceAdjType"),
                              lookupatts=("MarketCode",'StockListID',"TradeDate","PriceAdjType"))
    
    title_mapping={"StockListID":"stockcode",
                   "TradeDate":"tradedate",
                   "PreClosePrice":"preClosePrice",
                   "OpenPrice":"OpenClosePrice",
                   "ClosePrice":"ClosePrice"}
    
    for row in rehabdata:
        row['MarketCode'] = 102
        row['PriceAdjType'] = 1
        rehabdim.ensure(row, title_mapping)
        
    connection.commit()
        

if __name__ == "__main__":
    func1()
    
    