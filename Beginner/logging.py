"""
def get_capital(state):
    states = {
        "Lagos": 'Ikeja',
        "Cross River": "Calabar",
        "Abuja": "FCT"
    }
    return states.get(state, "Invalid input")

print(get_capital(0))
print(get_capital(2))
"""
"""
def total_calc(bill_amount, tip_perc = 10):
    total =  bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")

total_calc((50))
"""

'''
def discount(*args):
    sum = 0
    for i in args:
        i += sum
    if i > 100:
        print("Discount")
    else:
        print("No discount")


discount(10, 20, 30, 50)
'''