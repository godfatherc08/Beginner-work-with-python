
import operator
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