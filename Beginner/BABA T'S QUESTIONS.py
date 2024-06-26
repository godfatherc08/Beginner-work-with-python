import random
import string
import operator

# 1.
age = int(input("Enter your age:"))

if age >= 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")

# 2.
num = int(input("Enter a number:"))
if num % 2 == 0:
    print("The number is even")
else:
    print('The number is odd')

# 3.
num_2 = int(input("Enter a number:"))
if num_2 % 7 == 0:
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 7")

# 4.
num_3 = int(input("Enter a number:"))
if num_3 % 5 == 0:
    print("Hello")
else:
    print("Bye")

# 5.
electricity_bill_float = float(input("Enter your current electricity bill:"))
price = 0
if electricity_bill_float <= 100:
    print("No charge")
elif (electricity_bill_float > 100) and (electricity_bill_float < 200):
    price = 5
    print("Price is #5 per unit")
elif electricity_bill_float > 200:
    price = 10
    print('Price is #10 per unit')

# 6.
num_4 = str(input("Enter a number:"))
digit = num_4[-1]
digit_2 = int(digit)
print(digit_2)

# 7.
num_5 = str(input("Enter a number:"))
digit_3 = num_5[-1]
digit_4 = int(digit)
if digit_4 % 3 == 0:
    print("It is divisible by 3")
else:
    print("It is not divisible by 3")

# 8.
score = float(input("Enter a score between 0.0 and 100.0: "))

if score > 90:
    print("Your grade is an A")
elif (score > 80) and (score <= 90):
    print("Your grade is a B")
elif (score >= 60) and (score <= 80):
    print("Your grade is a C")
else:
    print("Your score is out of specified range")

# 9.
price_2 = float(input("Enter the price of a bike:"))
if price_2 > 100000:
    print("15% tax to be paid")
elif (price_2 > 50000) and (price_2 <= 100000):
    print("10% tax to be paid")
elif price_2 <= 50000:
    print("5% tax to be paid")

# 10.
year = int(input("Enter the year:"))
if year % 2 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")

# 11.
num_6 = int(input("Enter a number between 1 and 7:"))
if num_6 not in range(0, 8):
    print("Wrong value")
days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

if num_6 in days.keys():
    print(days.pop(num_6))

# 12.
num_7 = int(input("Enter a number between 1 and 12:"))
if num_7 not in range(0, 13):
    print("Wrong value")
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}
if num_7 in months.keys():
    print(months.pop(num_7))

# 13.
city = input("Enter a city between Delhi, Agra, Jaipur: ")
if city == "Delhi":
    print("Red Fort is the monument")
elif city == "Agra":
    print("Taj Mahal is the monument")
else:
    print("Jal Mahal is the monument")

# 14.
num_8 = str(input("Enter a number:"))
digit_5 = len(num_8)
if digit_5 == 3:
    print("It is a 3 digit number")
else:
    print("It is not a 3 digit number")

# 15.
age_2 = int(input("Enter your age: "))
if age_2 > 60:
    print("You are a senior citizen")
else:
    print("Go back to work, you are not a senior citizen")
# 16.
num_9 = int(input("Enter a number:"))
num_10 = int(input("Enter another number:"))
min1 = min(num_9, num_10)
print(str(min1) + ' is the lowest number out of your two numbers')

# 17.
num_11 = int(input("Enter a number:"))
num_12 = int(input("Enter another number:"))
max1 = max(num_11, num_12)
print(str(max1) + ' is the highest number out of your two numbers')

# 18.
num_13 = int(input("Enter a number:"))
if num_13 > 0:
    print("It is positive")
else:
    print("It is negative")

# 19.
num_14 = int(input("Enter a number:"))
if (num_14 % 2 == 0) and (num_14 % 3 == 0):
    print("It is divisible by both 2 and 3")
else:
    print("It is not divisible by both 2 and 3")

# 20.
num_15 = int(input("Enter a number:"))
num_16 = int(input("Enter a number:"))
num_17 = int(input("Enter a number:"))
max2 = max(num_15, num_16, num_17)
print(str(max2) + ' is the lowest number out of your three numbers')

# 21.
age_3 = int(input("Enter your age:"))
age_4 = int(input("Enter another age:"))
age_5 = int(input("Enter another age:"))
age_6 = int(input("Enter another age:"))
min_age = min(age_3, age_4, age_5, age_6)
print(str(min_age) + ' is the lowest age out of your four specified ages')

# 22.
age_7 = int(input("Enter another age:"))
age_8 = int(input("Enter another age:"))
age_9 = int(input("Enter another age:"))
age_10 = int(input("Enter another age:"))
max_age = max(age_3, age_4, age_5, age_6)
print(str(max_age) + ' is the lowest age out of your four specified ages')

# 23.
num_18 = int(input("Enter a number:"))
number = list(string.digits)
number.remove('0')
random = random.choice(number)
if (num_18 % num_18 == 0) and (num_18 % 1 == 0) and (num_18 % random != 0):
    print("It is a prime number")
else:
    print("It is not a  prime number")

# 24 and 25.
vowels = ['a', 'e', 'i', 'o', 'u']
letter = str(input('Enter a letter:'))
if letter in vowels:
    print('It is a vowel')
else:
    print("It is a consonant")

# 26.
working_days_total = int(input('Enter your total amount of days at work: '))
absent_days_total = int(input('Enter your total amount of days absent from work: '))
side_1 = working_days_total/absent_days_total
percentage = side_1*100
if percentage < 75:
    print("You will not be able to sit for the exam")
else:
    pass

# 27.
salary = float(input("How much is your salary: "))
bonus_amount = 0
years_of_service = int(input('Enter your total years of service: '))
if years_of_service > 10:
    print("You get a bonus of 10%")
    bonus_amount = (10/100)*salary
    salary += bonus_amount
    print("Your new salary is " + str(salary))
if (years_of_service >= 6) and (years_of_service <= 10):
    print("You get a bonus of 8%")
    bonus_amount = (8/100)*salary
    salary += bonus_amount
    print("Your new salary is " + str(salary))
if years_of_service < 6:
    print("You get a bonus of 6%")
    bonus_amount = (6/109)*salary
    salary += bonus_amount
    print("Your new salary is " + str(salary))

# 28.
side_2 = float(input("Enter a side on the triangle"))
side_3 = float(input("Enter another side on the triangle"))
side_4 = float(input("Enter another side on the triangle"))
if side_2 == (side_3 or side_4):
    print("It is an isosceles triangle")
elif side_2 == (side_3 and side_4):
    print("It is an equilateral triangle")
else:
    print("It is a scalene triangle")

# 29.
print("Valid operations are addition, subtraction, division, multiplication and square")
num_1 = int(input("Enter a number:"))
op = input("Enter an operator:")
num_2 = int(input("Enter another number:"))

if op == "+":
    print(operator.add(num_1, num_2))
elif op == "-":
    print(operator.sub(num_1, num_2))
elif op == "/":
    print(operator.truediv(num_1, num_2))
elif op == "*":
    print(operator.mul(num_1, num_2))
elif op == "**":
    square = int(num_1**num_2)
    print(square)
else:
    print("Invalid operator")


# 30.
length = float(input("Enter the length of the plane shape"))
breadth = float(input("Enter the breadth of the plane shape"))
if length == breadth:
    print("This plane shape is a square")
else:
    print("This plane shape is not a square")
