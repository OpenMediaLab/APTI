# T_T coding=utf-8 T_T

"""
This module is used for providing some useful tools.
"""

__author__ = "dtysky"
__email__ = "dtysky@outlook.com"
__name__ = "Utils"

import os
import time
from MySQLdb import connect
from datetime import datetime, timedelta
from config import config


def date_now():
    """
    获取当前时间
    :return: datetime对象
    """
    return datetime.now()


def date_from_string(s):
    """
    从字符串获取datetime
    :param s: 字符串
    :return: datetime对象
    """
    return datetime.strptime(s, "%Y-%m-%d %H:%M:%S")


def date_to_string(date):
    """
    从datetime转换为字符串
    :param date: datetime对象
    :return: 字符串
    """
    return date.strftime("%Y-%m-%d %H:%M:%S")

def date_next_day(date):
    """
    从datetime获取下一日的整点值
    :param date: datetime对象
    :return: 字符串
    """
    next_day = add_date(date, 1, "day").strftime("%Y-%m-%d %H:%M:%S").split(" ")[0]
    return datetime.strptime(next_day, "%Y-%m-%d")

def date_to_timestamp(date):
    """
    将datetime转换为时间戳
    :param t: datetime对象
    :return: 时间戳, int
    """
    return int(time.mktime(date.timetuple()))


def add_date(date, value, mode):
    """
    将datetime对象加上若干mode单位
    :param date: datetime对象
    :param value: 增量, int
    :value mode: 运算类型, "day", "hour", "week"
    :return: datetime对象
    """
    if mode == "hour":
        return date + timedelta(hours=value)
    if mode == "day":
        return date + timedelta(days=value)
    return date + timedelta(weeks=value)


class Logger(object):
    """
    A monitor for printing and storing server state.
    """

    def __init__(self, log_dir_path):
        self._log_dir_path = log_dir_path
        self._time = ""
        self._file = None
        self._new_with_check()

    def _new_with_check(self):
        if not os.path.exists(self._log_dir_path):
            os.mkdir(self._log_dir_path)
        now = datetime.now().strftime("%Y-%m-%d")
        if now != self._time:
            self._time = now
            if self._file:
                self._file.close()
            self._file = open(
                "%s/%s.log" %
                (self._log_dir_path, now),
                "a"
            )

    def _log(self, message, color):
        self._new_with_check()
        line = "%s: %s\n" % (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            message
        )
        if config["dev_mode"]:
            print "%s%s" % (color, line)
        self._file.write(line)

    def info(self, message):
        self._log(
            "Info:\n%s" % message,
            "\033[1;32m"
        )

    def warning(self, message):
        self._log(
            "Warning:\n%s" % message,
            "\033[1;35m"
        )

    def error(self, message):
        self._log(
            "Error:\n%s" % message,
            "\033[1;31m"
        )


# Singleton
logger = Logger(config["log_path"])
