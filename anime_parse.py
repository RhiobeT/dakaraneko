#!/usr/bin/env python3
##
# Dakara Project
#

from nekoparse import anime_file2data
from music_parse import extract_tags

def parse_file_name(file_name):
    """ From a file name, returns a dictionnary with revelant values 
    """
    result = {}
    data = anime_file2data(file_name)
    result['title_music'] = data['title_music']
    result['detail'] = data['detail']
    result['title_work'] = data['title_anime']
    result['subtitle_work'] = data['subtitle_anime']
    result['work_type'] = 'Anime'
    genre = data['genre']
    if genre['op']:
        result['link_type'] = 'OP'
        result['link_nb'] = genre['op_nbr']
    elif genre['ed']:
        result['link_type'] = 'ED'
        result['link_nb'] = genre['ed_nbr']
    elif genre['ins']:
        result['link_type'] = 'IN'
        result['link_nb'] = None 
    elif genre['is']:
        result['link_type'] = 'IS'
        result['link_nb'] = None 
    else:
        result['link_type'] = None
        result['link_nb'] = None

    result['artists'] = []

    result['tags'] = extract_tags(data['genre'])

    return result
