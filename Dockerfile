FROM python:3.11-slim
WORKDIR /app
COPY automation.py .
CMD ["python", "automation.py"]
