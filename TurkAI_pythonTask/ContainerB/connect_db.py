import pika
import psycopg2


def process_data(data):
    # Implement this function to process the data and return processed_data
    # For now, let's assume it just returns the data as-is
    return data

def process_queue(channel, method, properties, body):
    try:
        data = body.decode('utf-8')
        print("Received data:", data)  # Debug print
        processed_data = process_data(data)  # Veriyi işleyerek istenen formata dönüştür
        print("Processed data:", processed_data)  # Debug print
        
        save_to_database(processed_data)  # Veritabanına kaydet
        
        channel.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print("Error processing message:", e)

def save_to_database(data):
    connection = psycopg2.connect(
        database="mydb",
        user="turkai",
    )
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO rednotice_db (namesurname, age, nationalities) VALUES (%s, %s, %s);",
                           (data['name'], data['age'], data['nationality']))
        
        connection.commit()
    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        connection.close()

# Kuyruğa bağlan
connection = pika.BlockingConnection(pika.ConnectionParameters(host='container_c', virtual_host='/', credentials=pika.PlainCredentials('guest', 'guest')))
channel = connection.channel()
channel.queue_declare(queue='interpol_queue', durable=True)

# Kuyruğu dinle ve verileri işle
try:
    channel.basic_consume(queue='interpol_queue', on_message_callback=process_queue)
    print("Waiting for messages. To exit, press CTRL+C")
    channel.start_consuming()
finally:
    connection.close()
