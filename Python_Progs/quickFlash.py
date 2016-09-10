import sys

zzz = [["5 2 6 1 3 4", "1 2 3 4", "4 3 2 1"],["3 1 2 4", "1 3 2 4"]]
pivs = 0

def quicksort(arr, start, end):
	if (start < end):
		# find pivot to split list
		piv = find_piv(arr, start, end)
		global pivs
		pivs = pivs + 1
		# sort each part
		quicksort(arr, start, piv-1)
		quicksort(arr, piv+1, end)
	return arr
		
def find_piv(arr, start, end):
	piv = arr[start] # get first item
	left = start + 1 # get left marker
	right = end # get right marker
	over = False
	while (not over):
		while ((left <= right) and (arr[left] <= piv)):
			left = left + 1
		while ((right >= left) and (arr[right] >= piv)):
			right = right - 1
		if (left >= right):
			over = True
		else:
			temp = arr[left]
			arr[left] = arr[right]
			arr[right] = temp
	# swap pivot with current right marker
	temp = arr[start]
	arr[start] = arr[right]
	arr[right] = temp
	return right #current pivot index

#with open(sys.argv[1], 'r') as test_cases:
for test_cases in zzz:
	for test in test_cases:
		if not test:
			continue
		arr = map(int,test.split(' '))
		global pivs
		pivs = 0
		quicksort(arr,0,len(arr)-1)
		print str(pivs)

