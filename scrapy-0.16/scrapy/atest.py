# -*- coding:utf-8 -*-
'''
Created on 2013-3-1 
@author: corleone
'''
from scrapy.cmdline import execute
from scrapy.settings import CrawlerSettings
# CrawlerSettings: <CrawlerSettings module='scrapy.dmoz.settings'>
if __name__ == '__main__':
    
#    execute(argv=["scrapy","crawl","dmoz"], settings=CrawlerSettings(__import__('scrapy.dmoz.settings', {}, {}, [''])))
    
    execute(argv=["scrapy","crawl","statsgov"], settings=CrawlerSettings(__import__('scrapy.statsgov.settings', {}, {}, [''])))
#    execute(argv=["scrapy","shell","http://www.stats.gov.cn/tjbz/xzqhdm/t20130118_402867249.htm" ], settings=CrawlerSettings(__import__('scrapy.statsgov.settings', {}, {}, [''])))
    
#    execute(argv=["scrapy", "crawl", "dmoz"], settings=None)
    
