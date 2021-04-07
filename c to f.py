while True :
	c = input('請輸入攝氏溫度: ')
	if  c == 'q' :
		print('終止程式')
		break
	else:		
		result = float(c) * 1.8 + 32
		print('華氏溫度為', result)
