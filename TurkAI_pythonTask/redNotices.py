from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def findRedNotices():
    browser = webdriver.Chrome() 
    browser.get("https://www.interpol.int/How-we-work/Notices/Red-Notices/View-Red-Notices")
    time.sleep(1)
    
    redNotices_name = browser.find_elements(By.CLASS_NAME, "redNoticeItem__labelLink")
    redNotices_ages = browser.find_elements(By.CLASS_NAME, "age")
    redNotices_nationalities = browser.find_elements(By.CLASS_NAME, "nationalities")
    
    list = zip(redNotices_name, redNotices_ages,redNotices_nationalities)
    
    for name_element, age_element, nation_element in list:
        with open("/home/turkai/Desktop/asliceren/basics/redNotices_data.txt", "a", encoding="utf-8") as file:
            file.write(f"Name: {name_element.text}, Age: {age_element.text}, Nationalities: {nation_element.text}\n")  
    
    browser.quit()
    
with open("/home/turkai/Desktop/asliceren/basics/redNotices_data.txt", 'w') as file:
    file.write('')   
findRedNotices()