"""Password generator"""


import secrets
import string
from cryptography.fernet import Fernet

letters = string.ascii_letters
number = string.digits
special_characters = string.punctuation
total = letters + number + special_characters

n = int(input("Enter the desired length of the password:"))
pwd = ""

for i in range(n):
    pwd += "".join(secrets.choice(total))

key = Fernet.generate_key()
f = Fernet(key)
d = pwd.encode()
encrypted_pwd = f.encrypt(d)


def file_handling_2():
    print("1. Press r to read"
        "     2. w to change or add"
        "     3. h to view originals")
    prompt_1 = input("What do you want to do with your passwords:")
    if prompt_1 == "r":
        file_operation_1 = open('password', "r")
        for i in file_operation_1:
            print(i)
    elif prompt_1 == "w":
        file_operation_2 = open('password', "a+")
        info_1 = input("Website:")
        info_2 = encrypted_pwd
        info_3 = n
        print(file_operation_2.write('\n' + info_1 + "  -  " + str(info_2) + "  -  " + str("length of the password is " + str(info_3))))
        file_operation_2.close()
    elif prompt_1 == "h":
        file_operation_1 = open('password', "r")
        info_website = input("What website are you looking for: ")
        for password in file_operation_1:
            print(password)
        #  decrypted_pwd = f.decrypt(pwd)
         #   print(decrypted_pwd)
          #  print(d)
    else:
        print("Invalid operation")


file_handling_2()
