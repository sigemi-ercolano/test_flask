# backend/Dockerfile
FROM python:3.12-slim-bullseye

# Installa i pacchetti necessari per ODBC e il driver ODBC per SQL Server
RUN apt-get update \
    && apt-get install -y unixodbc unixodbc-dev \
    && apt-get install -y odbcinst \
    && apt-get install -y g++ \
    && apt-get install -y curl gnupg
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
# Crea un utente non root per eseguire l'applicazione
RUN adduser --disabled-password --gecos '' myuser

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice dell'applicazione
COPY app.py .

# Imposta i permessi appropriati per l'utente non root
RUN chown -R myuser:myuser /app

# Commuta a un utente non root
USER myuser

CMD ["python", "app.py"]
