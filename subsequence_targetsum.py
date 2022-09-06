def printall(indx, temp_arr, ans_arr, s, arr, target_sum):
	if indx == len(arr):
		if s == target_sum:
			t_arr = temp_arr.copy()
			ans_arr.append(t_arr)
		return ans_arr
		# return

	# add
	s += arr[indx]
	temp_arr.append(arr[indx])
	a_arr = printall(indx + 1, temp_arr, ans_arr, s, arr, target_sum)

	# remove
	s -= arr[indx]
	temp_arr.pop()
	return printall(indx + 1, temp_arr, a_arr, s, arr, target_sum)
	# return ans_arr


def print_True_False(indx, temp_arr, s, arr, target_sum):
	if indx == len(arr):
		if s == target_sum:
			return True
		else:
			return False
	# add
	s += arr[indx]
	temp_arr.append(arr[indx])
	if print_True_False(indx + 1, temp_arr, s, arr, target_sum):
		return True

	# remove
	s -= arr[indx]
	temp_arr.pop()
	if print_True_False(indx + 1, temp_arr, s, arr, target_sum):
		return True
	return False


def print_onlyone_pair(indx, temp_arr, s, arr, target_sum):
	if indx == len(arr):
		if s == target_sum:
			return temp_arr
		else:
			return []
	s += arr[indx]
	temp_arr.append(arr[indx])
	one_pair = print_onlyone_pair(indx + 1, temp_arr, s, arr, target_sum)
	if one_pair:
		return one_pair

	s -= arr[indx]
	temp_arr.pop()
	one_pair = print_onlyone_pair(indx + 1, temp_arr, s, arr, target_sum)
	if one_pair:
		return one_pair
	return []


arr1 = [3, 1, 2]
target1 = 3
print(printall(0, [], [], 0, arr1, target1))
print(print_True_False(0, [], 0, arr1, target1))
print(print_onlyone_pair(0, [], 0, arr1, target1))
