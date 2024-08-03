FROM python:3.9 as BASE

COPY . .

RUN pip install -r requirements.txt && python setup.py sdist
RUN pip install --upgrade pip

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

LABEL version="0.1.0"

# RUN pip install -U "celery[redis]"

# Setup FS
WORKDIR /
RUN mkdir -p /app/config
RUN mkdir -p /app/tests
RUN mkdir -p /app/dist

COPY requirements.txt /app/requirements.txt
COPY --from=BASE dist/ /app/dist/

RUN mkdir -p /var/log/pdf_generator/ && \
    pip install -r /app/requirements.txt && \
    pip install /app/dist/pdf_generator* && \
    rm -r /app/dist/*
