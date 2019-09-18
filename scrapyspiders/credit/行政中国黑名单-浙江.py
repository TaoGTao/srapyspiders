from scrapyspiders.basespiders.xgspider import XgSpider
from scrapyspiders.tools import *


class MySpider(XgSpider):
    name = "信用中国黑名单-浙江"
    dbName = "信用中国黑名单"
    collName = "浙江"
    url = 'http://credit.zj.gov.cn/js/black.js'
    url1 = 'http://credit.zj.gov.cn/hmd/dishonestyProxy.do?startrecord=1&endrecord=10&perpage={}&totalRecord={}'  # 翻页
    url2 = 'http://credit.zj.gov.cn/hmd/dishonestyDetailxx.do?zjid={}&deptnames={}&titleAll={}&tableId={}'  # 详情页
    url3 = 'http://credit.zj.gov.cn/hmd/dishonestyDetailx.do?titleAll={}&deptnames={}&tableId={}'  # 列表页首次请求的url

    def parse(self, response):
        response = response.replace(encoding='gbk')
        lines = re.findall('black\$(.+?)\$(.+?)\$\d{4}-\d{2}-\d{2}\$(\w+?)"', response.text)
        for line in lines:  # (deptnames, titleAll, tabId)
            print(self.url3.format(*line))
            yield Request(self.url3.format(*line), self.parse1, meta={'line': line})

    def parse1(self, response):  # 获取部分板块需要列表页表头信息
        r = json.loads(response.text)
        tab_titles = re.findall('>([^<]+?)<', r['retBuffer'])
        yield FormRequest(self.url1.format(r['perPage'], r['totalNums']), self.parse2,
                          formdata={'tabId': response.meta['line'][-1]},
                          meta={'line': response.meta['line'], 'tab_titles': tab_titles})

    def parse2(self, response):
        dis = re.findall('"(.*?)"', response.text)
        new = 0
        for di in dis:
            infos = di.split('$')[1:]
            info = dict(zip(response.meta['tab_titles'], infos[1:]))
            url = self.url2.format(infos[0], *response.meta['line'])
            show_url = url.replace('dishonestyDetailxx', 'dishonestyDetail')
            yield self.down_detail(url=show_url, **info)
            new += 1
        if new:
            yield response.request.replace(url=get_next_page(response.url, "record=%d", mod=10))
#
#
# if __name__ == '__main__':
#     MySpider.run_download(fast=__file__)
