from cgitb import text
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from example import return_path
from time import sleep

class attach_pdf:
    def __init__(self, excel_data,contact_column):

        self.excel_data = excel_data
        self.contact_column = contact_column

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://web.whatsapp.com')

        pdf_path = return_path("pdf_filepath")
        
        count = 0
        # input("Press ENTER after login into Whatsapp Web and your chats are visiable.")

        for column in excel_data['Contact'].tolist():
            try:
                url = 'https://web.whatsapp.com/send?phone=' + str(excel_data[contact_column][count]) 
                sent = False

                # It tries 3 times to send a message in case if there any error occurred
                sleep(2)

                driver.get(url)
                try:
                    click_btn = WebDriverWait(driver, 35).until(
                        EC.element_to_be_clickable((By.XPATH, '//div[@title="Attach"]')))

                    click_btn.click()

                    pdf_box = driver.find_element(By.XPATH,'//input[@accept="*"]')
                    pdf_box.send_keys(pdf_path)
                    
                    sleep(2)
                    send_button = driver.find_element(By.XPATH, '//div[@class="_165_h _2HL9j"]')
                    # send_button.click()
                    

                except Exception as e:
                    print("Sorry message could not sent to " + str(excel_data[contact_column][count]))
                else:
                    # click_btn.click()
                    send_button.click()
                    sent = True
                    # sleep(2)
                    print('Pdf file sent to: ' + str(excel_data[contact_column][count]))

                count = count + 1
                
            except Exception as e:
                print('Failed to send pdf file to ' + str(excel_data[contact_column][count]) + str(e))
        driver.quit()
        print("The script executed successfully.")