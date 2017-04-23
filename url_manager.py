# -*- coding: utf-8 -*-
__author__ = 'Administrator'


class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_news = set()

    # 添加单个url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_news:
            self.new_urls.add(url)

    # 添加多个urls
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return

        for url in urls:
            self.add_new_url(url)

    # 判断是否有新的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 获取新的url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_news.add(new_url)
        return new_url