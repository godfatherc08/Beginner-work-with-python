
score = float(input("Enter a score between 0.0 and 1.0: "))

if score >= 0.9:
    print("Your grade is an A")
elif score >= 0.8:
    print("Your grade is a B")
elif score >= 0.7:
    print("Your grade is a C")
elif score >= 0.6:
    print("Your grade is a D")
elif score < 0.6:
    print("Your grade is an F")
else:
    print("Your score is out of specified range")