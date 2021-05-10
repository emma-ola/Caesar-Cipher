# Area Calc
# The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a
# random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height ✖️ wall width) ÷ coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 * 4) ÷ 5  = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
# Write your code below this line 👇
from math import ceil


def paint_calc(height, width, cover):
    num_of_cans = ceil((height * width) / cover)
    print(f'You\'ll need {num_of_cans} cans of paint.')


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# Prime Numbers
# Prime numbers are numbers that can only be cleanly divided by itself and 1.
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
def prime_checker(number):
    is_prime = True
    # Because a prime num can only be cleanly divisible by itself and one, generate a range of numbers from 2 to the num
    # before the number we want to check. Loop through the numbers and check if the num is cleanly divisible by any of
    # the generated numbers, if it is, then it is not a Prime Number.
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print('It\'s a prime number.')
    else:
        print('It\'s not a prime number.')


n = int(input("Check this number: "))
prime_checker(number=n)
