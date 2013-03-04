# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['scrapy.dmoz.spiders']
NEWSPIDER_MODULE = 'scrapy.dmoz.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
