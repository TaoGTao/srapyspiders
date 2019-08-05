import os

from srapyspiders.basespiders.xgspider import XgSpider


class MySpider(XgSpider):
    name = 'baidu'
    url = 'http://www.sxcredit.gov.cn/queryPage/xzcf.jspx'

    def parse(self, response):
        print(response.text)





if __name__ == '__main__':
    os.system('scrapy crawl baidu')
