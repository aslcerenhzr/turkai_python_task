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

@app.route("/")
def index():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM rednotice_db ")
    data = cursor.fetchall()
    connection.commit()
    cursor.close()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run()
