import psycopg2

connection = psycopg2.connect(
    database="mydb",
    user="turkai",
) 
    
with open("/home/turkai/Desktop/turkai_python_task/TurkAI_pythonTask/ContainerA/redNotices_data.txt", "r") as file:
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM rednotice_db;")
    
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split(", ")
        name = parts[0].split(": ")[1]
        age = parts[1].split(": ")[1].split(" years")[0]
        nationality = parts[2].split(": ")[1]
        
        insert_query = f"INSERT INTO rednotice_db (namesurname, age, nationalities) VALUES ('{name}', {age}, '{nationality}');"
        
        with connection.cursor() as cursor:
            cursor.execute(insert_query)
        
        connection.commit()
        
connection.close()
