FROM python:3.10-alpine
RUN addgroup -S nextcloud-news-updater && adduser -S nextcloud-news-updater -G nextcloud-news-updater

WORKDIR /usr/src/news-updater
COPY . .
RUN python3 setup.py install --install-scripts=/usr/bin

WORKDIR /

USER nextcloud-news-updater
