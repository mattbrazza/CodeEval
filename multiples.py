import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        x, n = map(int, test.split(','))
        m = 1
        ans = n * m
        while (ans < x):
            m += 1
            ans = n * m

        print ans

