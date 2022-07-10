def binarySearchUsingRecursive(arr, low, high, searchnumber):
	if not high < low:
		mid = (high + low) // 2

		if searchnumber == arr[mid]:
			return mid
		elif searchnumber < mid:
			return binarySearchUsingRecursive(arr, low, mid - 1, searchnumber)
		elif searchnumber > mid:
			return binarySearchUsingRecursive(arr, mid + 1, high, searchnumber)
	else:
		return "Not Found"


arr1 = [1, 2, 3, 4, 5]
print("index is", binarySearchUsingRecursive(arr1, 0, len(arr1) - 1, 3))
