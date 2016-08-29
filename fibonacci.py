import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        num = int(test)
        total = 0

        if (num == 0):
            total = 0
        elif (num == 1):
            total = 1
        else:
            tot_1 = 0
            tot_2 = 1
            while num > 1:
                total = tot_1 + tot_2
                tot_1 = tot_2
                tot_2 = total
                num -= 1
        print total

