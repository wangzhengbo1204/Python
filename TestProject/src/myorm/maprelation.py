#-*- coding:utf-8 -*-
'''
Created on 2012-11-25 @author: GFTOwenWang
'''
from conn import createengine, create_session
from sqlalchemy import Column, Integer, String, Table, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship



Base = declarative_base()

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name=Column(String(50))
    children = relationship("Child", backref='parent')

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name=Column(String(50))
    parent_id = Column(Integer, ForeignKey('parent.id'))


engine = createengine()
Base.metadata.create_all(engine)

def func1():
    p1=Parent(name='p1')
    c1=Child(name='c1')
    p1.children.append(c1)
    
    session = create_session()
    session.add(p1)
    session.commit()
    
def func2():
    session = create_session()
    p1 =session.query(Parent).filter_by(id=1)[0]
    print type(p1)
    c1 = session.query(Child).filter_by(id=1)[0]
    print type(c1)
    p1.children.remove(c1)
    session.commit()
    
    
if __name__=='__main__':
    #func1()
    func2()
    


