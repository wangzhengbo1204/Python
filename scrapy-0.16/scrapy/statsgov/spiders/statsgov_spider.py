# -*- coding:utf8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.statsgov.items import StatsGovItem

class StatsgovSpider(BaseSpider):
    name = "statsgov"
    allowed_domains = ["statsgov.org"]
    start_urls = [
        "http://www.stats.gov.cn/tjbz/xzqhdm/t20130118_402867249.htm",
    ]
#//span[@class="content"]/table/tbody/tr[1]/td[1]/p/span
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        trs = hxs.select('//span[@class="content"]/table/tbody/tr')
        items = []
        
        for tr in trs:
            i = StatsGovItem()
            code = tr.select("td[1]/p/span/text()").extract()[0]
            label = tr.select("td[2]/p/span/text()").extract()[0]
            i[u"code"] = code
            i[u"label"] = label
            
            print label, i[u'label']
            
            items.append(i)
            
        return items



