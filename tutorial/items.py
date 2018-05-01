# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DmozItem(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()
    novel_url = scrapy.Field()
    serial_status = scrapy.Field()
    serial_number = scrapy.Field()
    category = scrapy.Field()
    name_id = scrapy.Field()


class FictionContentItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    seq = scrapy.Field()

    # def __init__(self, seq, title, content):
    #     # self.seq = seq
    #     # self.title = title
    #     # self.content = content
    #     super(FictionContent, self).__init__()


class FictionItem(scrapy.Item):
    book_name = scrapy.Field()
    author = scrapy.Field()
    number_of_words = scrapy.Field()
    status = scrapy.Field()
    url = scrapy.Field()


class DoubanItem(scrapy.Item):
    title = scrapy.Field()
    English_title = scrapy.Field()
    other_title = scrapy.Field()
    # message = scrapy.Field()
    # year = scrapy.Field()
    # country = scrapy.Field()
    # director = scrapy.Field()
    # protagonist = scrapy.Field()
    # category = scrapy.Field()
