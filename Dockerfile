FROM python:3.5.6-slim

EXPOSE 8080

RUN mkdir -p /var/app
WORKDIR /var/app

ADD requirements.txt /var/app
RUN pip install -r requirements.txt

ADD . .

CMD python manage.py runserver 0.0.0.0:8080
