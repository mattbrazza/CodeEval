import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        sets = test[:len(test)-1].split(' ')
        nums = []
        for grp in sets:
            for x in grp:
                nums.append(int(x))

        even = False
        ans = 0
        for n in nums:
            if (even):
                ans += n
            else:
                ans += (n*2)
            even = not even

        if (ans%10)==0:
            print "Real"
        else:
            print "Fake"

