FROM            python:3.6.5-slim
MAINTAINER      rlaalsrbgk@gmail.com

RUN             apt -y update && apt -y dist-upgrade
RUN             apt -y install build-essential
RUN             apt -y install nginx supervisor

COPY            ./requirements.txt  /srv/
RUN             pip install -r /srv/requirements.txt

ENV             BUILD_MODE              production
ENV             DJANGO_SETTINGS_MODULE  config.settings.${BUILD_MODE}

COPY            .       /srv/project
ENV             PROJECT_DIR             /srv/project


RUN         cp -f   ${PROJECT_DIR}/.config/${BUILD_MODE}/nginx.conf \
                    /etc/nginx/nginx.conf && \

            cp -f   ${PROJECT_DIR}/.config/${BUILD_MODE}/nginx_app.conf \
                    /etc/nginx/sites-available/ && \

            rm -rf  /etc/nginx/sites-enabled/* && \


            ln -sf  /etc/nginx/sites-available/nginx_app.conf \
                    /etc/nginx/sites-enabled

RUN         cp -f   ${PROJECT_DIR}/.config/${BUILD_MODE}/supervisor.conf \
                    /etc/supervisor/conf.d/

CMD         supervisord -n