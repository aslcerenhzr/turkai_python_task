from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pika

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

def findRedNotices():
    browser = webdriver.Chrome(options=chrome_options) 
    browser.get("https://www.interpol.int/How-we-work/Notices/Red-Notices/View-Red-Notices")
    time.sleep(1)
    
    redNotices_data = []
    
    names = browser.find_elements(By.CLASS_NAME, "redNoticeItem__labelLink")
    ages = browser.find_elements(By.CLASS_NAME, "age")
    nationalities = browser.find_elements(By.CLASS_NAME, "nationalities")
    
    for name_element, age_element, nation_element in zip(names, ages, nationalities):
        name = name_element.text.replace("\n", "")
        age = age_element.text
        nationality = nation_element.text
        redNotices_data.append({"Name": name, "Age": age, "Nationalities": nationality})
    
    browser.quit()
    return redNotices_data

def send_to_rabbitmq(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='1303ef764b4a'))
    channel = connection.channel()
    channel.queue_declare(queue='interpol_queue', durable=True)
    
    for item in data:
        channel.basic_publish(exchange='',
                              routing_key='interpol_queue',
                              body=str(item),
                              properties=pika.BasicProperties(
                                  delivery_mode=2,  # Veriyi kalıcı olarak kuyruğa ekle
                              ))
        print(f"Veri kuyruğa eklendi: {item}")
    
    connection.close()

if __name__ == "__main__":
    redNotices_data = findRedNotices()
    send_to_rabbitmq(redNotices_data)