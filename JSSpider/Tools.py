# -*- coding:utf-8 -*-

from lxml import etree
from selenium import webdriver
from Setting import *
import time
import pandas as pd
import sys
import logging

reload(sys)
sys.setdefaultencoding('utf-8')


class FundSpider:
    def __init__(self):
        self.__selector = None
        pass

    def read_html(self, filename):
        self.__selector = etree.HTML(open(filename, 'r').read())

    def parse(self):
        list_fund_index = self.__selector.xpath(FUND_INDEX)
        list_fund_code = self.__selector.xpath(FUND_CODE)
        list_fund_name = self.__selector.xpath(FUND_NAME)
        list_fund_link = self.__selector.xpath(FUND_LINK)
        list_fund_UNW = self.__selector.xpath(FUND_UNW)
        list_fund_date = self.__selector.xpath(FUND_DATE)
        list_one_year = self.__selector.xpath(ONE_YEAR)
        list_two_year = self.__selector.xpath(TWO_YEAR)
        list_three_year = self.__selector.xpath(THREE_YEAR)
        list_five_year = self.__selector.xpath(FIVE_YEAR)
        list_fund_rate = self.__selector.xpath(FUND_RATE)
        list_commission_charges = self.__selector.xpath(COMMISSION_CHARGES)
        dict_df = {TABLE2_COLUMNS[0]: list_fund_index,
                   TABLE2_COLUMNS[1]: list_fund_code,
                   TABLE2_COLUMNS[2]: list_fund_name,
                   TABLE2_COLUMNS[3]: list_fund_link,
                   TABLE2_COLUMNS[4]: list_fund_UNW,
                   TABLE2_COLUMNS[5]: list_fund_date,
                   TABLE2_COLUMNS[6]: list_one_year,
                   TABLE2_COLUMNS[7]: list_two_year,
                   TABLE2_COLUMNS[8]: list_three_year,
                   TABLE2_COLUMNS[9]: list_five_year,
                   TABLE2_COLUMNS[10]: list_fund_rate,
                   TABLE2_COLUMNS[11]: list_commission_charges}
        df = pd.DataFrame(dict_df, columns=TABLE2_COLUMNS[0:12])
        df[u'基金链接'] = 'http://fund.eastmoney.com/' + df[u'基金链接'] + '.html'
        df.to_excel('./fund_list.xlsx', index=False)
        print(df)
        return df
        pass

    def run(self):
        df = pd.read_excel('./fund_list.xlsx')
        s_url = df[u'基金链接']
        web = webdriver.Chrome()


if __name__ == '__main__':
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(filename='./log.txt', level=logging.DEBUG, format=LOG_FORMAT)
    logging.info('This is a INFO message!')
    logging.error("This is a error log!")
    pass
