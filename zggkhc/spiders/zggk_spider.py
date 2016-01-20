#!/usr/bin/env python
# encoding: utf-8

import scrapy
from zggkhc.items import *
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class zggkSpider(scrapy.Spider):
    name = "zggk"
    allowed_domains = ["http://www.zggkhc.com"]

    def start_requests(self):
        for i in xrange(100):
            yield self.make_requests_from_url("http://www.zggkhc.com/hngzzb.aspx?page=%d" % i)

    def parse(self,response):
        items = []
        sel = Selector(response)
        star_sel = sel.xpath('//table[@width="1080"]')

        for site in star_sel:
            item = ZggkhcItem()

            serNum = star_sel.xpath('tr/td[1]/text()').extract()
            cateGory = star_sel.xpath('tr/td[2]/text()').extract()
            groupDir = star_sel.xpath('tr/td[3]/text()').extract()
            prducNam = star_sel.xpath('tr/td[4]/text()').extract()
            unit = star_sel.xpath('tr/td[5]/text()').extract()
            addres = star_sel.xpath('tr/td[6]/text()').extract()
            meterial = star_sel.xpath('tr/td[7]/text()').extract()
            speciFication = star_sel.xpath('tr/td[8]/span/text()').extract()
            model = star_sel.xpath('tr/td[9]/span/text()').extract()
            producEnter = star_sel.xpath('tr/td[10]/text()').extract()
            winPrud  = star_sel.xpath('tr/td[11]/text()').extract()
            price = star_sel.xpath('tr/td[12]/text()').extract()


            item['serNum'] = [s.encode('utf-8') for s in serNum]
            item['cateGory'] = [c.encode('utf-8') for c in cateGory ]
            item['groupDir'] = [g.encode('utf-8') for g in groupDir]
            item['prducNam'] = [p.encode('utf-8') for p in prducNam]
            item['unit'] = [u.encode('utf-8') for u in unit]
            item['addres'] = [a.encode('utf-8') for a in addres]
            item['meterial'] = [m.encode('utf-8') for m in meterial]
            item['speciFication'] = [s.encode('utf-8') for s in speciFication]
            item['model'] = [m.encode('utf-8') for m in model]
            item['producEnter'] = [p.encode('utf-8') for p in producEnter]
            item['winPrud'] = [w.encode('utf-8') for w in winPrud ]
            item['price'] = [p.encode('utf-8') for p in price]
            items.append(item)

        return items
