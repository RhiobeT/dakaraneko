#!/usr/bin/env python3
##
# Dakara Project
#

from nekoparse import cartoon_file2data
from music_parse import extract_tags

def parse_file_name(file_name):
    """ From a file name, returns a dictionnary with revelant values 
    """
    result = {}
    data = cartoon_file2data(file_name)
    title = data['title_music']
    result['title_work'] = data['title_cartoon']
    if title:
        result['title_music'] = title
    else:
        result['title_music'] = result['title_work']
    detail = data['detail']
    lang = data['language']
    if detail:
        result['detail'] = detail + " - " + lang
    else:
        result['detail'] = lang
        
    result['subtitle_work'] = data['subtitle_cartoon']
    result['work_type_name'] = 'Dessin anime'
    result['work_type_query_name'] = 'dessin-anime'
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
