import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        tcnt = 0.00
        lcnt = 0.00
        ucnt = 0.00 
        for ch in test:
            if ch.isalpha():
                tcnt+=1
                if (ch.islower()):
                    lcnt+=1
                else:
                    ucnt+=1

        lpct = (lcnt/tcnt)*100.00
        upct = (ucnt/tcnt)*100.00
        print "lowercase: {0:.2f} uppercase: {1:.2f}".format(lpct,upct)

