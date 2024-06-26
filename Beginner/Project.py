master_password = "pwd"

pwd = input("Please enter the master password:")


def file_handling():
    print("Press r to read or w to change or add")
    prompt_1 = input("What do you want to do with your contacts:")
    if prompt_1 == "r":
        file_operation_1 = open('File', "r")
        for i in file_operation_1:
            print(i)
    elif prompt_1 == "w":
        file_operation_2 = open('File', "a+")
        info_1 = input("Name:")
        info_2 = input("Number:")
        print(file_operation_2.write('\n' + info_1 + "-" + str(info_2)))
        file_operation_2.close()
    else:
        print("Invalid operation")


if pwd == master_password:
    file_handling()
else:
    print("Incorrect master password, you have been logged out")
