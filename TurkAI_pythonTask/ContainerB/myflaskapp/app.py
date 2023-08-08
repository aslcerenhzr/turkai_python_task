from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# PostgreSQL bağlantısı
conn = psycopg2.connect(
    database="mydb",
    user="turkai",
)

@app.route("/")
def index():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rednotice_db ")
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run()
