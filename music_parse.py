#!/usr/bin/env python3
##
# Dakara Project
#

from karaneko.nekoparse import NekoParseMusic, ConventionError
from warnings import warn

TAG_LIST = [
        'pv',
        'amv',
        'live',
        'long',
        'cover',
        'remix',
        ]

def extract_tags(genre):
    """ From the genre dictionnary, returns list of tags
    """ 
    tags = []

    for tag_name in TAG_LIST:
        if getattr(genre, tag_name):
            tags.append(tag_name.upper())

    return tags
    

def parse_file_name(file_name):
    """ From a file name, returns a dictionnary with revelant values 
    """
    result = {}
    parser = NekoParseMusic(file_name)

    try:
        parser.parse()

    except ConventionError as error:
        warn("Error with '{}': {}".format(file_name, error))
        raise ValueError

    result['title_music'] = parser.title_music
    result['detail'] = parser.details
    result['artists'] = parser.singers
    result['artists'].extend(parser.composers)

    result['title_work'] = None
    result['subtitle_work'] = None
    result['link_type'] = None
    result['link_nb'] = None
    result['work_type'] = None

    result['tags'] = extract_tags(parser.tags)

    return result
