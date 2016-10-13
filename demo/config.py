# T_T coding=utf-8 T_T

"""
This module is used for config.
"""

__author__ = "Tianyu Dai (dtysky)"
__email = "dtysky@outlook.com"
__name__ = "config"

import os


config_dev = {
    "server_ip": "127.0.0.1",
    "server_port": 4884,
    "dev_mode": True
}

config_pd = {
    "server_ip": "127.0.0.1",
    "server_port": 4884,
    "dev_mode": False
}

config = {
    "acceptable_type": ["audio/ogg", "audio/acc", "audio/mp3"],
    "image_type": "tiff",
    "env": os.environ["PYTHON_ENV"],
    "log_path": "./logs"
}

config.update(config_dev if os.environ["PYTHON_ENV"] == "development" else config_pd)
