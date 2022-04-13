#################   RETURNING 91 COUNTRY CODE ADDED TO THE NUMBER IF THE NUMBER IS 10 DIGITS

def fetch_number(number):
    if len(number)==10:
        num = "91"+number
    else:
        num = number
    return num