FROM python:3.7.0

WORKDIR /app

RUN pip install --no-cache-dir  Django==1.11.17
RUN pip install --no-cache-dir  django-crispy-forms==1.7.2


COPY . .

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
