FROM python:alpine3.17

RUN mkdir /app

WORKDIR /app

ADD requirements.txt /app

RUN pip3 install -r requirements.txt

ADD . /app

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]