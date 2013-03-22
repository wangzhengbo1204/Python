'''
Created on 2013-3-22

@author: GFTOwenWang
'''
from scrapy.cmdline import execute
from scrapy.settings import CrawlerSettings

if __name__ == '__main__':
    execute(argv=["scrapy", "crawl", "baidu" ], settings=CrawlerSettings(__import__('scrapytutorail.settings', {}, {}, [''])))


