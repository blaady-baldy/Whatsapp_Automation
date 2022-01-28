from ast import Num
from logging import exception
from attach_message import attach_message
from attach_pdf import attach_pdf
from attach_media import attach_media
# from script import execute
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
    try:
        choice = int(input("Choice = "))
    except Exception as e:
        print("\nWrong choice\nExiting..........\n")
        return


    excel_path = return_path("excel_filepath")
    excel_filename = return_path("excel_filename")
    name_column = return_path("column_name_of_names_stored")
    contact_column = return_path("column_name_of_contacts")
    excel_data = pandas.read_excel(excel_path, sheet_name=excel_filename)

    # execute(choice, excel_data)
    
    if choice==1:
        attach_message(excel_data,name_column,contact_column)
    elif choice==2:
        attach_media(excel_data,contact_column)
    elif choice==3:
        attach_pdf(excel_data,contact_column)
    elif choice==4:
        attach_message(excel_data,name_column,contact_column)
        attach_media(excel_data,contact_column)
    elif choice==5:
        attach_message(excel_data,name_column,contact_column)
        attach_pdf(excel_data,contact_column)
    else:
        print("\nWrong choice\nExiting..........\n")
if __name__ == "__main__":
    Main()

