FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
RUN apt-get update && \
    apt-get install -y vim && \
    apt-get install -y cron && \
    apt-get -y install tesseract-ocr
WORKDIR /ocrproject
COPY requirements.txt /ocrproject/
RUN pip install -r requirements.txt
COPY . /ocrproject/


CMD gunicorn ocrproject.wsgi:application --timeout 60 --keep-alive 5 --log-level debug --bind 0.0.0.0:$PORT

