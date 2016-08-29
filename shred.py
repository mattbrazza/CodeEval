import sys

with open(sys.argv[1], 'r') as test_cases:
    for test_case in test_cases:
        shreds = map(str,test_case[1:-2].split('|'));

        i = 0
        while len(shreds) > 10:
            spot = shreds.pop(0)
            i = i+1
#            print "Spot(" + str(i) + "): " + spot
            if not spot:
                continue
            j = 0
            for test in shreds:
                j = j+1
#                print "Test(" + str(j) + "): " + test
                lspot = len(spot)
                ltest = len(test)
                if lspot > ltest:
                    print spot +">"+ test
                    if test[1:] == spot[:ltest]:
#                        print spot +":"+ test
                        comb = "%s%s" % (test[-1:],spot)
                    elif test[:-1] == spot[:-ltest]:
#                        print spot +"::"+ test
                        comb = "%s%s" % (spot,test[:-1])
                    else:
                        comb = ""
                elif lspot < ltest:
                    print spot + "<" + test
                    if spot[1:] == test[:lspot]:
#                        print spot +":::"+ test
                        comb = "%s%s" % (spot[-1:],test)
                    elif spot[:-1] == test[:-(lspot-1)]:
#                        print spot +":::"+ test
                        comb = "%s%s" % (test,spot[:-1])
                    else:
                        comb = ""
                else:
                    if spot[1:] == test[:-1]:
                        comb = "%s%s" % (spot,test[ltest-1])
                    elif spot[:-1] == test[1:]:
                        comb = "%s%s" % (test[0],spot)
                    else:
                        comb = ""

                if comb:
#                    print spot +"::"+ test
#                    shreds.remove(spot)
                    shreds.remove(test)
                    shreds.append(comb)
                    print "Comb/b: " + comb
                    break

            ans = ''.join(shreds)
        print ans

#        test = map(int, test.split(','))
#        ans = []
#        ans.append(test.pop(0))
#        for num in test:
#            if (num != ans[len(ans)-1]):
#                ans.append(num)
#
#        ans = map(str,ans)
#        print ','.join(ans)

