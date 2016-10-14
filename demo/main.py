# T_T coding=utf-8 T_T

"""
This module is used for main.
"""

__author__ = "Tianyu Dai (dtysky)"
__email = "dtysky@outlook.com"
__name__ = "__main__"

import sys
sys.path.append("../")

from server import WebServer
from config import config
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop


if __name__ == "__main__":
    server = WebServer()
    server.register()
    if (config["dev_mode"]):
        server.web_server.run(
            config["server_ip"],
            config["server_port"],
            debug = True
        )
    else:
        server = HTTPServer(
            WSGIContainer(server.web_server)
        )
        server.listen(
            config["server_port"],
            config["server_ip"]
        )
        IOLoop.instance().start()
