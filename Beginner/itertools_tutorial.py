from itertools import groupby
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import accumulate
from itertools import count, cycle, repeat
import operator
def smaller_than_3(x):
    if x < 3:
        print("True")
    else:
        print("False")

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
c = [5, 6, 7, 8]
prime_2 = product(b, c, repeat= 6)
prime = groupby(a, key=smaller_than_3(5))
prime_3 = combinations(a, 3)
prime_4 = permutations(a, 3)
prime_5 = combinations_with_replacement(a, 2)
prime_6 = accumulate(c, func= max)
print(list(prime))
"""for i in count(10):
    print(i)"""# it will loop infinitely so make sure to use an if statement and break to stop the count
# if i == 15:
# break

"""for i in cycle(a):
    print(i)
    if i == 4:
        break"""# cycles through an iterable

"""for i in repeat(1, 4):
    print(i)""" # Repeats a number