############################################################
# Dockerfile to build Factory Concepts container image
# Based on Debian 8
############################################################
FROM python:3.4.2


ENV PYTHONUNBUFFERED=1

RUN \
  curl -sL https://deb.nodesource.com/setup_6.x | bash - \
  && apt-get update \
  && apt-get install -y nodejs \
  && npm install -g babel-cli bower livescript \
  && apt-get -y autoremove \
  && apt-get -y autoclean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
COPY wheelhouse /tmp/wheelhouse
RUN pip install --find-links=file:///tmp/wheelhouse -r /tmp/requirements.txt \
  ; rm -rf /tmp/*

COPY . /app

EXPOSE 8080
CMD ["./runserver.sh"]
