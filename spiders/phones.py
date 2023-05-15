import scrapy

from ..items import PhonehousebdItem
def cfDecodeEmail(encodedString):                       
    r = int(encodedString[:2],16)
    email = ''.join([chr(int(encodedString[i:i+2], 16) ^ r) for i in range(2, len(encodedString), 2)])
    return email

class PhonesSpider(scrapy.Spider):
    name = 'phones'
    allowed_domains = ['gsmarena.com.bd']
    start_urls = ['https://www.gsmarena.com.bd/brands/']

    def parse(self, response):
        brands = response.css('.text-center a::attr(href)').extract()
        # print('******** =',brands)
        # total_brands = len(brands)
        # print(total_brands)
        yield from response.follow_all(brands, self.phones)
    
    def phones(self, response):
        phones = response.css('.mobile_price+ a::attr(href)').extract()
        # print('******', phones)
        yield from response.follow_all(phones, self.details)
    
    def details(self,response):
        # mobile_details = {}
        item = PhonehousebdItem()
        for table in response.css('.table_specs'):
            for t in table.css('tr'):
                keys = t.css('.specs_name ::text').extract_first()
                values = t.css('.specs_name2 ::text').extract_first()
               
                

                if t.css('.__cf_email__'):                    
                    x = t.css('td ::attr(data-cfemail)').extract()
                    values = [cfDecodeEmail(y) for y in x]
                # mobile_details[keys] = values
                item[keys] = values
        yield item




