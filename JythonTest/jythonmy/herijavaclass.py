#-*- coding:utf-8 -*-
'''
Created on 2013-3-5

@author: GFTOwenWang
'''
import Point  
  
class Circle(Point):  
    def __init__(self, x, y, r):  
        super(Circle, self).__init__(x, y)  
        self.r = r;  
  
    def dump(self):  
        super(Circle, self).dump()  
        print "This radius of Circle is %s" % self.r  
  
    def area(self):  
        return self.r**2*3.1415  
  
if __name__ == "__main__":  
    p = Point(2,3)  
    p.dump()  
    c = Circle(2,10,3) # 但是实际上这里有问题，我不知道怎么回事，还在研究中……哪位指点下  
    c.dump()  