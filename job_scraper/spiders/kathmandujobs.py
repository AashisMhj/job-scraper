import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from slugify import slugify



class KathmanduJobsSpider(scrapy.Spider):
    name = 'kathmandujobs'
    allowed_domains = ['kathmandujobs.com']
    start_urls = ['https://kathmandujobs.com/jobs']

    def parse(self, response):
        posts = response.css('div.job-listing-btns a')
        yield from response.follow_all(posts, self.parseDetail)

    def parseDetail(self, response):
        # addresses = response.css('p.address + *::text').getall()
        # addresses = [s for s in addresses if not any(c in s for c in['\n'])]
        # addresses[1].css('*:not(:contains("\\n")):not(:matches("^[\\s\\n]*$")):not(:matches("^.*[\\s\\n]{2,}.*$"):not(strong)::text').getall()
        addresses = response.css('p.address')
        addresses_length = len(addresses)


        def getAddressValue(index):
            values = addresses[index].css('*:not(:contains("\\n")):not(strong)::text').getall() if index < addresses_length else []
            return values[1] if len(values) > 1 else ''

        # TODO use some logic to extract exact details from addresses instead of using index
        yield {
            'name': response.css('div.titles h6::text').get(),
            'location': getAddressValue(6),
            'url': 'url',
            'image': response.css('img::attr(src)').get(),
            'job-title': response.css('div.titles h4::text').get(),
            'position': '',
            'level': getAddressValue(1),
            'experience': getAddressValue(0),
            'total-position': getAddressValue(2),
            'job-type': getAddressValue(3),
            'salary': getAddressValue(4),
            'education': getAddressValue(5),
            'type': '',
            'deadline':getAddressValue(7),
            'description': "".join(response.css('div.description *').getall()),
            'url': response.url,
            'slug': slugify(response.css('div.titles h4::text').get())
        }

            


