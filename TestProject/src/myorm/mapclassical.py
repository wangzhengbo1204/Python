#-*- coding:utf-8 -*-
'''
Created on 2012-11-25 @author: GFTOwenWang
'''
from sqlalchemy import Column, Integer, String, Table, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship

from conn import createengine, create_session


Base = declarative_base()


#metadata = MetaData()
#
#user = Table('user',metadata,
#             Column('id',Integer, primary_key=True),
#             Column('name', String(50)),
#             Column('fullname',String(50)),
#             Column('password',String(12))
#                    )
#
#class User(object):
#    
#    def __init__(self, name, fullname, password):
#        self.name = name
#        self.fullname = fullname
#        self.password = password
#        
#        
#address = Table('address', metadata,
#                Column('id',Integer,primary_key=True),
#                Column('user_id',Integer,ForeignKey('user.id')),
#                Column('email_address',String(50))
#                )
#
#class Address(object):
#    
#    def __init__(self, user_id, email_address):
#        self.user_id = user_id
#        self.email_address = email_address
#
#mapper(User, user, properties={'addresses':relationship(Address, backref='user',order_by=address.c.id)})
#
#mapper(Address, address)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(50))
    

class Address(Base):
    __tablename__='address'
    
    id=Column('id',Integer,primary_key=True)
    user_id = Column('user_id',Integer,ForeignKey('users.id'))
    email_address = Column('email_address',String(50))
    
    
engine = createengine()
Base.metadata.create_all(engine)

def func1():
    session = create_session()
    userobj =User(name='a',fullname='abc',password='123')
    session.add(userobj)
    session.commit()
    
    
if __name__ == "__main__":
    func1()
    
    
        
