from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pika

# Configure Chrome options for headless browsing
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

# Function to scrape data from Interpol's Red Notices page
def findRedNotices():
    
    # Initialize a Chrome WebDriver instance with the configured options
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://www.interpol.int/How-we-work/Notices/Red-Notices/View-Red-Notices")
    
    time.sleep(1)
    redNotices_data = []
    
    # Find elements containing information about individuals on the page
    names = browser.find_elements(By.CLASS_NAME, "redNoticeItem__labelLink")
    ages = browser.find_elements(By.CLASS_NAME, "age")
    nationalities = browser.find_elements(By.CLASS_NAME, "nationalities")
    
    # Iterate through the scraped data and create dictionaries for each individual
    for name_element, age_element, nation_element in zip(names, ages, nationalities):
        name = name_element.text.replace("\n", "")
        age = age_element.text
        nationality = nation_element.text
        redNotices_data.append({"Name": name, "Age": age, "Nationalities": nationality})
    
    browser.quit()
    
    return redNotices_data

# Function to send data to RabbitMQ queue
def send_to_rabbitmq(data):
    # Establish a connection to the RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='container_c'))
    channel = connection.channel()
    
    # Declare a queue named 'interpol_queue'
    channel.queue_declare(queue='interpol_queue', durable=True)
    
    # Publish each item of data to the RabbitMQ queue
    for item in data:
        channel.basic_publish(exchange='',
                              routing_key='interpol_queue',
                              body=str(item),
                              properties=pika.BasicProperties(
                                  delivery_mode=2,
                              ))
    
    connection.close()

if __name__ == "__main__":

    redNotices_data = findRedNotices()
    
    send_to_rabbitmq(redNotices_data)
