FROM python:3.11-alpine

WORKDIR /app

COPY app.py .

RUN pip install flask

EXPOSE 80

CMD ["python", "app.py"]