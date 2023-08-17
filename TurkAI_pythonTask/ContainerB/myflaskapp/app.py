from flask import Flask, render_template
import psycopg2
from datetime import datetime


app = Flask(__name__)

# PostgreSQL bağlantısı
connection = psycopg2.connect(
    dbname="mydb",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

pg_cursor = connection.cursor()

# Tabloyu seç
pg_cursor.execute("SELECT * FROM rednotice_db;")
table_data = pg_cursor.fetchall()
# Sütun isimlerini al
column_names = [desc[0] for desc in pg_cursor.description]
# Sütun isimlerini yazdır
print(column_names, flush=True)
# Verileri yazdır
for row in table_data:
    print(row, flush=True)


@app.route("/")
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM rednotice_db ")
    data = cursor.fetchall()
    connection.commit()
    cursor.close()
    return render_template("index.html", data=data, current_time=current_time)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
