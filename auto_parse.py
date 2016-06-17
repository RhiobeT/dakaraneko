#!/usr/bin/env python3
##
# Dakara Project
#

from nekoparse import anime_file2data
from anime_parse import parse_file_name as anime_parse_file_name
from music_parse import parse_file_name as music_parse_file_name

def parse_file_name(file_name):
    """ AutoDetect file name as anime or music
    """
    data = anime_file2data(file_name)
    genre = data['genre']
    if genre['op'] or genre['ed'] or genre['ins'] or genre['is']:
        return anime_parse_file_name(file_name)
    else:
        return music_parse_file_name(file_name)

    return result
