#!/bin/bash

#
# This Script sync existing karaoke database with server.
# If changes are detected, it will execute the feeder to update the database
#

FEED_SCRIPT=/path/to/feed.sh
KARA_DIR=/path/to/karaoke_folder/
SERVER_URL="https://exemple.com"
USER="login"
PASSWORD="pass"

echo "Initiating file sync"

SYNC_LOGS="$(nextcloudcmd --non-interactive -u $USER -p $PASSWORD $KARA_DIR $SERVER_URL 2>&1)"

#echo "$SYNC_LOGS"

echo "$SYNC_LOGS" | grep -E "INSTRUCTION_(NEW|REMOVE|RENAME|SYNC)"
if [ $? -eq 0 ];
then
  echo "Changes detected, starting feeder"
  bash $FEED_SCRIPT
else
  echo "No changes"
fi

