# -*- coding:utf-8 -*-

INDEX = "//div[@class='section']/table/tbody/tr/td[1]"  # 序号
STOCKHOLDER_NAME = "//div[@class='section']/table/tbody/tr/td[2]/a"  # 股东名称
STOCKHOLDER_TYPE = "//div[@class='section']/table/tbody/tr/td[3]"  # 股东类型
STOCKHOLDER_RANK = "//div[@class='section']/table/tbody/tr/td[4]"  # 股东排名
STOCK_CODE = "//div[@class='section']/table/tbody/tr/td[5]/a"  # 股票代码
STOCK_NAME = "//div[@class='section']/table/tbody/tr/td[6]/a"  # 股票简称
REPORT_PERIOD = "//div[@class='section']/table/tbody/tr/td[8]"  # 报告期
HOLD_AMOUNT = "//div[@class='section']/table/tbody/tr/td[9]"  # 持股数量
HOLD_PROPORTION = "//div[@class='section']/table/tbody/tr/td[10]"  # 持股占比
AMOUNT_CHANGE = "//div[@class='section']/table/tbody/tr/td[11]"  # 数量变化
CHANGE_PROPORTION = "//div[@class='section']/table/tbody/tr/td[12]"  # 数量变化占比
HOLD_CHANGE = "//div[@class='section']/table/tbody/tr/td[13]"  # 持股变化
MARKET_VALUE = "//div[@class='section']/table/tbody/tr/td[14]"  # 市值
ISSUE_DATE = "//div[@class='section']/table/tbody/tr/td[15]"  # 公告日

NEXT_PAGE = "//div[@class='content']/div[@class='PageNav']/div[@class='Page']/a"
TO_PAGE = "//input[@id='PageContgopage']"

LIST_COLUMNS = [u'序号', u'股东名称', u'股东类型', u'股东排名', u'股票代码',
                u'股票简称', u'报告期', u'持股数量', u'持股占比', u'数量变化',
                u'数量变化占比', u'持股变化', u'市值', u'公告日']

URL = ["http://data.eastmoney.com/gdfx/HoldingDetail.aspx",
       "http://data.eastmoney.com/gdfx/holdingDetail.aspx?tab=1"]

PATH = ['./Data/c_stockholder_10_',
        './Data/stockholder_10_']

FUND_INDEX = '//tbody/tr/td[2]//text()'
FUND_CODE = '//tbody/tr/td[3]//text()'
FUND_NAME = '//tbody/tr/td[4]//text()'
FUND_LINK = '//tbody/tr/td[3]//text()'
FUND_UNW = '//tbody/tr/td[6]//text()'
FUND_DATE = '//tbody/tr/td[7]/text()'
ONE_YEAR = '//tbody/tr/td[8]//text()'
TWO_YEAR = '//tbody/tr/td[9]//text()'
THREE_YEAR = '//tbody/tr/td[10]//text()'
FIVE_YEAR = '//tbody/tr/td[11]//text()'
FUND_RATE = '//tbody/tr/td[12]//text()'
COMMISSION_CHARGES = '//tbody/tr/td[13]//text()'
STOCK_01 = ''
STOCK_02 = ''
STOCK_03 = ''
STOCK_04 = ''
STOCK_05 = ''
STOCK_06 = ''
STOCK_07 = ''
STOCK_08 = ''
STOCK_09 = ''
STOCK_10 = ''

TABLE2_COLUMNS = [u'序号', u'基金代码', u'基金名称', u'基金链接', u'单位净值',
                  u'日期', u'近1年收益', u'近2年收益', u'近3年收益', u'近5年收益',
                  u'上海证券评级', u'手续费',
                  u'股票01', u'股票02', u'股票03', u'股票04', u'股票05',
                  u'股票06', u'股票07', u'股票08', u'股票09', u'股票10']
