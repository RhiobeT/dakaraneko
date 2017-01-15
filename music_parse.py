#!/usr/bin/env python3
##
# Dakara Project
#

from karaneko.nekoparse import NekoParseMusic, NekoParseTagsGeneric, ConventionError
from warnings import warn

TAGS_DICT = {
        tag[0]: tag[2] for tag in NekoParseTagsGeneric.TAGS_BASE
        }

def extract_tags(tags):
    """ From the genre dictionnary, returns list of tags
    """ 
    tags_list = []

    for tag_attr, tag_name in TAGS_DICT.items():
        if getattr(tags, tag_attr):
            tags_list.append(tag_name)

    return tags_list

def parse_file_name(file_name):
    """ From a file name, returns a dictionnary with revelant values 
    """
    result = {}
    music = NekoParseMusic(file_name)
    music.parse()

    result['title_music'] = music.title_music
    result['version'] = music.extras.version
    result['detail'] = music.details
    result['artists'] = music.singers
    result['artists'].extend(music.composers)
    if music.extras.original_artist:
        result['artists'].append(music.extras.original_artist)

    extras = music.extras
    if extras.opening:
        result['link_type'] = 'OP'
        result['link_nb'] = extras.opening_nbr
        result['title_work'] = extras.opening

    elif extras.ending:
        result['link_type'] = 'ED'
        result['link_nb'] = extras.ending_nbr
        result['title_work'] = extras.ending

    elif extras.insert_song:
        result['link_type'] = 'IN'
        result['title_work'] = extras.insert_song

    elif extras.image_song:
        result['link_type'] = 'IS'
        result['title_work'] = extras.image_song

    if result.get('link_type'):
        result['work_type_name'] = 'Anime'
        result['work_type_query_name'] = 'anime'

    detail_video_list = []
    if extras.video:
        detail_video_list.append(extras.video)

    if extras.amv:
        detail_video_list.append(extras.amv)

    if extras.title_video:
        detail_video_list.append(extras.title_video)

    result['detail_video'] = ', '.join(detail_video_list)

    result['subtitle_work'] = "" # TODO
    result['tags'] = extract_tags(music.tags)

    return result
