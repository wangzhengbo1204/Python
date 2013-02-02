#-*- coding:utf-8 -*-
'''
Created on 2011-8-11

@author: GFTOwenWang
'''
import pymssql


SQLSERVER='192.168.1.135'
USER='sa'
PASSWORD='123456'
DATABASE='PG'

connection_string = 'DRIVER={SQL Server};SERVER=192.168.1.135;DATABASE=PG;UID=sa;PWD=123456'
conn = pymssql.connect(host=SQLSERVER,user=USER,password=PASSWORD,database=DATABASE)
#conn = pymssql.connect(connection_string) 

cursor = conn.cursor()   

def func1():
    #sql = 'select PRI_BIZ from BND_COM_PROFILE where COMCODE =200000044'
    sql = """select ComCode ,
            DeclareDate ,
            SEQ,
            P_SEQ ,
            DIST_CLS_CODE ,
            ALLOT_MTD ,
            ALLOT_INFO ,
            BASE_DATE ,
            BASE_VOL ,
            ALLOT_PCT ,
            PRC_INFO ,
            ALLOT_PRC ,
            FOR_PRC ,
            CURNCY ,
            ALLOT_VOL ,
            LTD_VOL ,
            UNLTD_VOL ,
            BH_VOL ,
            A_APL_CODE ,
            A_APL_NAME ,
            B_APL_CODE ,
            B_APL_NAME ,
            A_REG_DATE ,
            A_EXRGT_DATE ,
            B_REG_DATE ,
            B_LAST_TD ,
            B_EXRGT_DATE ,
            STR_BUY_DATE ,
            END_BUY_DATE ,
            CAP ,
            FEE ,
            NET_CAP 
      from STK_ALLOT_INTRO
                        where MTIME > '2009-10-13 11:54:55' AND MTIME <= '2009-12-31'"""
    sql = sql.decode('utf-8').encode('gbk')
    ret = cursor.execute(sql)   
    #import pdb
    #pdb.set_trace()
    rows = cursor.fetchall()
    print len(rows)
    for r in rows:
        for i in r:
            if isinstance(i,basestring):
                print i.decode('gbk')
            else:
                print i
    #print len(rows)  
    #s = rows[0][0]
    #s1= s.decode('gbk')
    #print s1

def func2():
    strsql = "select DISC_ID,TITLE,DECLAREDATE from dbo.DISC_MAIN_COM"
    cursor.execute(strsql)
    rs = cursor.fetchall()
    for r in rs:
        strsql = "select DISC_ID,TITLE,DECLAREDATE from dbo.DISC_MAIN_COM where DISC_ID = '%s'" % r[0]
        print r[0]
        cursor.execute(strsql)
        cursor.fetchall()
        
if __name__ == '__main__':
    func2()
    
    
        
        
    
