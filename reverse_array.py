def reverse_array(arr, left, right):
	if left >= right:
		# print(arr)
		return arr
	arr[left], arr[right] = arr[right], arr[left]
	return reverse_array(arr, left + 1, right - 1)


def reverse_sec(arr, index):
	# print(index)
	if index >= len(arr):
		# print(index)
		return list([])
	prev = reverse_sec(arr, index + 1)
	prev.append(arr[index])

	return prev


arr1 = [1, 2, 3, 4, 5]
print(reverse_array(arr1, 0, 4))
print(reverse_sec(arr1, 0))
