#!/usr/bin/env python3
##
# Dakara Project
#

from nekoparse import music_file2data, GenreConventionError
from warnings import warn

def parse_file_name(file_name):
    """ From a file name, returns a dictionnary with revelant values 
    """
    result = {}
    try:
        data = music_file2data(file_name)

    except GenreConventionError as error:
        warn("Error with '{}': {}".format(file_name, error))
        raise ValueError

    result['title_music'] = data['title_music']
    result['detail'] = data['detail']
    result['artists'] = []
    result['artists'].extend(data['singer'])
    if data['composer'] and data['composer'][0]:
        result['artists'].extend(data['composer'])

    result['title_work'] = None
    result['subtitle_work'] = None
    result['link_type'] = None
    result['link_nb'] = None
    result['work_type'] = None

    # tags
    tags = []
    genre = data['genre']
    tag_list = [
            'pv',
            'amv',
            'live',
            'long',
            'court',
            'cover',
            'remix',
            ]

    for tag_name in tag_list:
        if genre.get(tag_name):
            tags.append(tag_name.upper())

    result['tags'] = tags

    return result
