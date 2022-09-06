def bitwise_appo(arr):
	ans = []
	n = 2 ** len(arr)
	for x in range(n):
		temp = []
		# tempind = x
		for i in range(len(arr)):
			# print(temp, i, x)
			j = 2 ** i
			indx = j & x

			if indx == j:
				# print(arr[i])
				indx -= 1
				temp.append(arr[i])
		ans.append(temp)
	return ans


def recursive_subarray(arr, indx, temp_arr, ans_arr):
	if indx == len(arr):
		# print("inside return", ans_arr)
		t_arr = temp_arr.copy()
		ans_arr.append(t_arr)
		return ans_arr
	# right = None
	# right = temp_arr
	temp_arr.append(arr[indx])
	a_arr = recursive_subarray(arr, indx + 1, temp_arr, ans_arr)
	# print("a_arr", a_arr)
	temp_arr.pop()
	return recursive_subarray(arr, indx + 1, temp_arr, a_arr)


arr1 = [3, 2, 1]
print(bitwise_appo(arr1))
print(recursive_subarray(arr1, 0, [], []))
