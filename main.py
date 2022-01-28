from ast import Num
from attach_message import attach_message
from attach_pdf import attach_pdf
from attach_media import attach_media
from example import return_path
import pandas

def Main():
    
    
    print("\n"+"*"*50+"Menu"+"*"*50)
    print("Enter what you want to attach : ")
    print("1. Message")
    print("2. Media file")
    print("3. Pdf")
    print("4. Message with attached media")
    print("5. Message with attached pdf")
    choice = int(input())

    excel_path = return_path("excel_filepath")
    excel_data = pandas.read_excel(excel_path, sheet_name='Recipients')

    if choice==1:
        attach_message(excel_data)
    if choice==2:
        attach_media(excel_data)
    if choice==3:
        attach_pdf(excel_data)

if __name__ == "__main__":
    Main()

