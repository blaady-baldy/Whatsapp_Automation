# Program to send bulk messages through WhatsApp web from an excel sheet without saving contact numbers
# Author @inforkgodara



excel_data = pandas.read_excel('Recipients data.xlsx', sheet_name='Recipients')
filepath = "D:\python\Whatsapp_Text_Only/akriti.png" #the path of the file for attachment

count = 0

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')


input("Press ENTER after login into Whatsapp Web and your chats are visiable.")

filepath = input("Enter the path of the image to be attached : ")


for column in excel_data['Contact'].tolist():
    try:
        url = 'https://web.whatsapp.com/send?phone=' + str(excel_data['Contact'][count]) + '&text=' + excel_data['Message'][count]
        sent = False

        # It tries 3 times to send a message in case if there any error occurred

        driver.get(url)
        try:
            click_btn = WebDriverWait(driver, 35).until(
                EC.element_to_be_clickable((By.CLASS_NAME, '_4sWnG')))

            sleep(2)

            attachment_box = driver.find_element(By.XPATH, '//div[@title="Attach"]')
            attachment_box.click()

            sleep(2)

            image_box = driver.find_element(By.XPATH,'//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            image_box.send_keys(filepath)

            sleep(2)

            send_button = driver.find_element(By.XPATH, '//div[@class="_165_h _2HL9j"]')
            # send_button.click()

        except Exception as e:
            print("Sorry message could not sent to " + str(excel_data['Contact'][count]))
        else:
            sleep(2)
            # click_btn.click()
            send_button.click()
            sent = True
            sleep(2)
            print('Message sent to: ' + str(excel_data['Contact'][count]))

        count = count + 1
        
    except Exception as e:
        print('Failed to send message to ' + str(excel_data['Contact'][count]) + str(e))
driver.quit()
print("The script executed successfully.")
