FROM python:3.10-slim-buster

WORKDIR /python-docker
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["pip", "install", "-e", "."]
CMD ["flask", "--app", "gameshop", "run", "--host=0.0.0.0"]