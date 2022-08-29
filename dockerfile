FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./src /app

ENTRYPOINT ["python"]

CMD ["main.py"]