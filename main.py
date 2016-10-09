# T_T coding=utf-8 T_T

"""
This module is used for main.
"""

__author__ = "Tianyu Dai (dtysky)"
__email = "dtysky@outlook.com"
__name__ = "__main__"


from core import audio2image, image2audio

if __name__ == "__main__":
    audio2image('test_files/test2.wav', 'test_files/test2.tiff')
    image2audio('test_files/test2.tiff', 'test_files/test3.wav')