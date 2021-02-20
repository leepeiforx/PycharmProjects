
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SpidersSpider(CrawlSpider):
    name = 'spiders'
    allowed_domains = ['s1.v5uh.xyz']
    start_urls = ['https://s1.v5uh.xyz/2048/thread.php?fid-103.html']
    link = LinkExtractor(allow=r'fid-103-page-\d+\.html')
    linke_detail = LinkExtractor(allow='')

    rules = (
        Rule(link, callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        tr_lsts = response.xpath('//*[@id="ajaxtable"]//tr')
        for tr in tr_lsts:
            title = tr.xpath('./td[2]/a/text()').extract_first()
            n_date = tr.xpath('./td[2]/text()').extract_first()
            title = (n_date, title)
            if (n_date, title) is not None:
                title = (n_date, title)
            print(title)