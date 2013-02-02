'''
Created on 2011-8-10

@author: GFTOwenWang
'''

def test_param(name=None):
    print name
    
def main():
    a='name'
    test_param(a='test name')
    
main()