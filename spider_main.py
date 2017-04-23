# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import url_manager
import html_downloader
import html_parser
import html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        # 添加到url管理器中
        self.urls.add_new_url(root_url)
        # 循环读取
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()

                print 'spider %d : %s' % (count, new_url)

                html_count = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_count)

                # 把new_urls添加到url管理器中
                self.urls.add_new_urls(new_urls)
                # 把数据存储到outputer
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break

                count = (count + 1)
            except :
                print 'spider failed'

        # 输出
        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/link?url=Ipctz5pN6lyb-Ju2veITR6E5HImrd1FAa8vUteDeYEu42cp5aVs87oorGLLnmV3fTUZ_PZLXL_wIIucjheda2wozSgMpjJdzzKK0iN2Q6PDYNum9BArlQoup8fV9k3hD9rCvAG8pHO8G2BT3F53lAK"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)