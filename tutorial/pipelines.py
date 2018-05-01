# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from tutorial import settings
import logging
import pymysql

logger = logging.getLogger('mylogger')


class DBPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOSTS,
            db=settings.MYSQL_DB,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)

        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        if spider.name != "bookSpider":
            return item
        try:
            # 插入数据
            self.cursor.execute(
                "INSERT INTO fiction(book_name, author, number_of_words,status, url) VALUES (%s, %s, %s, %s, %s)",
                (item['book_name'], item['author'], item['number_of_words'], item['status'], item["url"])
            )

            self.connect.commit()

        except Exception as error:
            logger.exception("Exception Logged", error)
        return item


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class FictionPipeline(object):
    def process_item(self, item, spider):
        pass


class DoubanPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOSTS,
            db=settings.MYSQL_DB,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)

        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        if spider.name != "Douban":
            return item
        try:
            self.cursor.execute(
                "INSERT INTO douban(title, English_title, other_title) VALUES (%s, %s, %s)",
                (item['title'], item['English_title'], item['other_title'])
            )

            self.connect.commit()

        except Exception as error:
            logger.exception("Exception Logged", error)
        return item
