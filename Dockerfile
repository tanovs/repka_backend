FROM python:3.10

WORKDIR /opt

RUN git clone https://github.com/tanovs/repka_backend.git

WORKDIR /opt/repka_backend


RUN apt-get update \
    && apt-get install -y netcat-traditional
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

EXPOSE 8080


CMD ["python3.10", "application/main.py"]