'''
Created on 2012-3-26

@author: GFTOwenWang
'''
import threading
from DBUtils import PooledDB


class MSDBHelper(object):
    
    __lock = threading.Lock()
    __pool = None
    
    def __init__(self, SQLSERVER=None, USER=None, PASSWORD=None, DATABASE=None, CHARSET=None):
        pass
#        import pymssql
#        if SQLSERVER is None or USER is None or PASSWORD is None or DATABASE is None or CHARSET is None:
#            SQLSERVER='192.168.1.135'
#            USER='sa'
#            PASSWORD='123456'
#            DATABASE='PG'
#            CHARSET='GBK'
#        self.conn = pymssql.connect(host=SQLSERVER,user=USER,password=PASSWORD,database=DATABASE, charset=CHARSET)
    
    @staticmethod
    def getConn():
        MSDBHelper.__lock.acquire()
        if MSDBHelper.__pool is None:
            import pymssql
#            MSDBHelper.__pool = PooledDB.PooledDB(creator=pymssql, mincached=2 , maxcached=5 , 
#                              maxshared=5, maxconnections= 10, host="192.168.1.135" , port=1433 , 
#                              blocking=True, user="sa" , passwd="123456" , db="PG",
#                              use_unicode=True,charset="GBK") 
            MSDBHelper.__pool = PooledDB.PooledDB(creator=pymssql, mincached=2 , maxcached=5 , 
                              maxshared=5, maxconnections= 10, host="192.168.1.135:1433",
                              user="sa", password="123456", database="PG", charset="GBK") 
        MSDBHelper.__lock.release()
        conn = MSDBHelper.__pool.connection()
        return conn
    
    def select(self, sql):
        self.conn = MSDBHelper.getConn()
        cursor = self.conn.cursor()
        
        try:
            cursor.execute(sql)
            rs = cursor.fetchall()
        finally:
            cursor.close()
        
        return rs
    
class MSDBHelper2(object):
    
    def __init__(self, SQLSERVER=None, USER=None, PASSWORD=None, DATABASE=None, CHARSET=None):
        pass
#        import pymssql
#        if SQLSERVER is None or USER is None or PASSWORD is None or DATABASE is None or CHARSET is None:
#            SQLSERVER='192.168.1.135'
#            USER='sa'
#            PASSWORD='123456'
#            DATABASE='PG'
#            CHARSET='GBK'
#        self.conn = pymssql.connect(host=SQLSERVER,user=USER,password=PASSWORD,database=DATABASE, charset=CHARSET)
    
    @staticmethod
    def getConn():
        import pymssql
        SQLSERVER='192.168.1.135'
        USER='sa'
        PASSWORD='123456'
        DATABASE='PG'
        CHARSET='GBK'
        conn = pymssql.connect(host=SQLSERVER,user=USER,password=PASSWORD,database=DATABASE, charset=CHARSET)
        return conn
    
    def select(self, sql):
        self.conn = MSDBHelper2.getConn()
        cursor = self.conn.cursor()
        
        try:
            cursor.execute(sql)
            rs = cursor.fetchall()
        finally:
            cursor.close()
        
        return rs
    
class MSDBHelper3(object):
    
    def __init__(self, SQLSERVER=None, USER=None, PASSWORD=None, DATABASE=None, CHARSET=None):
        import pymssql
        if SQLSERVER is None or USER is None or PASSWORD is None or DATABASE is None or CHARSET is None:
            SQLSERVER='192.168.1.135'
            USER='sa'
            PASSWORD='123456'
            DATABASE='PG'
            CHARSET='GBK'
        self.conn = pymssql.connect(host=SQLSERVER,user=USER,password=PASSWORD,database=DATABASE, charset=CHARSET)
    
    def select(self, sql):
        cursor = self.conn.cursor()
        
        try:
            cursor.execute(sql)
            rs = cursor.fetchall()
        finally:
            cursor.close()
        
        return rs

def func1():
    strsql = "select top 10 * from dbo.BND_CRED_LINE "
    msdb = MSDBHelper()
    rs = msdb.select(strsql)
    for r in rs:
        print r
        


    
    
if __name__ == "__main__":
    func1()
    
    