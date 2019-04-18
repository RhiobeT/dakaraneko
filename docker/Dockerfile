FROM python:3.6

RUN apt-get update
RUN apt-get install -y ffmpeg mediainfo

RUN wget $(curl --silent https://api.github.com/repos/DakaraProject/dakara-server/releases/latest | grep browser_download_url | sed -e 's/^.*\": \"//' -e 's/\"$//') -O dakara-server.zip

RUN unzip dakara-server.zip
RUN rm dakara-server.zip
RUN mv dakara-server* /dakara-server
RUN pip install -r /dakara-server/requirements.txt

RUN cp /dakara-server/dakara_server/dakara_server/local_settings.py.example /dakara-server/dakara_server/dakara_server/local_settings.py
RUN sed -i "s/^ALLOWED_HOSTS\ =\ \[/ALLOWED_HOSTS\ =\ \[\'\*\'/" /dakara-server/dakara_server/dakara_server/local_settings.py

COPY ./ /dakaraneko
RUN pip install -r dakaraneko/karaneko/requirements.txt

RUN sed -i -e 's/^DAKARA_SERVER_DIR=.*$/DAKARA_SERVER_DIR=\/dakara-server/' -e 's/^DAKARANEKO_DIR=.*$/DAKARANEKO_DIR=\/dakaraneko/' -e 's/^KARA_DIR=.*$/KARA_DIR=\/karabase/' /dakaraneko/feed.sh

COPY docker/entrypoint.sh /
RUN chmod u+x entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["run"]
