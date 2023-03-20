FROM python:3.6-alpine

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

RUN apk add --no-cache libffi-dev build-base

COPY requirements.txt /usr/src/app/

RUN pip3 install --upgrade pip

RUN pip3 install wheel

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]

