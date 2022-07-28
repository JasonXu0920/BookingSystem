FROM alpine:lastest

RUN apk add --no-cache python3-dev
RUN pip3 install --upgrade pip

WORKDIR /service

COPY . /service

RUN pip3 install -r requirements.txt

EXPOSE 5002

CMD demo/__init__.py