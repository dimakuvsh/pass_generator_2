import random
import string

def generate_password(number_of_symbols = 12):
    paswrd = " "
    for i in range(number_of_symbols):    
        randnum = random.randint(1, 4)
        if randnum == 1:
            paswrd += random.choice(string.ascii_uppercase)
        elif randnum == 2:
            paswrd += random.choice(string.ascii_lowercase)
        elif randnum == 3:
            paswrd += random.choice(string.digits)
        elif randnum == 4:
            paswrd += random.choice("£$%^&*()@}?><*/{[]}:")
    return paswrd

if __name__ == "__main__":
    print("запущен модуль")
    print(generate_password())

