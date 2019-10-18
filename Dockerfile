FROM python:3.6
MAINTAINER dima117

RUN pip install Eve 
ADD evemain.py .
RUN python evemain.py
RUN --no-debugger
