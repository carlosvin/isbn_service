FROM httpd:2.4

#FROM google/dart

MAINTAINER Carlos Martin <carlosvin@gmail.com>

# Enable HTTPS for apt.
RUN apt-get update
RUN apt-get install apt-transport-https
# Get the Google Linux package signing key.
RUN sh -c 'curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -'
# Set up the location of the stable repository.
RUN sh -c 'curl https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list > /etc/apt/sources.list.d/dart_stable.list'
RUN apt-get update
RUN apt-get install dart
WORKDIR /tmp
ADD . .
RUN pub upgrade
RUN pub build --mode=release --all --output=/usr/share/isbn/
