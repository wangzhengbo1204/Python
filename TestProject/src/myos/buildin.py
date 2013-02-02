'''
Created on 2012-11-3

@author: GFTOwenWang
'''

def func1():
    row={'NT_SpecialEnitiyBasicInfo':{'a':1},'NT_IndividualBasicInfo':{'b':2},'NT_CorpBasicInfo':{'c':3}}
    orgtype = 700
    if int(orgtype) > 700:
        destable = 'NT_SpecialEnitiyBasicInfo'
    elif int(orgtype) == 700:
        destable = 'NT_IndividualBasicInfo'
    else:
        destable = 'NT_CorpBasicInfo'
        
    newd = filter(lambda x:x==destable, row)
    
    print newd
    
    
if __name__ == '__main__':
    func1()
    
    