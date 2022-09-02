FROM --platform=linux/amd64 python:3.10

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./src /app

EXPOSE 3000

ENTRYPOINT ["python"]

CMD ["api.py"]