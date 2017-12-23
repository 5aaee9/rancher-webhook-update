FROM python:3.6-alpine

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "main.py"]
