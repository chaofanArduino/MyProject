# -*- coding:utf-8 -*-

from selenium import webdriver
from Setting import *
import time
import pandas as pd
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class JSSpider:
    def __init__(self):
        self.__browser = None
        self.__list_df = []
        pass

    def open_browser(self, url):
        self.__browser = webdriver.Chrome()
        self.__browser.get(url)
        pass

    def close_browser(self):
        self.__browser.close()
        pass

    def log_in(self, account, pass_word):
        pass

    def __get_text(self, list_elements):
        return [i.text for i in list_elements]
        pass

    def next_page(self):
        print(self.__browser.find_elements_by_xpath(NEXT_PAGE)[-2].text)
        self.__browser.find_elements_by_xpath(NEXT_PAGE)[-2].click()
        time.sleep(6)
        pass

    def jump_to_page(self, page):
        self.__browser.find_elements_by_xpath(TO_PAGE)[0].clear()
        self.__browser.find_elements_by_xpath(TO_PAGE)[0].send_keys(str(page))
        self.__browser.find_elements_by_xpath(NEXT_PAGE)[-1].click()
        time.sleep(6)
        pass

    def refresh_page(self):
        try:
            self.__browser.find_elements_by_xpath(NEXT_PAGE)[-1].click()
        except Exception as e:
            time.sleep(60)
            self.__browser.find_elements_by_xpath(NEXT_PAGE)[-1].click()
        time.sleep(15)
        pass

    def parse(self, path, count):
        list_index = self.__get_text(self.__browser.find_elements_by_xpath(INDEX))
        list_stockholder_name = self.__get_text(self.__browser.find_elements_by_xpath(STOCKHOLDER_NAME))
        list_stockholder_type = self.__get_text(self.__browser.find_elements_by_xpath(STOCKHOLDER_TYPE))
        list_stockholder_rank = self.__get_text(self.__browser.find_elements_by_xpath(STOCKHOLDER_RANK))
        list_stock_code = self.__get_text(self.__browser.find_elements_by_xpath(STOCK_CODE))
        list_stock_name = self.__get_text(self.__browser.find_elements_by_xpath(STOCK_NAME))
        list_report_period = self.__get_text(self.__browser.find_elements_by_xpath(REPORT_PERIOD))
        list_hold_amount = self.__get_text(self.__browser.find_elements_by_xpath(HOLD_AMOUNT))
        list_hold_proportion = self.__get_text(self.__browser.find_elements_by_xpath(HOLD_PROPORTION))
        list_amount_change = self.__get_text(self.__browser.find_elements_by_xpath(AMOUNT_CHANGE))
        list_change_proportion = self.__get_text(self.__browser.find_elements_by_xpath(CHANGE_PROPORTION))
        list_hold_change = self.__get_text(self.__browser.find_elements_by_xpath(HOLD_CHANGE))
        list_market_value = self.__get_text(self.__browser.find_elements_by_xpath(MARKET_VALUE))
        list_issue_date = self.__get_text(self.__browser.find_elements_by_xpath(ISSUE_DATE))
        dict_df = {LIST_COLUMNS[0]: list_index,
                   LIST_COLUMNS[1]: list_stockholder_name,
                   LIST_COLUMNS[2]: list_stockholder_type,
                   LIST_COLUMNS[3]: list_stockholder_rank,
                   LIST_COLUMNS[4]: list_stock_code,
                   LIST_COLUMNS[5]: list_stock_name,
                   LIST_COLUMNS[6]: list_report_period,
                   LIST_COLUMNS[7]: list_hold_amount,
                   LIST_COLUMNS[8]: list_hold_proportion,
                   LIST_COLUMNS[9]: list_amount_change,
                   LIST_COLUMNS[10]: list_change_proportion,
                   LIST_COLUMNS[11]: list_hold_change,
                   LIST_COLUMNS[12]: list_market_value,
                   LIST_COLUMNS[13]: list_issue_date}
        df = pd.DataFrame(dict_df, columns=LIST_COLUMNS)
        df.to_excel(path + str(count) + '.xlsx', index=False)
        print(df)
        return df
        pass

    def run(self):
        self.open_browser(URL[0])
        # self.jump_to_page(17)
        for i in xrange(1, 699):
            try:
                df = self.parse(i)
            except Exception as e:
                self.__browser.find_elements_by_xpath(NEXT_PAGE)[-1].click()
                time.sleep(20)
                df = self.parse(i)
            self.__list_df.append(df)
            self.next_page()
        df = pd.concat(self.__list_df)
        print(df)
        df.to_excel('./circulation_stockholder_10.xlsx', index=False)
        self.close_browser()



if __name__ == '__main__':
    a = JSSpider()
    a.run()
    pass
