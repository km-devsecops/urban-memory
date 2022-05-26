FROM python:3.9-alpine

ENV FLASK_APP=app
ENV FLASK_ENV=development

COPY app /app

WORKDIR /app

RUN pip install -r requirements.txt

#RUN flask init-db

# Unit tests
# RUN pip install pytest && pytest

EXPOSE 5000

CMD [ "python", "run.py", "--host=0.0.0.0" ]