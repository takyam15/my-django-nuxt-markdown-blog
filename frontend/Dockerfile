FROM node:16
ENV WORKDIR /code
WORKDIR /code
RUN npm update npm && npm install -g @vue/cli && \
    npm install -g @vue/cli-init
ADD . /code/
