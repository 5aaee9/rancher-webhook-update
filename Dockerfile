FROM python:2.7.14-alpine3.7

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "main.py"]
