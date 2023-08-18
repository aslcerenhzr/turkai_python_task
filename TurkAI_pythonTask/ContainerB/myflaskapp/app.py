from flask import Flask, render_template
import psycopg2
from datetime import datetime
import pytz

# Initialize the Flask app
app = Flask(__name__)

# Get the current time in the Turkey timezone
turkey_timezone = pytz.timezone('Europe/Istanbul')
current_time = datetime.now(tz=turkey_timezone).strftime("%Y-%m-%d %H:%M:%S")

# Establish connection to PostgreSQL
connection = psycopg2.connect(
    dbname="mydb",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

# Define a route for the index page
@app.route("/")
def index():
   # Create a cursor for executing SQL commands
    cursor = connection.cursor()
    
    # Execute an SQL query to fetch data from the 'rednotice_db' table
    cursor.execute("SELECT * FROM rednotice_db")
    data = cursor.fetchall()
    
    # Commit the transaction and close the cursor
    connection.commit()
    cursor.close()
    
    # Render the 'index.html' template and pass the data and current_time
    return render_template("index.html", data=data, current_time=current_time)

# Run the Flask app if this script is executed directly
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
