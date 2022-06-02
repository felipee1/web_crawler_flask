import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlsplit


class ExtractorSpider(scrapy.Spider):
    name = "extractor"
    start_urls = []

    def __init__(self, start_urls,**kwargs):
        self.start_urls = [start_urls]
        super().__init__(**kwargs)


    def parse(self, response):
        split_url= urlsplit(self.start_urls[0])
        base_url= split_url.scheme+'://'+split_url.netloc

        data = list(map(lambda x: x if 'http' in x or '//' in x else base_url+x, response.xpath('.//@href').getall()))
        
        for url in data:
            yield response.follow(url=url, callback = self.parse_link_list, cb_kwargs = { "url":url })
    
    def parse_link_list(self, response, url):
        split_url= urlsplit(url)
        base_url= split_url.scheme+'://'+split_url.netloc

        data = list(map(lambda x: x if 'http' in x or '//' in x else base_url+x, response.xpath('.//@href').getall()))
        yield {
            "name":url,
            "list_links":data
        }