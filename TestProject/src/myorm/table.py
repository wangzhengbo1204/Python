#-*- coding:utf-8 -*-
'''
Created on 2012-11-22 @author: GFTOwenWang
'''
from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



engine = create_engine("mysql://datatec:0.618@192.168.1.42:3307/test", echo=True)
Base = declarative_base()



class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(50))
    
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password
    
    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)
    
def test_user1(): 
    #print User.__table__
    #print User.__mapper__
    Base.metadata.create_all(engine)
    ed_user = User('ed','Ed Jodes', 'edspassword')
    print ed_user.name
    print ed_user.fullname
    
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    session.add(ed_user)
    
    our_user = session.query(User).filter_by(name='ed').first() 
    print our_user
    print our_user is ed_user
    
    session.add_all([User('wendy', 'Wendy Williams', 'foobar'),User('mary', 'Mary Contrary', 'xxg527'),
                     User('fred', 'Fred Flinstone', 'blah')])
    
    ed_user.password ='123'
    print session.dirty
    
    print session.new
    
#    session.commit()
    
    
    

if __name__ == "__main__":
    test_user1()
    
    

