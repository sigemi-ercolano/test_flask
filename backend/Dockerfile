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

RUN mkdir -p /opt/services/flaskapp/src 
COPY requirements.txt /opt/services/flaskapp/src/
WORKDIR /opt/services/flaskapp/src
RUN pip install -r requirements.txt

# Copia il codice dell'applicazione
COPY . /opt/services/flaskapp/src

# Imposta i permessi appropriati per l'utente non root
RUN chown -R myuser:myuser /opt/services/flaskapp/src

# Commuta a un utente non root
USER myuser

EXPOSE 5090

CMD ["python", "app.py"]
