# T_T coding=utf-8 T_T

"""
This module is used for providing some useful tools.
"""

__author__ = "dtysky"
__email__ = "dtysky@outlook.com"
__name__ = "Utils"

import os
import time
from datetime import datetime
from pydub import AudioSegment
from config import config
from core import api as fa_muse



def date_now():
    """
    获取当前时间
    :return: datetime对象
    """
    return datetime.now()

def date_to_string(date):
    return date.strftime("%Y-%m-%d %H:%M:%S")

def date_to_timestamp(date):
    return int(time.mktime(date.timetuple()))

def media_normalize(type, fp, name):
    src = None
    if (type == "audio/mp3"):
        src = AudioSegment.from_mp3(fp)
    if (type == "audio/acc"):
        src = AudioSegment.from_m4a(fp)
    if (type == "audio/ogg"):
        src = AudioSegment.from_ogg(fp)
    export_path = './tmp/%s.wav' % name
    src.export(export_path, "wav")
    os.remove(fp)
    return export_path

def media_to_image(type, fs):
    name = "%d" % date_to_timestamp(date_now())
    media_path = media_normalize(type, fs, name)
    image_path = './tmp/%s.tiff' % name
    fa_muse.audio2image(media_path, image_path)
    os.remove(media_path)
    return image_path

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
