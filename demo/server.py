# T_T coding=utf-8 T_T

"""
This module is used for server.
"""

__author__ = "Tianyu Dai (dtysky)"
__email = "dtysky@outlook.com"
__name__ = "server"

from flask import Flask, Response, render_template, send_from_directory, request
from utils import logger
from os import path
from config import config


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

    def _response(self, data, type="text/html", status=200):
        response = Response(
            data,
            status=status,
            mimetype=type
        )
        response.headers.add(
            'Access-Control-Allow-Origin', '*'
        )
        return response

    def _response_with_template(self, template, data):
        return self._response(
            render_template(
                "%s.jade" % template,
                data=data
            )
        )

    def register(self):
        def _info_req(base, param):
            logger.info(
                "Request: %s\nParameters: %s\n" % (base, param)
            )

        @self._server.route("/", methods=['GET'])
        def index_handler():
            return self._response_with_template("index", {})

        @self._server.route("/upload", methods=['POST'])
        def upload_handler():
            f = request.files["file"]
            if f.content_type not in config["acceptable_type"]:
                return self._response(
                    {"message": "File type mast be '%s'" % ', '.join(config["acceptable_type"])},
                    "application/json",
                    406
                )
            f.save("./tmp/%s" % f.filename)
            return self._response({"id": f.filename}, "application/json")

        @self._server.route("/<mode>/<path:path>", methods=['GET'])
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
