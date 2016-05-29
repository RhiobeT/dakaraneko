##
# Dakara Project
#

from anime_parse import parse_file_name as parse_file_name_music
import random

artists = [
        "Megurine Luka",
        "Scandal",
        "supercell",
        "Iwasugi Natsu",
        ]

def parse_file_name(file_name):
    """ From a file name, returns a dictionnary with revelant values 
    """
    result = parse_file_name_music(file_name)
    result['work_type'] = 'Game'
    result['artists'] = [artists[random.randint(0, 3)] for i in range(random.randint(1, 3))]

    return result
