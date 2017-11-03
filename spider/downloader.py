# -*- coding:utf-8 -*-

import urllib2

__all__ = ['Downloader']


class Downloader:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def download(self, url):
        req = urllib2.Request(url)
        try:
            html = urllib2.urlopen(req).read()
            print html
        except Exception as e:
            raise
        return html
    pass


if __name__ == '__main__':
    url = 'http://so.iplaypython.com/'
    Downloader().download(url)
    pass
