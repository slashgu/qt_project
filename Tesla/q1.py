__author__ = 'chenggu'

import argparse

def is_prime(num):
    for i in range(1, num - 1):
        if num % i is 0:
            return False
    return True

for num in sys.argv:
    if is_prime(int(num)):
        print num, " is prime number!", '\n'
    else:
        print num, " is NOT prime number!", '\n'