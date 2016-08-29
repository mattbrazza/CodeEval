import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        ans = ""
        cap = True
        for ch in test:
            if (cap):
                if (ch.isalpha()):
                    ans += ch.upper()
                else:
                    ans += ch
                cap = False
            else:
                if (ch == ' '):
                    cap = True
                ans += ch

        print ans[:len(ans)-1]

