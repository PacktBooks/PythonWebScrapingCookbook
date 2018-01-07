FROM python:3
WORKDIR /usr/src/app

RUN pip install Flask-RESTful Elasticsearch Nameko

COPY api.py .

CMD ["python", "api.py"]