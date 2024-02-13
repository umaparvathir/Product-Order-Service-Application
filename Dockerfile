FROM python:3.9.11

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python3","main.py"]