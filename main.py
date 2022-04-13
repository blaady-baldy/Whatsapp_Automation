from ast import Num
from logging import exception
from attachments.attach_message import attach_message
from attachments.attach_pdf import attach_pdf
from attachments.attach_media import attach_media
from attachments.attach_message_with_pdf import attach_message_with_pdf
from attachments.attach_message_with_media import attach_message_with_media
from attachments.fetch_number import fetch_number
from attachments.example import return_path
import pandas

def Main(choice,choice_for_name):

    # ******************           EXTRACTING ALL THE DETAILS STORED IN DETAILS.TXT
    excel_path = return_path("excel_filepath")
    excel_filename = return_path("excel_filename")
    name_column = return_path("column_name_of_names_stored")
    contact_column = return_path("column_name_of_contacts")
    excel_data = pandas.read_excel(excel_path, sheet_name=excel_filename)
    
    # ******************            EXECUTING THE FUNCTION ACCORDING TO USER'S CHOICE
    if choice==1:
        attach_message(excel_data,name_column,contact_column,choice_for_name)
    elif choice==2:
        attach_media(excel_data,contact_column)
    elif choice==3:
        attach_pdf(excel_data,contact_column)
    elif choice==4:
        attach_message_with_media(excel_data,name_column,contact_column,choice_for_name)
    elif choice==5:
        attach_message_with_pdf(excel_data,name_column,contact_column,choice_for_name)
    else:
        print("\nWrong choice\nExiting..........\n")


