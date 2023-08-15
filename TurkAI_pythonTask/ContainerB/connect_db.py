import pika
import psycopg2

def callback(ch, method, properties, body):
    data = eval(body)  # Gönderilen veriyi bir sözlüğe dönüştür
    name = data.get("Name")
    age = data.get("Age")
    nationality = data.get("Nationalities")
    
    # PostgreSQL'e veri ekleme
    pg_cursor.execute("INSERT INTO rednotice_db (namesurname, age, nationalities) VALUES (%s, %s, %s);",
                           (name, age, nationality))
    connection.commit()
    
try:
    # RabbitMQ bağlantısı
    rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters('container_c'))
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

    create_table_query = '''CREATE TABLE rednotice_db (
        id SERIAL PRIMARY KEY,
        namesurname VARCHAR(100),
        age VARCHAR(100),
        nationalities VARCHAR(100),
        olusturma_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    '''
    pg_cursor.execute(create_table_query)
    connection.commit()
    
    channel.basic_consume(queue='interpol_queue', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
    
finally:
    if connection:
        connection.close()
    if rabbitmq_connection:
        rabbitmq_connection.close()