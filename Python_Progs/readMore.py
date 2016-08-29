import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        if len(test) <= 55:
            print test[:len(test)-1]
        else:
            begstr = test[:40]
            begstr = begstr[:begstr.rfind(" ")].strip()
            print "{}... <Read More>".format(begstr)
