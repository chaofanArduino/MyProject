# -*- coding:utf-8 -*-

from lxml import etree

__all__ = ['XMLParser']


class XMLParser:
    def __init__(self):
        self.__list_url = []
        self.__dict_item = {}
        pass

    def __str__(self):
        pass

    def get_url(self):
        return self.__list_url

    def get_item(self):
        return self.__dict_item

    def parser(self, html):
        selector = etree.HTML(html)
        self.__list_url = selector.xpath('//li/a/@href')
        pass

    pass


if __name__ == '__main__':
    from downloader import Downloader
    url = 'http://www.iplaypy.com/jichu/set.html'
    html = Downloader().download(url)
    parser = XMLParser()
    parser.parser(html)
    pass
