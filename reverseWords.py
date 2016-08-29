import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test[:len(test)-1]
        words = test.split(" ")
        nwords = words[::-1]
        nstr = " ".join(nwords)
        print nstr


