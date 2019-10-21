FROM python:latest
MAINTAINER dima117

RUN pip install Eve 
ADD evemain.py .


