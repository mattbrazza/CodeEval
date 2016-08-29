import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
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

