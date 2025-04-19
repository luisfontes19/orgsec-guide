FROM python:3.12-alpine

RUN apk update
RUN apk add nodejs-current npm git bash
RUN npm install -g markdownlint-cli2 && true

ENTRYPOINT ["tail", "-f", "/dev/null"]

