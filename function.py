# This is dhaval python homework
import math


def is_prime_and_odd(number):
    """
    All the numbers are which are prime
    or odd, so checking for odd is futile

    :param number:
    :return:
    """
    n = int(math.sqrt(number))
    for i in range(2, n + 1):
        if number % i == 0:
            prime = 1
            break
        else:
            prime = 0
    return prime


is_prime = is_prime_and_odd(8)

print("If the return is {} then it is prime".format(is_prime))


def print_pattern(number):
    if number % 2 == 1:
        for i in range(0, number):
            for j in range(0, i + 1):
                print('* ', end="")
            print("\r")
    else:
        for i in range(number, 0, -1):
            print((number - i) * ' ' + i * '*')


print_pattern(8)


def master_yoda(words):
    return reverse(words)


def reverse(words):
    reverse_str = ""
    for i in words:
        reverse_str = i + reverse_str
    return reverse_str


print(master_yoda("Bunza"))
