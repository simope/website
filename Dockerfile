FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
COPY . /app/
COPY ./requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python3 manage.py collectstatic --noinput
RUN chmod +x scripts/start.sh
ENTRYPOINT [ "sh", "-c", "./scripts/start.sh" ]