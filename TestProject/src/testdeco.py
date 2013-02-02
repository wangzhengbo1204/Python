'''
Created on 2011-12-28

@author: GFTOwenWang
'''

def deco1(msg):
    print 'decoretor1'
    
@deco1
def func1(a, b):
    pass


if __name__ == '__main__':
    func1(None, None)