"Solution in Python"
def get_changes(money):
	"""Return changes for money
	>>> get_changes(17)
	10
	5
	1
	1
	"""
	if money > 0:
		for change in [50, 25, 10, 5, 1]:
			if money >= change:
				money -= change
				print change
				break
		get_changes(money)

def get_changes_non_recur(money):
	i, changes = 0, [50, 25, 10, 5, 1]
	while money > 0 and i < len(changes):
		numOfCoins = money / changes[i]
		if numOfCoins > 0:
			print ( str(changes[i]) + ',' ) * numOfCoins
			money -= numOfCoins * changes[i]
		else:
			i += 1






def power(a, n):
	result = 1
	while n > 0:
		if n % 2 == 1:
			result *= a
		a *= a
		n /= 2
	return result

if __name__ == '__main__':
	print power(5,3)


def Q5(stream):
	# only store 101 items in the heap.
	heap = stream[0:101]
	# build min heap
	build_min_heap(heap)
	for item in stream[101:]:
		# get the root, i.e. the min, of heap.
		print heap[0]
		# get the next item from stream as new heap root
		heap[0] = item
		min_heapify(heap)
	# print the last 101 items in the stream
	while heap:
		print heap[0]
		heap.pop(0)
		min_heapify(heap)
