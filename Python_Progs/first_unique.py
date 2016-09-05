import sys

#inin = [["yellow", "tooth"], []]
with open(sys.argv[1], 'r') as test_cases:
#for test_cases in inin:
    for test in test_cases:
		if not test:
			continue
		
		letters = []
		values = []
		for i in range(0,len(test)):
			letter = test[i]
			if letter in letters:
				i0 = letters.index(letter)
				values[i0] = False
			else:
				letters.append(letter)
				values.append(True)

		for j in range(0,len(test)):
			if values[j] == True:
				print letters[j]
				break
