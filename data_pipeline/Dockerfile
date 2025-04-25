FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y curl gnupg2 unixodbc-dev gcc g++ && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
    pip install pandas pyodbc psycopg2-binary requests

WORKDIR /app
COPY . /app

CMD ["python", "load_sqlserver.py"]
