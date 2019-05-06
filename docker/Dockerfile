FROM python:3.6

RUN apt-get update \
    && apt-get install -y ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY docker/get_dakara.sh /
RUN chmod u+x get_dakara.sh && /get_dakara.sh

RUN pip install -r /dakara-server/requirements.txt

COPY ./ /dakaraneko
RUN pip install -r dakaraneko/karaneko/requirements.txt

RUN sed -i -e 's+^DAKARA_SERVER_DIR=.*$+DAKARA_SERVER_DIR=/dakara-server+' -e 's+^DAKARANEKO_DIR=.*$+DAKARANEKO_DIR=/dakaraneko+' -e 's+^KARA_DIR=.*$+KARA_DIR=/karabase+' /dakaraneko/feed.sh

COPY docker/entrypoint.sh /
RUN chmod u+x entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["run"]
