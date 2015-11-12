FROM pypy

LABEL version="1.0"
MAINTAINER Carlos Martin <carlosvin@gmail.com>

RUN pip install -r requirements.txt

WORKDIR /isbn_service
ADD . .
RUN pypy3 -m unittest discover test "*_test.py"

VOLUME ["/data"]
WORKDIR /data

ENTRYPOINT gunicorn /isbn_service/rest.srv
