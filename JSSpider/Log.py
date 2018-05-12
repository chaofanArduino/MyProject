# -*- coding:utf-8 -*-


__all__ = ['Logger']

import logging

LOG_FORMAT = [
    '%(asctime)s - PID:%(process)d - %(levelname)s: %(message)s'
]

LOGFILE_PATH = [
    './log.txt'
]


class Logger:
    def __init__(self, name='root'):
        self.__logger = logging.getLogger(name=name)
        self.__set_logger()
        pass

    def __str__(self):
        pass

    def __set_logger(self):
        self.__logger.setLevel(level=logging.DEBUG)
        #
        handler1 = logging.FileHandler(LOGFILE_PATH[0])
        handler1.setLevel(level=logging.DEBUG)
        handler1.setFormatter(fmt=logging.Formatter(LOG_FORMAT[0]))
        self.__logger.addHandler(hdlr=handler1)
        #
        handler2 = logging.StreamHandler()
        handler2.setLevel(level=logging.DEBUG)
        handler2.setFormatter(fmt=logging.Formatter(LOG_FORMAT[0]))
        self.__logger.addHandler(hdlr=handler2)
        pass

    def debug(self, msg):
        self.__logger.debug(msg=msg)
        pass

    def info(self, msg):
        self.__logger.info(msg=msg)
        pass

    def warning(self, msg):
        self.__logger.warning(msg=msg)
        pass

    def error(self, msg):
        self.__logger.error(msg=msg)
        pass

    def critical(self, msg):
        self.__logger.critical(msg=msg)
        pass

    pass


if __name__ == '__main__':
    logger = Logger()
    logger.debug('This is a debug msg!')
    pass