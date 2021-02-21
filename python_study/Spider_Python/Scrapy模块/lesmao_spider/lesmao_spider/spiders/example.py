import scrapy

from lesmao_spider.items import LesmaoSpiderItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.lesmao.org']
    start_urls = ['https://lesmao.org/plugin.php?id=group&page={}'.format(str(i)) for i in range(1, 21)]

    # def parse(self, response):
    #     # 该方法实现使用命令存储
    #     divs = response.xpath('//div[@class="group"]')
    #     data_lst = []
    #     for div in divs:
    #         title = div.xpath('./div[1]/a/img/@alt').extract_first()
    #         href = div.xpath('./div[1]/a/@href').extract_first()
    #
    #         dic = {
    #             'title': title,
    #             'href': 'https://lesmao.org/'+href
    #         }
    #
    #         data_lst.append(dic)
    #         #
    #         # item = LesmaoSpiderItem()
    #         # item['title'] = title
    #         # item['href'] = href
    #         #
    #         # yield item
    #
    #     return data_lst

    def parse(self, response):
        # 该方法实现使用命令存储
        divs = response.xpath('//div[@class="group"]')
        data_lst = []
        for div in divs:
            title = div.xpath('./div[1]/a/img/@alt').extract_first()
            href = div.xpath('./div[1]/a/@href').extract_first()

            item = LesmaoSpiderItem()
            item['title'] = title
            item['href'] = href

            yield item
