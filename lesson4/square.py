from math import sqrt
from itertools import count, islice


def simple_square(num):
    if is_prime(num):
        return num * num
    return num


def is_prime(n):
    if n < 2 :
        return False
    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False
    return True


squared_numbers = list(map(simple_square, range(20)))
print(squared_numbers)