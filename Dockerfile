FROM python:3.7.5-alpine3.10
MAINTAINER Fabian Affolter <fabian@affolter-engineering.ch>
ENV PS1="\[\e[0;33m\]|> penin <| \[\e[1;35m\]\W\[\e[0m\] \[\e[0m\]# "

WORKDIR /src
COPY . /src
RUN pip install --no-cache-dir -r requirements.txt \
    && python setup.py install
WORKDIR /
ENTRYPOINT ["penin"]
