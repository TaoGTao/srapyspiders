# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaseItem(scrapy.Item):
    发布网站 = scrapy.Field()
    发布时间 = scrapy.Field()
    下载时间 = scrapy.Field()
    URL = scrapy.Field
    more = scrapy.Field()

class JobItem(BaseItem):
    pass
