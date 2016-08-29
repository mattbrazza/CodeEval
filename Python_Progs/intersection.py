import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = test[:len(test)-1]
        test = test.split(';')
        
        a = map(int, test[0].split(','))
        b = map(int, test[1].split(','))

        ll = len(a) if (len(a) < len(b)) else len(b)
        switch = (sum(a[:ll-1]) > sum(b[:ll-1]))
        if (switch):
            l1, l2 = b, a
        else:
            l1, l2 = a, b

        ans = []
        i = 0
        for num in l1:
            if (num > l2[i]):
                break
            elif (num == l2[i]):
                ans.append(num)
                i += 1
            if (i == len(l2)):
                break

        if (len(ans) == 0):
            print ""
        else:
            ans = map(str, ans)
            print ",".join(ans)

