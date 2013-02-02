'''
Created on 2012-3-20

@author: GFTOwenWang
'''
class T(type):
    pass

if __name__ == '__main__':
    
    BBI = T('BondBasicInfo',(),{u'x':6})
    print BBI.x # 6
    
    bbi = BBI()
    print bbi.x # 6
    print BBI.x # 6
    bbi.x = 10
    print bbi.x # 10
    print BBI.x # 6