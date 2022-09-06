def printi(arr, i):
	if i >= len(arr):
		return
	print(arr[i])
	printi(arr, i + 1)
	printi(arr, i + 2)


def print2(n):
	if n >= 4:
		return

	print(n)
	print2(n + 1)
	print(n)
	print2(n + 1)


arr1 = [0, 1, 2, 3, 4]
# printi(arr1, 0)
print2(0)
