import scrapy


class ListSpider(scrapy.Spider):
    name = 'list'
    allowed_domains = ['lalafo.az']
    start_urls = ['http://lalafo.az/']

    def parse(self, response):

        response.selector.remove_namespaces()

        #Extract article information
        titles = response.xpath('//div[@class="adTile-title__wrap"]/span/text()').extract()
        prices = response.xpath('//p[@class = "adTile-price"]/span/text()').extract()
        links = response.xpath('//a[@class = "adTile-mainInfo"]/@href').extract()

        for item in zip(titles,prices, links):
            scraped_info = {
                'title' : item[0],
		'prices' : item[1],
		'link' : 'lalafo.az' + item[2]
            }

            yield scraped_info

