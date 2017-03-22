#!/usr/bin/env python3
##
# Dakara Project
#

from karaneko.nekoparse import NekoParseCartoon
from music_parse import extract_tags

def parse_file_name(file_name):
    """ From a file name, returns a dictionnary with revelant values 
    """
    result = {}
    cartoon = NekoParseCartoon(file_name)
    cartoon.parse()

    title = cartoon.title_music
    result['title_work'] = cartoon.title_cartoon
    if title:
        result['title_music'] = title
    else:
        result['title_music'] = cartoon.title_cartoon
    detail = cartoon.details

    lang = cartoon.language 
    if detail:
            result['detail'] = detail + " - " + lang
    else:
            result['detail'] = lang

    result['detail_video'] = ""
    result['version'] = ""
        
    result['subtitle_work'] = cartoon.subtitle_cartoon or '' 
    result['work_type_name'] = 'Dessin animé'
    result['work_type_query_name'] = 'dessin-anime'

    tags = cartoon.tags
    if tags.opening:
        result['link_type'] = 'OP'
        result['link_nb'] = tags.opening_nbr
    elif tags.ending:
        result['link_type'] = 'ED'
        result['link_nb'] = tags.ending_nbr

    elif tags.insert_song:
        result['link_type'] = 'IN'

    elif tags.image_song:
        result['link_type'] = 'IS'

    result['artists'] = []

    result['tags'] = extract_tags(tags)

    return result
