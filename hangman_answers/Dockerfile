FROM python:3.8.2-alpine

RUN mkdir /app
WORKDIR /app

COPY . .
RUN apk add curl && pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "app.py"]
