import sys
from collections import OrderedDict

class Node:
    def __init__(self, k, v, lf=False, l=None, r=None):
        self.key = k
        self.value = v
        self.leaf = lf
        self.left = l
        self.right = r
        self.code = ""

    def __str__(self):
        return "{}-{}--{}-{}".format(self.value, self.leaf, self.left, self.right)

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print test

# Create dictionary of input sring's letters and their occurence number
        letters = {}
        for ch in test[:len(test)-1]:
            if (ch in letters):
                letters[ch] += 1
            else:
                letters[ch] = 1

# Create the Huffman tree
        values_sorted = OrderedDict(sorted(letters.items(), key=lambda t: t[1]))

        for k in values_sorted:
            print k, values_sorted[k]

        leafs = []
        for k in values_sorted:
            leafs.append(Node(k, values_sorted[k], True))

        print leafs

# Trying something new.........
        tree = {}
        for itm in leafs:
            if (itm.value in tree):
                tree[itm.value].append(itm)
            else:
                tree[itm.value] = [itm]

        for k in tree:
            for j in tree[k]:
                print k, j

        break

# Find a way to compare values and merge the two lowest ones...
        min_k = leafs[0].key
        min_v = leafs[0].value
        i = 0
        while (len(leafs)>0):
            print i, len(leafs)
            if (leafs[i].value > 0):
                print "----", leafs[i].key, leafs[i].value
            leafs.remove(leafs[0])
            i += 0
        #---

        new_leafs = []
        for i1 in range(0,len(leafs),2):
            print i1
            n1 = leafs[i1]
            n2 = leafs[i1+1]
            new_leafs.append(Node(n1.value + n2.value, False, n1, n2))

        for nd in new_leafs:
            crt = nd
            while not (crt.left):
                crt = crt.left
                print crt
            while not (crt.right):
                crt = crt.right
                print crt

# Assign encoding bits to leafs

# Print out answer
#        break

"""
        countries = test[:len(test)-1].split(' | ')
        teams = {}
        i = 1
        for country in countries:
            for team in country.split(' '):
                if (team in teams):
                    teams[team].append(str(i))
                else:
                    teams[team] = [str(i)]
            i += 1

        ans = []
        for k in sorted(map(int, teams)):
            cntrs = ','.join(teams[str(k)])
            ans.append("{}:{}".format(str(k), cntrs))

        print "{};".format('; '.join(ans))
"""

