import pika
import psycopg2

i=0 

def callback(ch, method, properties, body):

    global i 
    
    data = eval(body)  # Gönderilen veriyi bir sözlüğe dönüştür
    name = data.get("Name")
    age = data.get("Age")
    nationality = data.get("Nationalities")
    
    # Gelen veriyi print et
    print("Received Data:", flush=True)
    print("Name:", name, flush=True)
    print("Age:", age, flush=True)
    print("Nationality:", nationality, flush=True)
    
    i+=1
    if i==20:
        ch.stop_consuming()     
        
    # PostgreSQL'e veri ekleme
    pg_cursor.execute("INSERT INTO rednotice_db (namesurname, age, nationalities) VALUES (%s, %s, %s);",
                           (name, age, nationality))
    connection.commit()

# PostgreSQL bağlantısı
connection = psycopg2.connect(
    dbname="mydb",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
pg_cursor = connection.cursor()
pg_cursor.execute("CREATE TABLE IF NOT EXISTS rednotice_db (namesurname VARCHAR(100), age VARCHAR(100), nationalities VARCHAR(100));")
connection.commit()

# RabbitMQ bağlantısı
rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters('container_c'))
channel = rabbitmq_connection.channel()
channel.queue_declare(queue='interpol_queue', durable=True)
channel.basic_consume(queue='interpol_queue', on_message_callback=callback, auto_ack=True)


print("Start consuming messages...")
channel.start_consuming()

print("Finished consuming messages.")
rabbitmq_connection.close()
pg_cursor.close()
connection.close()
