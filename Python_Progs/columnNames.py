import sys
from math import log, pow

def col_conv(n):
	cols = {
		1: 'A',
		2: 'B',
		3: 'C',
		4: 'D',
		5: 'E',
		6: 'F',
		7: 'G',
		8: 'H',
		9: 'I',
		10: 'J',
		11: 'K',
		12: 'L',
		13: 'M',
		14: 'N',
		15: 'O',
		16: 'P',
		17: 'Q',
		18: 'R',
		19: 'S',
		20: 'T',
		21: 'U',
		22: 'V',
		23: 'W',
		24: 'X',
		25: 'Y',
		0: 'Z'}
	return cols[n]

inin = [["1", "13", "26", "28"], ["52", "3702"]]
#with open(sys.argv[1], 'r') as test_cases:
for test_cases in inin:
	for test in test_cases:
		if not test:
			continue
		
		num = int(test)
		ans = []
		while (num > 0):
			nexp = int(log(num, 26))
			npow = pow(26, nexp)
			print nexp, npow
			
			mdlo = (num - npow) % 26
			lttr = col_conv(mdlo)
			print mdlo, lttr

#			ans.append(lttr)
			num = num - npow

		print ans

#26^2 = 676
#26^3 = 17,576
#A to Z = 1 to 26
#AA to ZZ = 27 to 702
#AAA to ZZZ = 703 to 18278
#ZZZ = 26^1 + 26^2 + 26^3
