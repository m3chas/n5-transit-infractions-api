# Dockerfile
FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=app
ENV FLASK_ENV=development
ENV DATABASE_URL=postgresql://n5_test:n5_test_password@db:5432/n5_test_db
ENV JWT_SECRET_KEY=n5_jwt_secret

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
