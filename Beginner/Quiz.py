# variable definition #

from class2 import Quiz
terminate = True

questions = [
    "Who was the winner of the 2022 edition of the world cup?"
    "When did Nigeria gain independence?"
    "Who was the major antagonist for the second world war"
]

options = [
    ["(a) Argentina \n", "(b) France \n", "(c) Portugal \n", "(d) Denmark"],
    ["(a) 1963 \n" "(b) 1954 \n" "(c) 1960 \n" "(d) 1966"],
    ["(a) Donald Trump\n" "(b) Thomas Hitler \n" "(c) Rabastan Lestrange \n" "(d) Adolf Hitler"]

]

answers = [
    "a"
    "c"
    "d"
]

for question in questions:
    score = 0
    print(options)
    answer_1 = input("Your answer:")
    for answer in answers:
        if answer_1 == answer:
            score += 1

