'''
Created on 2012-4-9

@author: GFTOwenWang
'''

class Parrot(object):  
    def __init__(self):  
        self._voltage = 100000  
 
    @property  
    def voltage(self):  
        """Get the current voltage."""  
        return self._voltage  
 
    @voltage.setter  
    def voltage(self, new_value):  
        self._voltage = new_value  
  
if __name__ == "__main__":  
    # instance  
    p = Parrot()  
    # similarly invoke "getter" via @property  
    print p.voltage  
    # update, similarly invoke "setter"  
    p.voltage = 12
    
    print p.voltage