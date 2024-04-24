FROM python:3.12

RUN pip3 install poetry 

WORKDIR /app

COPY . .

RUN poetry install 

EXPOSE 8000

