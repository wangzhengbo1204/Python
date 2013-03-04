# -*- coding:utf8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import TakeFirst, MapCompose, Compose
from scrapy.contrib.loader import ItemLoader

class StatsGovItem(Item):
    
    label = Field(
                  input_processor=Compose(lambda x:x.strip(u'市')),
                  output_processor=MapCompose(str.strip),
                  )
    code = Field()
#    label = Field()
    
    

    
