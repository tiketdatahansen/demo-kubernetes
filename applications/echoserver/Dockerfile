FROM python:3.8.18-slim
WORKDIR /app

RUN pip install --no-cache-dir fastapi==0.109.2 uvicorn==0.27.1 requests==2.28.2
COPY app .

ENTRYPOINT ["uvicorn", "main:app"]
CMD ["--host", "0.0.0.0", "--port", "8000"]
