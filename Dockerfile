FROM python:3.8.3-alpine as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev tiff-dev libjpeg-turbo-dev gdal-dev geos-dev

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

#ENTRYPOINT ["/app/entrypoint_two.sh"]