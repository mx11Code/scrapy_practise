import scrapy
import re
from bs4 import BeautifulSoup
from scrapy.spider import CrawlSpider, Rule
from tutorial.items import DmozItem
from scrapy.http import Request


class DmozSpider(CrawlSpider):
    name = "dmoz"
    allowed_domains = ["23us.so"]
    bash_url = "http://www.23us.so/list/"
    bashurl = ".html"

    # http://www.23us.so/files/article/html/18/18661/\d+.html

    def start_requests(self):
        for i in range(1, 10):
            url = self.bash_url + str(i) + "_1" + self.bashurl
            yield Request(url, self.parse)
        yield Request('http://www.23us.so/full.html', self.parse)

    def parse(self, response):
        print(response.text)
