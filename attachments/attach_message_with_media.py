from cgitb import text
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from attachments.example import return_path
from time import sleep
from attachments.fetch_number import fetch_number
import os

class attach_message_with_media:
    def __init__(self, excel_data,name_column,contact_column):

        self.excel_data = excel_data
        self.name_column = name_column
        self.contact_column = contact_column

        print("Do you want to include name in message to be sent ? (0 - NO / 1 - Yes)")
        isName = int(input("Choice : "))
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://web.whatsapp.com')

        media_path = return_path("media_filepath")

        count = 0

        text_path = return_path("message_filepath")
        text_file = open(text_path, "r")
        message = text_file.read()
        text_file.close()
        

        for column in excel_data[contact_column].tolist():
            try:
                if isName : 
                    name = message.replace("($name$)",str(excel_data[name_column][count]))
                else :
                    name = message
                
                number = str(excel_data[contact_column][count])
                num = fetch_number(number)

                url = 'https://web.whatsapp.com/send?phone=' + num + '&text=' + name
                sent = False

                driver.get(url)
                sleep(2)

                try:
                    click_btn = WebDriverWait(driver, 35).until(
                        EC.element_to_be_clickable((By.XPATH, '//div[@title="Attach"]')))
                    click_btn.click()

                    media_box = driver.find_element(By.XPATH,'//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                    media_box.send_keys(media_path)

                    sleep(2)
                    send_button = driver.find_element(By.XPATH, '//div[@class="_165_h _2HL9j"]')

                except Exception as e:
                    print("Sorry media file could not be sent to : " + num)
                else:
                    send_button.click()
                    sent = True
                    sleep(4)
                    print(str(count+1) + '. Media file sent to: ' + num)
                    count = count + 1
                
            except Exception as e:
                print('Failed to send message to ' + num + str(e))
        driver.quit()
        print("The script executed successfully.")

    