#!/usr/bin/env python3
##
# Dakara Project
#

from anime_parse import parse_file_name as anime_parse_file_name
from music_parse import parse_file_name as music_parse_file_name

def parse_file_name(file_name):
    """ AutoDetect file name as anime or music
    """
    if any((
        'OP' in file_name,
        'ED' in file_name,
        'INS' in file_name,
        'IS' in file_name,
        )):

        return anime_parse_file_name(file_name)

    else:
        return music_parse_file_name(file_name)
