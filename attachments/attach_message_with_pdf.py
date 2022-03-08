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

class attach_message_with_pdf:
    def __init__(self, excel_data,name_column,contact_column,choice_for_name):

        self.excel_data = excel_data
        self.name_column = name_column
        self.contact_column = contact_column
        self.choice_for_name = choice_for_name
        isName = choice_for_name

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://web.whatsapp.com')

        pdf_path = return_path("pdf_filepath")

        count = 0

        message = return_path("message")

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

                    media_box = driver.find_element(By.XPATH,'//input[@accept="*"]')
                    media_box.send_keys(pdf_path)

                    sleep(2)
                    send_button = driver.find_element(By.XPATH, '//div[@class="_165_h _2HL9j"]')

                except Exception as e:
                    print("Sorry pdf file could not be sent to : " + num)
                else:
                    send_button.click()
                    msg_btn = driver.find_element(By.CLASS_NAME, '_4sWnG')
                    msg_btn.click()
                    sent = True
                    sleep(4)
                    print(str(count+1) + '. Pdf file sent to: ' + num)
                    count = count + 1
                
            except Exception as e:
                print('Failed to send message to ' + num + str(e))
        driver.quit()
        print("The script executed successfully.")

    