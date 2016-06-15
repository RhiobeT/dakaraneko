#!/usr/bin/env python3
##
# Dakaraneko Project
#
# Script for setting work types icons name and tags colors id 
#

import os
import sys
import logging
import importlib
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dakara_server.settings")
package_path = os.path.dirname(__file__)
sys.path.append(
        os.path.join(
            package_path,
            os.pardir,
            "dakara_server"
            )
        )

try:
    from library.models import *
    from library.serializers import SongSerializer
    from django.test.client import RequestFactory
    import django

except ImportError as e:
    raise ImportError("Unable to import Django modules")

file_coding = sys.getfilesystemencoding()
context_dummy = dict(request=RequestFactory().get('/'))
django.setup()

# Work Types Icons
work_type_icons = {"Anime": "television", "Live action": "television", "Game": "gamepad"}

for key, value in work_type_icons.items():
    work_type = WorkType.objects.filter(name=key).first()
    if work_type:
        work_type.icon_name = value
        work_type.save()

# Tags color Ids
tags_color_ids = {
    'PV': 0,
    'AMV': 1,
    'LIVE': 2,
    'LONG': 3,
    'COURT': 4,
    'COVER': 5,
    'REMIX': 6,
    'INST': 7,
}

for key, value in tags_color_ids.items():
    tag = SongTag.objects.filter(name=key).first()
    if tag:
        tag.color_id = value
        tag.save()



