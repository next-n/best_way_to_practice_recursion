def sumArrayWithRecursion(arr, index):
	if index == 0:
		return arr[index]
	else:
		return arr[index] + sumArrayWithRecursion(arr, index - 1)


arr1 = [1, 2, 3]
print(sumArrayWithRecursion(arr1, len(arr1) - 1))
