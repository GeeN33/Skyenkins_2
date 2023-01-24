FROM python:alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app


RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

