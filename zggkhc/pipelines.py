# -*- coding: utf-8 -*-f
import json
import codecs
from openpyxl import Workbook
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZggkhcPipeline(object):
    def __init__(self):
        self.file = codecs.open('list.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False, encoding='utf8') + '\n'
        self.file.write(line)
        return item


