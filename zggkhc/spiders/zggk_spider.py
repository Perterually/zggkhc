#!/usr/bin/env python
# encoding: utf-8

import scrapy
from zggkhc.items import ZggkhcItem
class zggkSpider(scrapy.Spider):
    name = "zggk"
    allowed_domains = ["http://www.zggkhc.com"]
    start_urls = [
        "http://www.zggkhc.com/hngzzb.aspx?page=4"
    ]
    def parse(self,response):
        item = []
        item = [n.encode('utf-8') for n in response.xpath('//tr[@onmouseout="this.style.backgroundColor=c"]/td/text()').extract()]
        for ite in item:
            print(ite)
