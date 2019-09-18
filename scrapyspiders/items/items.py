# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaseItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    pubdate = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    more = scrapy.Field()

class creditItem(BaseItem):
    # 发布网站 = scrapy.Field()
    # 发布时间 = scrapy.Field()
    # 下载时间 = scrapy.Field()
    # name = scrapy.Field()
    pass
