FROM python:38

WORKDIR /code

ADD . /code/

ADD requirements.txt /code/

RUN pip install -r requirements.txt

WORKDIR /code

EXPOSE 80 22

CMD ["supervisord", "-n"]