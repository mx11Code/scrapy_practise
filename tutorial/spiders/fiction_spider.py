import scrapy
import re
from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider, Rule
from tutorial.items import DmozItem
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from ..utils.utils import chinese_to_number
from ..items import FictionItem


class FictionSpider(CrawlSpider):
    name = "bookSpider"
    # rules = [
    #     Rule(LinkExtractor(allow=(r'\b1_\d+.html')), callback='parse_chapter')
    # ]
    start_urls = ["http://www.23us.so/list/1_1.html"]

    def parse(self, response):
        item = FictionItem()
        soup = BeautifulSoup(response.text, "lxml")
        trs = soup.find_all("tr", bgcolor='#FFFFFF')
        for tr in trs:
            td = tr.find_all("td")
            book_name = td[0].get_text()
            author = td[2].get_text()
            number_of_words = td[3].get_text()
            status = td[5].get_text()
            item['book_name'] = book_name
            item['author'] = author
            item['number_of_words'] = number_of_words
            item['status'] = status
            item['url'] = response.url
            yield item

        for element in response.css("#pagelink a:not([class])"):
            yield response.follow(element, self.parse)
