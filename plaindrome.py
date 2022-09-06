def check(s, index):
	if not s:
		return False
	if index >= len(s) // 2:
		return True
	backpointer = len(s) - 1 - index
	ans = True if s[index] == s[backpointer] else False
	return ans and check(s, index + 1)


def check_sec_apporach(s, index):
	if not s:
		return False
	if index >= len(s) / 2:
		return True
	back  = len(s) - 1 - index
	if s[index] != s[back]:
		return False
	else:
		return check_sec_apporach(s, index + 1)


s1 = "csyuuysc"
b = ""
print(check(b, 0))
print(check_sec_apporach(b, 0))


