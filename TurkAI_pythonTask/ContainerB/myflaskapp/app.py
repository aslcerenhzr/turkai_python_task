from flask import Flask, render_template
import psycopg2
from datetime import datetime
import pytz

# Türkiye saat dilimini ayarla
turkey_timezone = pytz.timezone('Europe/Istanbul')

app = Flask(__name__)
current_time = datetime.now(tz=turkey_timezone).strftime("%Y-%m-%d %H:%M:%S")
# PostgreSQL bağlantısı
connection = psycopg2.connect(
    dbname="mydb",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

pg_cursor = connection.cursor()

@app.route("/")
def index():
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM rednotice_db ")
    data = cursor.fetchall()
    connection.commit()
    cursor.close()
    return render_template("index.html", data=data, current_time=current_time)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
