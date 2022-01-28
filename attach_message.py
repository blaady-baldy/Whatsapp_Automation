from cgitb import text
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from example import return_path
from time import sleep
import os

class attach_message:
    def __init__(self, excel_data,name_column,contact_column):

        self.excel_data = excel_data
        self.name_column = name_column
        self.contact_column = contact_column

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://web.whatsapp.com')

        count = 0

        text_path = return_path("message_filepath")
        text_file = open(text_path, "r")
        message = text_file.read()
        text_file.close()
        

        for column in excel_data['Contact'].tolist():
            try:
                name = message.replace("$$$$$$",str(excel_data[name_column][count]))
                url = 'https://web.whatsapp.com/send?phone=' + str(excel_data[contact_column][count]) + '&text=' + name
                sent = False

                sleep(2)

                driver.get(url)

                # input("Press ENTER after login into Whatsapp Web and your chats are visiable.")
                try:
                    click_btn = WebDriverWait(driver, 35).until(
                        EC.element_to_be_clickable((By.CLASS_NAME, '_4sWnG')))

                except Exception as e:
                    print("Sorry message could not sent to " + str(excel_data[contact_column][count]))
                else:
                    sleep(2)
                    # click_btn.click()
                    click_btn.click()
                    sent = True
                    # sleep(2)
                    print('Message sent to: ' + str(excel_data[contact_column][count]))
                    count = count + 1
                
            except Exception as e:
                print('Failed to send message to ' + str(excel_data[contact_column][count]) + str(e))
        driver.quit()
        print("The script executed successfully.")