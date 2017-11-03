# -*- coding:utf-8 -*-

from URLmanager import URLManager
from downloader import Downloader
from XMLparser import XMLParser


class Scheduler:
    def __init__(self):
        self.__url_manager = URLManager()
        self.__downloader = Downloader()
        self.__parser = XMLParser()
        pass

    def __str__(self):
        pass

    def run(self):
        start_url = ['http://www.iplaypy.com/jichu/set.html']
        self.__url_manager.put_url(list_url=start_url)
        while not self.__url_manager.empty():
            url = self.__url_manager.get_url()
            print(url)
            try:
                html = self.__downloader.download(url)
            except Exception as e:
                print(e)
                while not self.__url_manager.empty():
                    print(self.__url_manager.get_url())
            self.__parser.parser(html=html)
            self.__url_manager.put_url(list_url=self.__parser.get_url())
        pass

    pass


if __name__ == '__main__':
    s = Scheduler()
    s.run()
    pass
