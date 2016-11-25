FROM google/dart

MAINTAINER Carlos Martin <carlosvin@gmail.com>

ENV SERVER /usr/share/nginx/www/
ENV OUTPUT /tmp/output

RUN apt-get update
RUN apt-get -y install nginx

WORKDIR /tmp
ADD pubspec.yaml .
ADD web web
RUN pub upgrade && pub build --mode=release --all --output=$OUTPUT
RUN mv $OUTPUT/web/* $SERVER

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
