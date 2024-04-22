FROM python:3.12

RUN pip3 install poetry 

WORKDIR /app
VOLUME ["/app"]
COPY . .

EXPOSE 8000

RUN poetry install 
