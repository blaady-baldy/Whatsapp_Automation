# ************      PROGRAM TO RETURN DATA STORED FROM THE FORM

def return_path(path):

    text_file = open("details.txt", "r")
    message = text_file.read().split("\n")
    c = 0
    for i in message:
        obj = i.split(" = ")
        if obj[0]==path:
            return obj[1]

    print()
    text_file.close()