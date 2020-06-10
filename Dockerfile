# Modified from Dockerfile example at hub.docker.com/_/python/
FROM python:3

WORKDIR /usr/src/project_euler/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install . --no-deps
