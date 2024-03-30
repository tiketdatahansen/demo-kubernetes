FROM python:3.8.18-slim
WORKDIR /app

RUN pip install --no-cache-dir kafka-python==2.0.2
COPY app .

ENTRYPOINT ["python", "producer.py"]
