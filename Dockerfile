FROM python:3.6
MAINTAINER dima117

RUN pip install Eve 
ADD evemain.py .
ADD make_schema.py .
ADD my_schema.json .
ADD	my_settings.py .
ADD response1.json . 
CMD ["evemain.py", "run"]



