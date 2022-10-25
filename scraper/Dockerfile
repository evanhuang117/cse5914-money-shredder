# syntax=docker/dockerfile:1
FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apk --no-cache add gcc musl-dev
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "scraper.py" ]