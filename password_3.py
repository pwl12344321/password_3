# 密碼重試程式
# 正確密碼 'a123456'
# 最多輸入3次密碼
# 不對的話 印出'Wrong! You have _ chances left'
# 對的話 印出'Correct and enter now'

password = 'a123456'
i = 2
while i >= 0:
	x = input('please enter your password: ')
	if x == password:
		print('Correct and enter now')
		break
	else:
		print('Wrong! You have', i,' chances left')
		i = i - 1