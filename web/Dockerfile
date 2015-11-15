FROM google/dart

MAINTAINER Carlos Martin <carlosvin@gmail.com>

WORKDIR /tmp

ADD . .

RUN pub upgrade
RUN pub build --mode=release --all --output=/usr/share/isbn/

#RUN ls -la /usr/share/isbn/

#RUN find /usr/share/isbn/ -type d -exec chmod +rx {} \;




