FROM pypy

LABEL version="1.0"
MAINTAINER Carlos Martin <carlosvin@gmail.com>

WORKDIR /isbn_service
ADD . .
RUN chmod +x ./test.sh
RUN pip install -r requirements.txt

ENTRYPOINT gunicorn rest.srv
