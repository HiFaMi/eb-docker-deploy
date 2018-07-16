FROM            hifami/fc-eb-docker:base
MAINTAINER      rlaalsrbgk@gmail.com

ENV             BUILD_MODE              production
ENV             DJANGO_SETTINGS_MODULE  config.settings.${BUILD_MODE}

COPY            .       /srv/project
ENV             PROJECT_DIR             /srv/project
RUN             mkdir /var/log/django


RUN         cp -f   ${PROJECT_DIR}/.config/${BUILD_MODE}/nginx.conf \
                    /etc/nginx/nginx.conf && \

            cp -f   ${PROJECT_DIR}/.config/${BUILD_MODE}/nginx_app.conf \
                    /etc/nginx/sites-available/ && \

#            rm -rf  /etc/nginx/sites-enabled/* && \


            ln -sf  /etc/nginx/sites-available/nginx_app.conf \
                    /etc/nginx/sites-enabled

RUN         cp -f   ${PROJECT_DIR}/.config/${BUILD_MODE}/supervisor.conf \
                    /etc/supervisor/conf.d/
# 7000번 포트
EXPOSE      7000

CMD         supervisord -n