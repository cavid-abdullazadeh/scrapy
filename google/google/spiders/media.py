import scrapy


class MediaSpider(scrapy.Spider):
    name = 'media'
    allowed_domains = ['google.com/search?q=gilan+holding', 'google.com/search?q=socar' , 'google.com/search?q=carçıoğlu+group' ]
    start_urls = ['http://google.com/search?q=gilan+holding',
		  'http://google.com/search?q=socar',
		 'http://google.com/search?q=carçıoğlu+group']

    def parse(self, response):

        response.selector.remove_namespaces()

        #Extract article information
        titles = response.xpath('//div[@class="BNeawe vvjwJb AP7Wnd"]/text()').extract()
        headers = response.xpath('//div[@class = "BNeawe s3v9rd AP7Wnd"]/text()').extract()
        links = response.xpath('//div[@class = "kCrYT"]/a/@href').extract()

        for item in zip(titles,headers, links):
            scraped_info = {
                'title' : item[0],
		'header' : item[1],
		'link' : item[2]
            }

            yield scraped_info
