'''
Created on 2012-10-10

@author: GFTOwenWang
'''
from pygrametl.datasources import CSVSource


downloadlog = CSVSource(file('./a.csv', 'r', 16384),
                        delimiter='\t')

print downloadlog