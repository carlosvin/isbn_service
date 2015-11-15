FROM pypy

MAINTAINER Carlos Martin <carlosvin@gmail.com>

WORKDIR /isbn_service

ADD src/ .

RUN pip install -r requirements.txt

ENTRYPOINT gunicorn rest.srv
