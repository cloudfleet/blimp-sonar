FROM debian:jessie

RUN apt-get update -y && apt-get install -y python-pip
ADD requirements.txt /opt/sonar/requirements.txt
RUN pip install -r requirements.txt

ADD . /opt/conduit
WORKDIR /opt/conduit

CMD /usr/bin/python -u sonar.py

EXPOSE 5000
