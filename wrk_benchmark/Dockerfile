FROM python:3.11-slim

WORKDIR /app

RUN apt update && apt install -y wrk

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "benchmark_runner.py"]
