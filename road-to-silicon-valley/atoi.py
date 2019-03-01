def atoi(str):
	length = len(str)
	if length == 0:
		return 0
	INT_MAX = 2**31
	INT_MIN = INT_MAX * -1
	result_string = ""
	for index in xrange(0, length):
		if ord(str[index]) == 45 or ord(str[index]) == 43 :
			result_string = result_string + str[index]
			continue
		if ord(str[index]) != 32:
			if ord(str[index]) > 48  and ord(str[index]) < 58:
				result_string = result_string + str[index]
			else:
				break
	if len(result_string) == 0:
		return 0 
	if int(result_string) < INT_MIN:
		return INT_MIN
	if int(result_string) > INT_MAX:
		return INT_MAX
	return int(result_string)



case_1 = "42"
case_2 = " 42"
case_3 = "4193 with words"
case_4 = "words and 987"
case_5 = "-91283472332"
print atoi(case_1)
print atoi(case_2)
print atoi(case_3)
print atoi(case_4)
print atoi(case_5)
