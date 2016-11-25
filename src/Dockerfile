#FROM pypy:slim
FROM python:3-onbuild

MAINTAINER Carlos Martin <carlosvin@gmail.com>

ADD . /usr/isbn

#RUN pip install -r requirements.txt
EXPOSE 80 443

CMD ["gunicorn", "rest.srv", "-w2", "-b:80", "--pythonpath", "/usr/isbn"]
