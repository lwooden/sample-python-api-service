FROM python:slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "3000"]