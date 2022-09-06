from functools import cmp_to_key


def divi(arr):
	start = 0
	end = len(arr)-1
	if start == end:
		# print("se",arr, start, end)
		return arr
	mid = (start+end) // 2
	left1 = divi(arr[start:mid+1])
	right1 = divi(arr[mid+1:end+1])
	m = merge_sort(left1, right1)
	# print(m)
	return m


def merge_sort(left, right):
	i = 0
	j = 0
	arr = []
	while i < len(left) and j < len(right):
		a = str(left[i])
		b = str(right[j])
		ab = a+b
		ba = b+a
		if ab > ba:
			arr.append(left[i])
			i += 1
		else:
			arr.append(right[j])
			j += 1
	while i < len(left):
		arr.append(left[i])
		i += 1
	while j < len(right):
		arr.append(right[j])
		j += 1
	return arr


arr1 = [3, 30, 34, 5, 9]
arr2 = [30, 9, 5, 3]

print(divi(arr2))
