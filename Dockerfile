FROM pypy

LABEL version="1.0"
MAINTAINER Carlos Martin <carlosvin@gmail.com>

WORKDIR isbn_service
ADD . .

RUN pip install -r requirements.txt

RUN pypy3 -m unittest discover test "*_test.py"

ENTRYPOINT gunicorn rest.srv
