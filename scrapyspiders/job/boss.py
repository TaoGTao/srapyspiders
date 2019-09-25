from scrapyspiders.basespiders.xgspider import XgSpider
from scrapyspiders.tools import *


class MySpider(XgSpider):  # 网页版反爬算法待破解
    name = "招聘网站-boss直聘"
    dbName = "招聘网站"
    collName = "boss直聘"
    url = 'https://www.zhipin.com/mobile/jobs.json?city=101020100&query=爬虫&page=1'

    def parse(self, response):
        js = json.loads(response.text)
        html = Selector(text=js['html'])
        new, total = 0, 0
        for li in html.xpath('//li[@class="item"]'):
            url = response.urljoin(li.xpath('.//a/@href').get())
            position_name = li.xpath('.//h4/text()').get()  # 职位名称
            salary = li.xpath('.//span[@class="salary"]/text()').get()  # 薪资
            lines = li.xpath('.//div[@class="msg"]/em/text()').extract()
            xq = '-'.join(lines)
            if len(lines) == 3:
                place, work_year, educational = lines
            else:
                place, work_year, educational = None, None, None
            company = li.xpath('.//div[@class="name"]/text()').get()
            di = {'职位': position_name, '薪水': salary, '地点': place, '详情': xq,
                  '工作年限': work_year, '学历': educational, 'url': url, '公司名称': company}
            if self.coll.count({"url": url}):
                continue
            yield self.down_detail(**di)
            new += 1
        if new:
            next_page = re.sub('(page=)(\d+)', lambda i: i.group(1) + str(int(i.group(2)) + 1), response.url)
            yield response.request.replace(url=next_page)
