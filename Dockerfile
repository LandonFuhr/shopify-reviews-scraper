FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED True
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:server