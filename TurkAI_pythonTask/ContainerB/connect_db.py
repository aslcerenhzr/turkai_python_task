import pika
import psycopg2

# RabbitMQ bağlantısı
rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters('1303ef764b4a'))
channel = rabbitmq_connection.channel()
channel.queue_declare(queue='interpol_queue', durable=True)

# PostgreSQL bağlantısı
connection = psycopg2.connect(
    dbname="mydb",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
pg_cursor = connection.cursor()

def callback(ch, method, properties, body):
    data = eval(body)  # Gönderilen veriyi bir sözlüğe dönüştür
    name = data.get("Name")
    age = data.get("Age")
    nationality = data.get("Nationalities")
    
    # PostgreSQL'e veri ekleme
    pg_cursor.execute("INSERT INTO rednotice_db (namesurname, age, nationalities) VALUES (%s, %s, %s);",
                           (name, age, nationality))
    connection.commit()

channel.basic_consume(queue='interpol_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()
