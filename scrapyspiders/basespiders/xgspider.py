import subprocess

from scrapy import Request, Spider
from scrapy_redis.spiders import RedisSpider
from scrapy.shell import inspect_response

from scrapyspiders.items.items import creditItem
from scrapyspiders.tools.database import *
from scrapyspiders.tools.path import get_spider_path

class XgSpider(Spider):
    name = 'xgspider'
    custom_settings = {'ITEM_PIPELINES': {'scrapyspiders.pipelines.pipelines.MonGoPipeline': 7,
                                          # 'scrapy_redis.pipelines.RedisPipeline': 700
                                          },
    #                    'DUPEFILTER_CLASS': "scrapy_redis.dupefilter.RFPDupeFilter",
    # 'SCHEDULER': "scrapy_redis.scheduler.Scheduler",
    # 'SCHEDULER_PERSIST': 'True',
    }

    # redis_key = 'xgspider:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        # domain = kwargs.pop('domain', '')
        # self.allowed_domains = filter(None, domain.split(','))
        super().__init__(*args, **kwargs)
        self.client = get_mongo_client()
        self.coll = self.get_coll()

    def start_requests(self):
        if hasattr(self, 'get_start_request'):
            yield from self.get_start_request()
            return
        if not hasattr(self, 'url'):
            raise ValueError('url不能为空')
        yield Request(self.url, self.parse)

    @classmethod
    def cmd_debug(self, response):
        """
        控制台窗口shell调试
        :param response:
        :return:
        """
        inspect_response(response, self)

    @classmethod
    def run_download(cls, suffix='', fast=''):
        if fast:
            suffix += ' -s SPIDER_MODULES=' + get_spider_path(fast)
        subprocess.call('scrapy crawl {0}'.format(cls.name) + suffix)

    def down_detail(self, **kwargs):
        item = creditItem()
        item['name'] = kwargs.pop('name', None)
        item['url'] = kwargs.pop('url', None)
        item['pubdate'] = kwargs.pop('pubdate', None)
        item['title'] = kwargs.pop('title', None)
        item['text'] = kwargs.pop('text', None)
        item['more'] = kwargs

        return item

    def get_coll(self):
        return self.client[self.dbName][self.collName]

    def close(self, reason):
        self.client.close()

