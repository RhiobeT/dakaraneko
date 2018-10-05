#!/bin/bash

#
# This script call the dakara feeder for each karaoke folder
#

set -e
DAKARA_SERVER_DIR=/home/benjamin/Dakara/dakara-server
DAKARANEKO_DIR=/home/benjamin/Dakara/dakaraneko
KARA_DIR=/media/benjamin/Maxtor/Kara_Japan7
OPTIONS="--prune --append-only --no-progress"
cd ${DAKARA_SERVER_DIR}/dakara_server

# Activate virtualenv (uncomment to use it)
# ACTIVATE_PATH=/home/user/.virtualenvs/virtualenv_name/bin/activate
# source ${ACTIVATE_PATH}

rm $DAKARANEKO_DIR/generated/*

./manage.py feed $KARA_DIR $OPTIONS --parser $DAKARANEKO_DIR/anime_parse.py --directory Anime 
./manage.py dumpdata library.worktype --indent 2 > $DAKARANEKO_DIR/generated/library_worktype.json
./manage.py dumpdata library.work --indent 2 > $DAKARANEKO_DIR/generated/library_work.json

$DAKARANEKO_DIR/dump2animefile.py --path_worktype $DAKARANEKO_DIR/generated/library_worktype.json --path_work $DAKARANEKO_DIR/generated/library_work.json --path_scrapper $DAKARANEKO_DIR/mal_scrapper.json --output $DAKARANEKO_DIR/generated/animefile.json

./manage.py createworks $DAKARANEKO_DIR/generated/animefile.json
