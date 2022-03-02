# class return_path:
def return_path(path):

    text_file = open("details1.txt", "r")
    message = text_file.read().split("\n")
        # print(message)

    c = 0
    for i in message:
        obj = i.split(" = ")
        if obj[0]==path:
            return obj[1]

    print()
    text_file.close()