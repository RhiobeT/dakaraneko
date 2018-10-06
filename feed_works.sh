#!/bin/bash

#
# This script call the dakara feeder for each karaoke folder
#

set -e
DAKARA_SERVER_DIR=/path/to/dakara-server
DAKARANEKO_DIR=/path/to/dakaraneko
OPTIONS_WORKS="--debug --update-only"
cd ${DAKARA_SERVER_DIR}/dakara_server

# Activate virtualenv (uncomment to use it)
# ACTIVATE_PATH=/home/user/.virtualenvs/virtualenv_name/bin/activate
# source ${ACTIVATE_PATH}

mkdir -p $DAKARANEKO_DIR/generated
rm -rf $DAKARANEKO_DIR/generated/*

./manage.py dumpdata library.worktype --indent 2 > $DAKARANEKO_DIR/generated/library_worktype.json
./manage.py dumpdata library.work --indent 2 > $DAKARANEKO_DIR/generated/library_work.json

$DAKARANEKO_DIR/dump2animefile.py --path_worktype $DAKARANEKO_DIR/generated/library_worktype.json --path_work $DAKARANEKO_DIR/generated/library_work.json --path_scrapper $DAKARANEKO_DIR/mal_scrapper.json --output $DAKARANEKO_DIR/generated/animefile.json

./manage.py createworks $OPTIONS_WORKS $DAKARANEKO_DIR/generated/animefile.json
