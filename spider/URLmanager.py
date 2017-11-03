# -*- coding:utf-8 -*-

from Queue import Queue

__all__ = ['URLManager']


class URLManager:
    def __init__(self):
        self.__used_url = set()
        self.__url_queue = Queue()
        pass

    def __str__(self):
        pass

    def put_url(self, list_url):
        for url in list_url:
            if url not in self.__used_url:
                self.__url_queue.put(url)

    def get_url(self):
        if not self.__url_queue.empty():
            url = self.__url_queue.get()
            self.__used_url.add(url)
            return url
        return None

    def empty(self):
        if self.__url_queue.empty():
            return True
        return False

    def size(self):
        return self.__url_queue.qsize()
    pass


if __name__ == '__main__':
    url_manager = URLManager()
    list_url = [
        'http://www.jb51.net/article/58004.htm',
        'https://www.zhihu.com/question/21094489'
    ]
    url_manager.put_url(list_url)
    print(url_manager.get_url())
    print(url_manager.get_url())
    pass
