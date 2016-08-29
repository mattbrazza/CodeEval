import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        words = []
        nums = []
        buck = test[:len(test)-1].split(",")
        for item in buck:
            if item.isalpha():
                words.append(item)
            else:
                nums.append(item)

        wordsStr = ",".join(words)
        numsStr = ",".join(nums)
        if len(words) < 1:
            if len(nums) < 1:
                print ""
            else:
                print numsStr
        else:
            if len(nums) < 1:
                print wordsStr
            else:
                print "{0}|{1}".format(wordsStr, numsStr)


