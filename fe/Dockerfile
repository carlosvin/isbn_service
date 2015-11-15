FROM google/dart

MAINTAINER Carlos Martin <carlosvin@gmail.com>

WORKDIR /usr/share/fe/src

ADD . .

RUN pub get
RUN pub build
RUN ls
RUN mv build/web/* /usr/share/fe

WORKDIR /usr/share/fe
RUN rm -rf src
RUN chmod 701 /usr/share/fe



