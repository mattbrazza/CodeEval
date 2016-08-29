import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        scnt = 0
        cnt = 1
        nstr = ""
        for ch in test:
            if ch.isalpha():
                if (cnt%2)==0:
                    nstr += ch.lower()
                else:
                    nstr += ch.upper()
                cnt += 1
            else:
                nstr += ch
            scnt += 1        
        print nstr

