
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.dmoz.items import DmozItem


class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
#        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

#    def parse(self, response):
#        print response.url
#        filename = response.url.split("/")[-2]
#        print filename
#        open(filename, 'wb').write(response.body)

#    def parse(self, response):
#        hxs = HtmlXPathSelector(response)
#        sites = hxs.select('//ul/li')
#        for site in sites:
#            title = site.select('a/text()').extract()
#            link = site.select('a/@href').extract()
#            desc = site.select('text()').extract()
#            print [t.strip() for t in title], [t.strip() for t in link], [t.strip() for t in desc]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.select('a/text()').extract()
            item['link'] = site.select('a/@href').extract()
            item['desc'] = site.select('text()').extract()
            items.append(item)
        return items