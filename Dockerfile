FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /code
RUN apt-get -y update && apt-get install -y npm
RUN npm update npm && npm install -g @vue/cli && \
    npm install -g @vue/cli-init
COPY requirements.txt /code/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
ADD . /code/
