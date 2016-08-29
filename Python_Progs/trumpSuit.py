import sys

class Card:
    def __init__(self, val, suit):
        if (val == 'A'):
            value = 14
        elif (val == 'K'):
            value = 13
        elif (val == 'Q'):
            value = 12
        elif (val == 'J'):
            value = 11
        else:
            value = int(val)
        self.v = value
        self.s = suit

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        cards, trump = test[:len(test)-1].split('|')
        cards = cards.split(' ')
        c1r = cards[0].strip()
        c2r = cards[1].strip()
        trump = trump.strip()

        c1 = Card(c1r[:len(c1r)-1], c1r[len(c1r)-1])
        c2 = Card(c2r[:len(c2r)-1], c2r[len(c2r)-1])

        ans = ""
        if (c1.v == 2) or (c2.v == 2):
            if (c1.s == trump) and (c2.s == trump):
                print "{} {}".format(c1r, c2r)
                continue
            elif (c1.s == trump):
                print c1r
                continue
            elif (c2.s == trump):
                print c2r
                continue
        
        if (c1.v == c2.v):
            ans = "{0} {1}".format(c1r, c2r)
        elif (c1.v > c2.v):
            ans = c1r
        else:
            ans = c2r

        print ans

