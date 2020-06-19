# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class ComplaintSpider(scrapy.Spider):
    name = 'complaint'
    allowed_domains = ['12365auto.com']
    start_urls = ['http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-1.shtml']

    def parse(self, response):

        # 获取末页页码
        LastPg = int(response.xpath('/html/body/div[2]/div[4]/div[2]/div/a[11]/@href').get()[-11:-6])

        for page in range(1, LastPg):
            url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-{}.shtml'.format(page)
            yield Request(url, callback=self.parse_detail)

    def parse_detail(self, response):

        # 获取页面投诉条目数
        tr_list = response.xpath('//tr')

        for tr in tr_list[1:]:
            ID = tr.xpath('./td[1]/text()').get()
            Brand = tr.xpath('./td[2]/text()').get()
            Series = tr.xpath('./td[3]/text()').get()
            Model = tr.xpath('./td[4]/text()').get()
            Dscp = tr.xpath('./td[5]/a/text()').get()
            Problem = tr.xpath('./td[6]/text()').getall()
            Date = tr.xpath('./td[7]/text()').get()
            Status = tr.xpath('./td[8]/em/text()').get()

            item = {
                "投诉编号": ID,
                "投诉品牌": Brand,
                "投诉车系": Series,
                "投诉车型": Model,
                "问题简述": Dscp,
                "典型问题": Problem,
                "投诉时间": Date,
                "投诉状态": Status
            }
            yield item
