FROM python:3.12

RUN pip3 install poetry 

WORKDIR /app
VOLUME ["/app"]
COPY . .

EXPOSE 8080

RUN poetry install 

CMD python manage.py runserver 0.0.0.0:8000