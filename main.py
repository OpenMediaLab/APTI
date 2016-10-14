# T_T coding=utf-8 T_T

"""
This module is used for main.
"""

__author__ = "Tianyu Dai (dtysky)"
__email = "dtysky@outlook.com"
__name__ = "__main__"


from core import audio2image, image2audio

if __name__ == "__main__":
    audio_file_name = "BWV-998-Aria"
    audio2image(audio_file_name+'.wav', audio_file_name+'.tiff')
    image2audio(audio_file_name + '.tiff', 'after-'+audio_file_name+'.wav')
    
    audio_file_name = "Duke Ellington - Rext"
    audio2image(audio_file_name+'.wav', audio_file_name+'.tiff')
    image2audio(audio_file_name + '.tiff', 'after-'+audio_file_name+'.wav')

    audio_file_name = "out"
    image2audio(audio_file_name + '.tiff', 'after-'+audio_file_name+'.wav')


