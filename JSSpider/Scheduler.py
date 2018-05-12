# -*- coding:utf-8 -*-

from multiprocessing import Process
from selenium import webdriver
from Spider import JSSpider
from Setting import *
import time
import pandas as pd
import random
from Log import Logger


class Scheduler:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def task1(self, url, path, begin, end):
        spider = JSSpider()
        spider.open_browser(url=url)
        spider.jump_to_page(begin)
        for i in xrange(begin, end):
            try:
                spider.parse(path, i)
            except Exception as e:
                time.sleep(60)
                spider.refresh_page()
                spider.parse(path, i)
            spider.next_page()
        spider.close_browser()
        pass

    def get_text(self, list_elements):
        return [i.text for i in list_elements]
        pass

    def task2(self, s_url, begin, end):
        logger = Logger()
        path = '//div[@class="bd"]/ul/li[@class="position_shares"]/div/'
        driver = webdriver.Chrome()
        for url in s_url[begin:end]:
            logger.info(url)
            driver.get(url)
            temp = random.randint(9,20)
            time.sleep(temp)
            list_fund_code = [url[26:32] for i in xrange(10)]
            try:
                list_stock_name = self.get_text(driver.find_elements_by_xpath(path + 'table/tbody/tr/td[1]')[0:10])
                list_stock_per = self.get_text(driver.find_elements_by_xpath(path + 'table/tbody/tr/td[2]')[0:10])
                sum = self.get_text(driver.find_elements_by_xpath(path + 'p/span[2]'))
                list_per_sum = [sum[0] for i in xrange(10)]
            except Exception as e:
                logger.error(e)
                continue
            dict_df = {u'基金代码':pd.Series(list_fund_code),
                       u'股票名称':pd.Series(list_stock_name),
                       u'股票占比':pd.Series(list_stock_per),
                       u'前十持仓占比合计':pd.Series(list_per_sum)}
            df = pd.DataFrame(dict_df, columns=[u'基金代码', u'股票名称',u'股票占比', u'前十持仓占比合计'])
            print(df)
            # df.to_excel('./Data3/fund_position_' + str(url[26:32]) + '.xlsx', index=False)
        driver.close()
        pass

    def run(self):
        df = pd.read_excel('./fund_list.xlsx')
        s_url = df[u'基金链接']
        p1 = Process(target=self.task2, args=(s_url, 0, 1000,))
        p1.start()
        time.sleep(20)
        p2 = Process(target=self.task2, args=(s_url, 1000, 2000,))
        p2.start()
        time.sleep(20)
        p3 = Process(target=self.task2, args=(s_url, 2000, 3000,))
        p3.start()
        time.sleep(20)
        pass

    pass


if __name__ == '__main__':
    s = Scheduler()
    s.run()
    pass
