import scrapy
import re
import base64
import urllib.request
from bs4 import BeautifulSoup
from scrapy.spider import CrawlSpider, Rule
from tutorial.items import DoubanItem
from scrapy.http import Request, FormRequest
import os
import time
from scrapy.linkextractors import LinkExtractor
import getpass


class DoubanSpider(CrawlSpider):
    name = "Douban"
    allowed_domains = ["douban.com"]

    headers = {
        "UserAgent": "Mozilla / 5.0 (Windows NT 10.0; WOW64) AppleWebKit / 537.36 (KHTML, likeGecko) Chrome / 55.0.2883.87 Safari / 537.36"}

    # rules = [
    #     # Rule(LinkExtractor(),callback=)
    # ]

    def start_requests(self):
        return [
            Request("https://accounts.douban.com/login", callback=self.login),
            Request("https://movie.douban.com/top250?start=0&filter=", callback=self.parse)
        ]

    def parse(self, response):
        """
        :param response: abcfdasfdsa
        :return:
        """
        item = DoubanItem()
        soup = BeautifulSoup(response.text, "lxml")
        lis = soup.find("ol").find_all("li")
        for li in lis:
            all_title = li.find_all("span", attrs={"class": "title"})
            title = all_title[0].get_text()
            if len(all_title) > 1:
                english_title = all_title[1].get_text()
            else:
                english_title = ""
            other_title = li.find("span", attrs={"class": "other"}).get_text()
            item['title'] = title
            item['English_title'] = english_title
            item['other_title'] = other_title

            yield item

        for element in response.css("div [class='paginator'] a"):
            yield response.follow(element, self.parse)

    def login(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        captcha = soup.find(id="captcha_image").get('src')
        print("正在保存验证码图片")
        captchapicfile = os.path.join("E:", "douban", str(time.time()) + ".png")
        urllib.request.urlretrieve(captcha, filename=captchapicfile)
        print("请输入验证码")
        captcha_value = input()
        data = {
            "form_email": "",
            "form_password": "",
            "captcha-solution": captcha_value,
        }
        print("正在登陆中")
        return [FormRequest.from_response(response,
                                          headers=self.headers,
                                          formdata=data,
                                          callback=self.crawlerdata,
                                          )]

    def crawlerdata(self, response):
        print("登录成功")
        # with open(os.path.join("E:", "douban", str(time.time()) + ".html"), "w+") as f:
        #     f.write(response.text)
        title = response.xpath("/html/head/title/text()").extract()
        content2 = response.xpath("//meta[@name='description']/@content").extract()
        print(title[0])
