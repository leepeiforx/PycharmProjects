import scrapy
import time
from scrapy.http.response.html import HtmlResponse


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['https://www.zhipin.com/c101110100/?query="数据分析"&ka=sel-city-101110100']

    def parse_detail(self, response):
        job_info = response.xpath('div[@class="text"]//text').extract()
        job_info = ''.join(job_info)
        print(job_info)

    def parse(self, response):
        detail_infos = []
        data_lst = []
        job_names = response.xpath('//span[@class="job-name"]/a/text()').extract()
        hrefs = response.xpath('//span[@class="job-name"]/a/@href').extract()
        for href in hrefs:
            detial_href = 'https://www.zhipin.com' + href

            time.sleep(5)
            #  对详情页页面发起请求
            yield scrapy.Request(detial_href, callback=self.parse_detail)
