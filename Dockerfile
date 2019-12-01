FROM python:3.7.5-buster
EXPOSE 8000
WORKDIR /app
ADD . /app
RUN python -m pip install --upgrade pip
RUN python3 -m pip install wheel
RUN python3 -m pip install pipenv
RUN pipenv install --ignore-pipfile
