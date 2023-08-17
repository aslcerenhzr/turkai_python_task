from flask import Flask, render_template
import psycopg2

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
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM rednotice_db ")
    data = cursor.fetchall()
    connection.commit()
    cursor.close()
    return render_template("templates/index.html", data=data)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
