FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED True
WORKDIR /app
RUN pip3 install pipenv
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --deploy --ignore-pipfile
COPY . .
CMD pipenv run start
