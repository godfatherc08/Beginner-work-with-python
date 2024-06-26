def true ():
    user = [19, 19, 5, 5, 5, 4, 32, 2]
    noOf19 = user.count(19)
    no0f5 = user.count(5)
    if noOf19 == 2 and no0f5 == 3:
        print('TRUE')
    else:
        print("False")

true()

def accept():
    list_1 = [19, 15, 5, 7, 5, 5, 2]
    count = len(list_1)
    value = list_1[4]
    noOf5th = list_1.count(value)
    if count == 8 and noOf5th == 3:
        print("TRUE")
    else:
        print('FALSE')
accept()

