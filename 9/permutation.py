def solution_one(arr, temp, i, ans, m):

	if i == len(arr):
		ans.append(temp.copy())
		return
	for x in range(len(arr)):
		if arr[x] in m:
			continue
		if arr[x] not in m:
			i += 1
			temp.append(arr[x])
			m[arr[x]] = True
			solution_one(arr, temp, i, ans, m)
			m.pop(temp.pop(), None)
			i -= 1
	return ans


def solution_two(arr, i, ans, k):
	if k == 0:
		ans.append(arr.copy())
		return
	for x in range(k):
		arr[i], arr[i+x] = arr[i+x], arr[i]
		solution_two(arr, i+1, ans, k-1)
		arr[i], arr[i+x] = arr[i+x], arr[i]
	return ans


arr1 = [1, 2, 3]
print(solution_one(arr1, [], 0, [], {}))
print(solution_two(arr1, 0, [], len(arr1)))







