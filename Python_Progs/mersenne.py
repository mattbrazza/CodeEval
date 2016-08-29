# Mersenne Prime = 1 minus a prime that is a perfect square
import sys

def is_prime(num):
    for factor in range(2, int(num**0.5)+1):
        if (num % factor)==0:
            return False
    return True

def is_pwr_2(num):
    x = 0
    y = 2**x
    while (y <= num):
        if (y == num):
            return True
        x += 1
        y = 2**x
    return False

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        num = int(test)
        ans = ""
        for x in range(2, num+1):
            if (is_prime(x) and is_pwr_2(x+1)):
                ans += (str(x)+", ")

        ans = ans[:len(ans)-2]
        print ans

