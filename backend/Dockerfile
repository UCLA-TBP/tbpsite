FROM python:2.7.14-alpine3.7

ENV DJANGO_PRODUCTION=false
ENV PYTHONUNBUFFERED 1

#RUN apk add --no-cache libpq postgresql-dev build-base zlib-dev jpeg-dev tiff-dev freetype-dev lcms-dev libwebp-dev py-boto

RUN mkdir /logs
RUN mkdir /logs/gunicorn

EXPOSE 80


WORKDIR /app

RUN apk add --no-cache build-base curl-dev libcurl mariadb-dev

ADD requirements.txt /app/
RUN pip install -Ur requirements.txt
#RUN sh -c "cat requirements.txt | xargs -n 1 pip install "

ADD . /app/

RUN /app/manage.py collectstatic --noinput

CMD ["gunicorn","tbpsite.wsgi", "-b", ":80"]
