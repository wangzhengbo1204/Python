#-*- coding:utf-8 -*-
'''
Created on 2012-11-21 @author: GFTOwenWang
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def func1():
    #``dialect+driver://user:password@host/dbname[?key=value..]``
    #engine = create_engine("mysql://datatec:0.618@192.168.1.42:3307/Data_Fundamental_Master", echo=True)
    engine = create_engine("mysql://root:test@localhost/test", echo=True)
    print engine.execute("select * from test.t_stock limit 1").scalar()
    
def createengine():
    #engine = create_engine("mysql://datatec:0.618@192.168.1.42:3307/Data_Fundamental_Master", echo=True)
    engine = create_engine("mysql://root:test@localhost/test", echo=True)
    
    return engine
    
def create_session():
    engine = createengine()
    
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    
    return session
    
    
if __name__ == "__main__":
    func1()