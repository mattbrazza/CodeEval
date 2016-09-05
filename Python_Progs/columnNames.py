import sys

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

inin = [["1", "13", "26", "28"], ["52"]] #, "3702"]]
#with open(sys.argv[1], 'r') as test_cases:
for test_cases in inin:
	for test in test_cases:
		if not test:
			continue
		
		num = int(test)
		ans = []
		while (num > 0):
			mdlo = num % 26
			lttr = col_conv(mdlo)
			print mdlo, lttr
			ans.append(lttr)
			num = num - 26

		print ans
