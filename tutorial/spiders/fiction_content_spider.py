import scrapy
import re
from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider, Rule
from tutorial.items import DmozItem
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from ..utils.utils import chinese_to_number
from ..items import FictionContentItem


class FictionSpider(CrawlSpider):
    name = "fiction_content"
    rules = [
        Rule(LinkExtractor(allow=(r'\b18\/18661\/\d+.html')), callback='parse_chapter')
    ]
    start_urls = ["http://www.23us.so/files/article/html/18/18661/index.html"]



    def parse_chapter(self, response):
        item = FictionContentItem()
        title = response.css(".bdsub dl dd h1::text")[0].extract()
        seq = chinese_to_number(title)
        content = response.css("#contents::text").extract()
        item['title'] = title
        item['seq'] = seq
        item['content'] = content
        return item
