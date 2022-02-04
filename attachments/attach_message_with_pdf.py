from cgitb import text
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from example import return_path
from time import sleep
from fetch_number import fetch_number
import os

class attach_message_with_pdf:
    def __init__(self, excel_data,name_column,contact_column):

        self.excel_data = excel_data
        self.name_column = name_column
        self.contact_column = contact_column

        print("Do you want to include name in message to be sent ? (0 - NO / 1 - Yes)")
        isName = int(input("Choice : "))
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://web.whatsapp.com')

        pdf_path = return_path("pdf_filepath")

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

                sleep(2)

                driver.get(url)

                try:
                    # msg_btn = driver.find_element(By.CLASS_NAME,'_4sWnG').click()
                    # sleep(2)

                    click_btn = WebDriverWait(driver, 35).until(
                        EC.element_to_be_clickable((By.XPATH, '//div[@title="Attach]')))
                    
                    sleep(2)
                    click_btn.click()
                    message_btn = driver.find_element(By.XPATH, '//div[@title="Attach]').click()

                    pdf_box = driver.find_element(By.XPATH,'//input[@accept="*"]')
                    pdf_box.send_keys(pdf_path)
                    
                    sleep(2)
                    send_button = driver.find_element(By.XPATH, '//div[@class="_165_h _2HL9j"]')

                except Exception as e:
                    print("Sorry message could not sent to " + num)
                else:
                    sleep(2)
                    send_button.click()
                    sent = True
                    # sleep(2)
                    print(count + '. Message sent to: ' + num)
                    count = count + 1
                
            except Exception as e:
                print('Failed to send message to ' + num + str(e))
        driver.quit()
        print("The script executed successfully.")

    