#-*- coding:utf-8-*-
'''
Created on 2013-3-22

@author: GFTOwenWang
'''
from scrapy.spider import BaseSpider


class BaiduSpider(BaseSpider):
    name = "baidu"
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com']
    
    def parse(self, response):
        filename = 'baidu_home'
        open(filename, 'wb').write(response.body)
        