import pika
import psycopg2 

i = 0  # Counter to keep track of processed messages

# Callback function to process messages from RabbitMQ
def callback(ch, method, properties, body):
    global i
    
    # Convert the message body into a Python dictionary
    data = eval(body)
    name = data.get("Name")
    age = data.get("Age")
    nationality = data.get("Nationalities")
    
    i += 1
    if i == 20:
        ch.stop_consuming()  # Stop consuming messages after processing 20
    
    # Insert data into PostgreSQL database
    pg_cursor.execute("INSERT INTO rednotice_db (namesurname, age, nationalities) VALUES (%s, %s, %s);",
                      (name, age, nationality))
    connection.commit()

# Establish connection to PostgreSQL
connection = psycopg2.connect(
    dbname="mydb",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

# Create a cursor for executing SQL commands
pg_cursor = connection.cursor()

# Create the 'rednotice_db' table if it doesn't exist
pg_cursor.execute("CREATE TABLE IF NOT EXISTS rednotice_db (ID SERIAL PRIMARY KEY, namesurname VARCHAR(100), age VARCHAR(100), nationalities VARCHAR(100));")
connection.commit()

# Establish connection to RabbitMQ
rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters('container_c'))
channel = rabbitmq_connection.channel()

# Declare the 'interpol_queue'
channel.queue_declare(queue='interpol_queue', durable=True)

# Start consuming messages from the RabbitMQ queue
channel.basic_consume(queue='interpol_queue', on_message_callback=callback, auto_ack=True)

# Begin consuming messages until the callback stops it or all messages are processed
channel.start_consuming()

# Close connections
rabbitmq_connection.close()
pg_cursor.close()
connection.close()