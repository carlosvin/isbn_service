FROM pypy

MAINTAINER Carlos Martin <carlosvin@gmail.com>

WORKDIR /isbn_service

ADD src/ .

RUN pip install -r requirements.txt

EXPOSE  8000

ENTRYPOINT gunicorn rest.srv
