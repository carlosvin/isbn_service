FROM google/dart

MAINTAINER Carlos Martin <carlosvin@gmail.com>

WORKDIR /tmp

ADD . .

RUN pub upgrade
RUN pub build --mode=release --all --output=/usr/share/isbn

RUN rm -rf *