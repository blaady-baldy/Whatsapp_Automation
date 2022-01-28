from cgitb import text
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class attach_media:
    def __init__(self, excel_data):

        self.excel_data = excel_data

        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get('https://web.whatsapp.com')

        media_path = input("Enter the file path for the media file to be attached : ")
        
        count = 0
        input("Press ENTER after login into Whatsapp Web and your chats are visiable.")

        for column in excel_data['Contact'].tolist():
            try:
                url = 'https://web.whatsapp.com/send?phone=' + str(excel_data['Contact'][count]) 
                sent = False

                sleep(2)

                driver.get(url)
                try:
                    click_btn = WebDriverWait(driver, 35).until(
                        EC.element_to_be_clickable((By.XPATH, '//div[@title="Attach"]')))

                    # sleep(5)

                    click_btn.click()

                    # sleep(5)

                    pdf_box = driver.find_element(By.XPATH,'//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                    pdf_box.send_keys(media_path)

                    sleep(2)

                    send_button = driver.find_element(By.XPATH, '//div[@class="_165_h _2HL9j"]')
                    # send_button.click()

                except Exception as e:
                    print("Sorry message could not sent to " + str(excel_data['Contact'][count]))
                else:
                    # sleep(5)
                    # click_btn.click()
                    # sleep(2)
                    send_button.click()
                    sent = True
                    sleep(2)
                    print('Media file sent to: ' + str(excel_data['Contact'][count]))

                count = count + 1
                
            except Exception as e:
                print('Failed to send media file to ' + str(excel_data['Contact'][count]) + str(e))
                sleep(5)
        driver.quit()
        print("The script executed successfully.")