# class return_path:
def return_path(path):

    text_file = open("D:\python\og automated whatsapp web prog\Whatsapp_Text_Only\details.txt", "r")
    message = text_file.read().split("\n")
        # print(message)

    c = 0
    for i in message:
        obj = i.split(" = ")
        if obj[0]==path:
            return obj[1]

    print()
    text_file.close()