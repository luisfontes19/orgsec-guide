FROM python:3.12-alpine

RUN apk update
RUN apk add nodejs-current npm git bash cairo-dev curl
RUN npm install -g markdownlint-cli2 && true
RUN curl -1sLf 'https://dl.cloudsmith.io/public/task/task/setup.alpine.sh' | bash
RUN apk add task

ENTRYPOINT ["tail", "-f", "/dev/null"]

