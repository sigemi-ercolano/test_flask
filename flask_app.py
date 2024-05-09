from flask import Flask, redirect, request, render_template, url_for
import pyodbc

app = Flask(__name__)

# Connessione al database MSSQL
conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=localhost;'
    r'DATABASE=test_db;'
    r'UID=sa;'
    r'PWD=yourStrongPassword!1'
)


print('Connecting to SQL Server...')

db_connection = pyodbc.connect(conn_str)


@app.route('/')
def index():
    return render_template('front-end/index.html')

@app.route('/front-end/submit_data')
def submit_data_form():
    return render_template('front-end/submit_data.html')


@app.route('/submit_all_data', methods=['POST'])
def submit_data():
    data = request.json  # Assume che il frontend invii i dati come JSON
    
    # Esegui l'inserimento dei dati nel database
    cursor = db_connection.cursor()
    query = "INSERT INTO table_test (username, surname) VALUES (?, ?)"
    values = (data['value1'], data['value2'])
    cursor.execute(query, values)
    db_connection.commit()
    cursor.close()
    return '/front-end/show_data'



@app.route('/front-end/show_data')
def show_data():
    # Esegui la query per ottenere tutti i dati dal database
    cursor = db_connection.cursor()
    query = "SELECT * FROM table_test"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    # Passa i dati al template HTML per la visualizzazione
    return render_template('front-end/show_data.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
