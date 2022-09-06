def combine_2(arr, i, target, temp, tempsum, ans):
	if i == len(arr) or tempsum >= target:
		if tempsum == target:
			t = temp.copy()
			ans.append(t)
		return
	tempsum += arr[i]
	temp.append(arr[i])
	combine_2(arr, i + 1, target, temp, tempsum, ans)
	temp.pop()
	tempsum -= arr[i]
	while i + 1 < len(arr) and arr[i] == arr[i + 1]:
		i += 1
	combine_2(arr, i + 1, target, temp, tempsum, ans)
	return ans


def combine_2_sec(arr, i, target, temp, ans):
	if target == 0:
		t = temp.copy()
		ans.append(t)
		return
	if i == len(arr) or target < arr[i]:
		return
	temp.append(arr[i])
	combine_2_sec(arr, i+1, target-arr[i], temp, ans)
	temp.pop()
	while i + 1 < len(arr) and arr[i] == arr[i+1]:
		i += 1
	combine_2_sec(arr, i+1, target, temp, ans)
	return ans


arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(combine_2(arr1, 0, 30, [], 0, []))
print(combine_2_sec(arr1, 0, 30, [], []))

