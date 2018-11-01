FROM python:2.7.14-alpine3.7

ENV DJANGO_PRODUCTION=false
ENV PYTHONUNBUFFERED 1

EXPOSE 80

RUN mkdir -p /app/static
WORKDIR /app

RUN apk add --no-cache build-base curl-dev libcurl mariadb-dev tzdata
RUN cp /usr/share/zoneinfo/America/Los_Angeles /etc/localtime
RUN echo "America/Los_Angeles" > /etc/timezone

ADD requirements.txt /app/
RUN pip install -Ur requirements.txt

ADD . /app/

RUN /app/manage.py collectstatic --noinput

CMD ["gunicorn","tbpsite.wsgi", "-b", ":80"]
