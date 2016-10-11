# T_T coding=utf-8 T_T

"""
This module is used for server.
"""

__author__ = "Tianyu Dai (dtysky)"
__email = "dtysky@outlook.com"
__name__ = "server"

from flask import Flask, Response, render_template, send_from_directory, redirect, url_for, request
from utils import logger


class WebServer(object):
    def __init__(self):
        self._server = Flask(
            "web_server",
            static_url_path="/static"
        )
        self._server.jinja_env.add_extension(
            "pyjade.ext.jinja.PyJadeExtension"
        )


    @property
    def web_server(self):
        return self._server

    def _response_with_template(self, template, data):
        response = Response(
            render_template(
                "%s.jade" % template,
                data=data
            ),
            status=200
        )
        response.headers.add(
            'Access-Control-Allow-Origin', '*'
        )
        return response


    def register(self):
        def _info_req(base, param):
            logger.info(
                "Request: %s\nParameters: %s\n" % (base, param)
            )

        @self._server.route("/")
        def index_handler():
            return self._response_with_template("index", {})

        @self._server.route("/<mode>/<path:path>")
        def files_handler(mode, path):
            print mode, path
            _info_req("Static", (mode, path))
            response = Response(
                send_from_directory(mode, path),
                status=200
            )
            response.headers.add(
                'Access-Control-Allow-Origin', '*'
            )
            return response
