def combine(arr, i, temp, tempsum, ans, target):
	if i == len(arr) or tempsum >= target:
		# print(ans, tempsum, temp)
		if tempsum == target:
			# print(temp)
			t = temp.copy()
			ans.append(t)
		return
	temp.append(arr[i])
	tempsum += arr[i]
	combine(arr, i, temp, tempsum, ans, target)
	temp.pop()
	tempsum -= arr[i]
	combine(arr, i+1, temp, tempsum, ans, target)
	return ans


def combine_sec(arr, i, target, temp, ans):
	if target == 0:
		t = temp.copy()
		ans.append(t)
		return
	if i == len(arr) or target < arr[i]:
		return
	target -= arr[i]
	temp.append(arr[i])
	combine_sec(arr, i, target, temp, ans)
	temp.pop()
	target += arr[i]
	combine_sec(arr, i+1, target, temp, ans)
	return ans


arr1 = [2, 3, 7]
print(combine(arr1, 0, [], 0, [], 7))
arr1.sort()
print(combine_sec(arr1, 0, 7, [], []))
