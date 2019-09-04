import os

from scrapyspiders.basespiders.xgspider import XgSpider


class MySpider(XgSpider):
    name = '行政处罚-陕西'
    url = 'http://www.sxcredit.gov.cn/queryPage/xzcf.jspx'

    def parse(self, response):
        print(response.text)





if __name__ == '__main__':
    MySpider.run_download(fast=__file__)
