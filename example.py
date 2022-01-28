text_file = open("D:\python\og automated whatsapp web prog\Whatsapp_Text_Only\details.txt", "r")
message = text_file.read()
# print(message)
for i in message:
    if i == "media file":
        print("found")
li = message.split("=|\n")
print(li)
print()
text_file.close()