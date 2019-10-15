FROM python:latest
MANTAINER dima117

RUN pip install Eve 
ADD evemain.py 
RUN python evemain.py
