FROM python:3.11.3-slim-buster AS main

WORKDIR /var/usr/app

COPY requirements.txt .

FROM main AS setup

RUN pip install -r requirements.txt

COPY . .

FROM setup AS run

CMD [ "python", "main.py" ]