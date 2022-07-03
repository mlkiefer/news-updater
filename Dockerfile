FROM python:3.10
RUN groupadd -r nextcloud-news-updater && useradd -r -g nextcloud-news-updater nextcloud-news-updater

WORKDIR /usr/src/news-updater
COPY . .
RUN python3 setup.py install --install-scripts=/usr/bin

WORKDIR /

USER nextcloud-news-updater
