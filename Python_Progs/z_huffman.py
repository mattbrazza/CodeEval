import sys

class Node(object):
    def __init__(self, k, v, lf=True, l=None, r=None):
        self.letter = k
        self.value = v
        self.leaf = lf
        self.left = l
        self.right = r

    def __repr__(self):
        return ">{}-{}--{}<".format(self.letter, self.value, self.leaf)

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print test  # String of letters

# Break up letters into unique list & occurences
        letters = {}
        for ch in test[:len(test)-1]:
            if (ch in letters):
                letters[ch] += 1
            else:
                letters[ch] = 1

# Create list of sorted (letter, value) by value & letter ??
        sorted_values = sorted(letters.items(), key=lambda x:x[1])
        print sorted_values

        while (len(sorted_values)>1):
            p1 = sorted_values[0]
            p2 = sorted_values[1]
            s = (p1[1] + p2[1])*100
            s = s if (s < 1000) else (s/100)
            if (isinstance(p1[0],Node) and isinstance(p2[0],Node)):
                if (p1[1] > p2[1]):
                    nd = Node('A',s,False,p2[0],p1[0])
                else:
                    nd = Node('B',s,False,p1[0],p2[0])
            elif (isinstance(p1[0],Node) and not isinstance(p2[0],Node)):
                nd = Node('C',s,False,p1[0],p2[0])
            elif (isinstance(p2[0],Node) and not isinstance(p1[0],Node)):
                nd = Node('D',s,False,p2[0],p1[0])
            else:
                n1 = Node(p1[0], p1[1],True,None,None)
                n2 = Node(p2[0], p2[1],True,None,None)
                if (p1[1] > p2[1]):
                    nd = Node('Y',s,False,n2,n1)
                else:
                    nd = Node('Z',s,False,n1,n2)

            sorted_values.append((nd, s))
            sorted_values.remove(p1)
            sorted_values.remove(p2)
            sorted_values = sorted(sorted_values, key=lambda x:x[1])
        print "sorted_values[0] is ", sorted_values, "-->", sorted_values[0]
        print sorted_values[0][0]
        print

# Parse through tree and write encryption
        tree = sorted_values[0][0]
        code = ''

        ans = {}
        n = tree
        while (not n.leaf):
            while (not n.leaf):
                code += '0'
                n = n.left
            ans[n.letter] = code
            n = tree
            while (not n.leaf):
                code += '1'
                n = n.right
            ans[n.letter] = code
            n = tree.right

        print "done"
        for itm in ans:
            print itm,": ",ans[itm]

        break

