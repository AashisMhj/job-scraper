# Job Scraper

Web scraper build using scrapy to scrape date of job portals.

## Installation Guide
```bash
# install packages from requirement.txt
pip -r requirements.txt

cd job_scraper
# seel all the crawlers
scrapy list

# scrape data
scrapy crawl <crawler_name>  -O <outpfile_name>
```


## Job portal lists
- [X] [kathmandujobs](https://kathmandujobs.com/)
- [X] jobsnepal
- [ ] kantipurjob
- [ ] merojob
- [ ] [jobsniper](https://www.jobssniper.com/)

## TODO
* Scrape multiple pages
* trim clean fields
* format date values