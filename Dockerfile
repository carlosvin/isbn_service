FROM pypy

LABEL version="1.0"
MAINTAINER Carlos Martin <carlosvin@gmail.com>

ADD . .

ENTRYPOINT gunicorn rest.srv
