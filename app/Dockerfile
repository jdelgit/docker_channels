FROM python:3.6-alpine3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
COPY ./channelsproject/ /src/
RUN apk update && \
    apk upgrade && \
    apk add bash
RUN apk add build-base
WORKDIR /src
RUN pip3 install -r /src/requirements.txt
EXPOSE 9542

