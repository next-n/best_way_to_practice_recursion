def sumRecursively(n):
	if n < 1:
		print('nonononono accept only positive')
	elif n == 1:
		return 1
	else:
		return n + sumRecursively(n - 1)


print(sumRecursively(5))
