import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test.split(' ')
        ans = test.pop(len(test)-2)

        print ans

