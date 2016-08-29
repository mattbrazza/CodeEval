import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        test = map(int, test.split(','))
        ans = []
        ans.append(test.pop(0))
        for num in test:
            if (num != ans[len(ans)-1]):
                ans.append(num)

        ans = map(str,ans)
        print ','.join(ans)

