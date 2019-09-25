from scrapyspiders.basespiders.xgspider import XgSpider
from scrapyspiders.tools import *


class MySpider(XgSpider):
    name = "51job"
    dbName = "招聘网站"
    collName = "51job"
    url = "https://m.51job.com/search/joblist.php?jobarea=020000&keyword=爬虫&pageno=1"

    def parse(self, response):
        q = response.css
        items = q(".items a").xpath("@href").extract()
        new = 0
        for url in items:
            if self.coll.count({'url': url}):
                continue
            yield Request(url, self.parse_item)
            new += 1
        if new:
            next_page = re.sub('(pageno=)(\d+)', lambda i: i.group(1) + str(int(i.group(2)) + 1), response.url)
            yield response.request.replace(url=next_page)

    def parse_item(self, response):
        item = {}
        q = response.css
        item['地点'] = q('.jt em::text').extract_first() or '' + ' ' + q('.rec span::text').extract_first() or ''
        item['薪水'] = q('.jp::text').extract_first()
        item['pubdate'] = q('.jt span::text').extract_first()
        item['详情'] = q('.ain article').xpath('string(.)').extract_first()
        item['公司名称'] = q('.rec .c_444::text').extract_first()
        item['职位'] = q('.jt p::text').extract_first()
        item['工作年限'] = q('.jd .s_n::text').extract_first() or "不限"
        item['学历'] = q('.jd .s_x::text').extract_first() or "不限"
        item['url'] = response.request.url
        yield self.down_detail(**item)
