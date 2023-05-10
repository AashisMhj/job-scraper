import scrapy
from slugify import slugify


class JobsNepal(scrapy.Spider):
    name = 'jobsnepal'
    start_urls = ['https://www.jobsnepal.com/jobs']
    page_limit = 5
    count = 0

    def parse(self, response):
        print('parse link')
        print(response.url)
        posts = response.css('div.card div.card-body > a')
        yield from response.follow_all(posts, self.parseDetail)

        # if(self.count < self.page_limit):
        #     self.count = self.count + 1
        #     pagination_links = response.css('li.page-item a::attr(href)').getall()[-1]
        #     yield from response.follow(pagination_links, self.parse)


    def parseDetail(self, response):
        jobDetail = response.css('div.job-details')
        jobOverview = response.css('div.job-overview-inner table tr')
        job_overview_length = len(jobOverview)

        def getOverviewItem(index):
            values = jobOverview[index].css('td span::text').getall() if index < job_overview_length else []
            return values[0] if len(values) >= 1 else ''
        yield{
            'name': response.css('div.company-title::text').get(),
            'location': response.css('tr[itemprop=jobLocation] a span::text').get(),
            'image': response.css('div.company-logo img::attr(src)').get(),
            'website': '',
            'job-title': jobDetail.css('h1::text').get(),
            'position': '',
            'level': getOverviewItem(4),
            'experience': '',
            'total-position': getOverviewItem(1),
            'job-type': getOverviewItem(3),
            'salary': getOverviewItem(2),
            'education': '',
            'type': '',
            'deadline': response.css('span.apply-deadline::text').get(),
            'description': response.css('span[itemprop=description]').get(),
            'url': response.url,
            'slug': slugify(jobDetail.css('h1::text').get())
        }
