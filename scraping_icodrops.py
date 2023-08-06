import scrapy


class ICOSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://icodrops.com/category/upcoming-ico/']


    def parse(self, response):
        for item in response.xpath('//div[@class="ico-main-info"]'):
            link = item.xpath('./h3/a/@href')
            yield from response.follow_all(link, self.icodrops_info)


    def icodrops_info(self, response):

            yield {
                'name_ico': response.xpath('.//div[@class="ico-main-info"]/h3/a/text()').get(),
                'link_ico': response.xpath('.//div[@class="ico-main-info"]/h3/a/@href').get(),
                'category': response.xpath('.//div[@class="ico-main-info"]/span[@class="ico-category-name"]/text()').get(),
                'full_pul': response.xpath('.//div[@class="ico-main-info"]/div[@class="goal-in-card"]/text()').get(),
                'collected': response.xpath('.//div[@class="ico-main-info"]/div[@class="goal-in-card"]/span[@class="green"]/text()').get(),
                'token_sale': response.xpath('.//div[@class="white-desk ico-desk"]//div[@class="col-12 title-h4"]//h4/text()').get(),
                'ather_info': response.xpath('.//div[@class="white-desk ico-desk"]//div[@class="col-12 col-md-6"]/li/text()').getall(),
                 }


a = ICOSpider

print(a)