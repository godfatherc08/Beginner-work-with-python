
from Password import encrypted_pwd

class Quiz:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

def file_handling_2():
    print("Press r to read or w to change or add")
    prompt_1 = input("What do you want to do with your passwords:")
    if prompt_1 == "r":
        file_operation_1 = open('password', "r")
        for i in file_operation_1:
            print(i)
    elif prompt_1 == "w":
        file_operation_2 = open('password', "a")
        info_1 = input("Website:")
        info_2 = encrypted_pwd
        info_3 = input("Length of the password:")
        '\n'
        print(file_operation_2.write(info_1 + "  -  " + str(info_2) + "  -  " + str("length of the password is " + info_3)))
        file_operation_2.close()
    else:
        print("Invalid operation")


