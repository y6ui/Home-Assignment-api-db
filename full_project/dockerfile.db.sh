FROM python:3.10-slim
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get install -y curl wget

COPY . .
EXPOSE 5000

CMD ["python", "database/database_handaling.py"]

