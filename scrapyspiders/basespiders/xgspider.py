import subprocess

from scrapy import Spider, Request
from scrapy.shell import inspect_response
from scrapyspiders.tools.path import get_spider_path

class XgSpider(Spider):
    name = 'xgspider'

    def start_requests(self):
        if hasattr(self, 'get_start_request'):
            yield self.get_start_request
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


