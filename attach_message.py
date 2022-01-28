from cgitb import text
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from example import return_path
from time import sleep

class attach_message:
    def __init__(self, excel_data):

        self.excel_data = excel_data

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://web.whatsapp.com')

        text_path = return_path("message_filepath")
        text_file = open(text_path, "r")
        message = text_file.read()
        text_file.close()
        count = 0
        input("Press ENTER after login into Whatsapp Web and your chats are visiable.")

        for column in excel_data['Contact'].tolist():
            try:
                url = 'https://web.whatsapp.com/send?phone=' + str(excel_data['Contact'][count]) + '&text=' + message
                sent = False

                # It tries 3 times to send a message in case if there any error occurred

                driver.get(url)
                try:
                    click_btn = WebDriverWait(driver, 35).until(
                        EC.element_to_be_clickable((By.CLASS_NAME, '_4sWnG')))

                except Exception as e:
                    print("Sorry message could not sent to " + str(excel_data['Contact'][count]))
                else:
                    sleep(2)
                    # click_btn.click()
                    click_btn.click()
                    sent = True
                    sleep(2)
                    print('Message sent to: ' + str(excel_data['Contact'][count]))

                count = count + 1
                
            except Exception as e:
                print('Failed to send message to ' + str(excel_data['Contact'][count]) + str(e))
        driver.quit()
        print("The script executed successfully.")