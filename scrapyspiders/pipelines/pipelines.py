# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

from scrapyspiders.tools import *


class MysqlPipeline(object):

    def __init__(self):
        self.db = get_mysql_client()

    def close(self):
        self.db.close()

    def process_item(self, item, spider):
        table_name = spider.name.split('-')[0]
        ceate_tb_sql = """CREATE TABLE IF NOT EXISTS %s(id INT NOT NULL AUTO_INCREMENT,
      url TEXT, name VARCHAR(45),title VARCHAR(45), 
      pubdate DATETIME,text LONGTEXT,more JSON,PRIMARY KEY (id))""" % table_name
        insert_tb_sql = """INSERT INTO %s (url, name, title, text, pubdate, more) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')""" \
                        % (table_name, item['url'], item['name'], item['title'], item['text'], item['pubdate'],
                           json.dumps(item['more'], ensure_ascii=False))
        with self.db.cursor() as cursor:
            cursor.execute(ceate_tb_sql)
            cursor.execute(insert_tb_sql.replace("'None'", 'null'))
            self.db.commit()

        return item


class MonGoPipeline:
    def process_item(self, item, spider):
        outputs = item.pop('more')
        all_item = dict(item, **outputs)
        spider.coll.insert(all_item)
        return all_item
