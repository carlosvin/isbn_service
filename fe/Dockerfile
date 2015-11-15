FROM google/dart

MAINTAINER Carlos Martin <carlosvin@gmail.com>

WORKDIR /tmp

ADD . .

RUN pub get
RUN pub build --mode=release --all --output=/usr/share/fe

WORKDIR /usr/share/fe
RUN chmod 701 .



