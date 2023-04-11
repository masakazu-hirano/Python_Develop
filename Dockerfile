# $ docker build --tag 'Docker イメージ名':latest --no-cache .
# $ docker run --name 'Docker コンテナ名':latest --volume 'ホストOS':/usr/local/src --interactive --tty --detach --rm 'Docker イメージ名':latest

FROM python:3.11.3

COPY ./src /usr/local/src
WORKDIR /usr/local/src

RUN apt-get update \
    && apt-get install -y libgl1-mesa-dev

RUN pip install --upgrade pip \
    && pip install -r requirements.txt
