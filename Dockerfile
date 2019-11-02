FROM python:3

ADD ping.py /
ADD img.png /

RUN pip install pypng

CMD [ "python", "./ping.py" ]