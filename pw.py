#! python3
#pw.py - Программа для незащищенного хранения паролей.

PASSWORDS = {'email':'psmdfbmsdfgbmklsmdfklbmsklmfgb',
			'blog':'SDCVoomMmpovpsmdvsMSVMSKmvskmdvs',
			'luggage':'12345'}


import sys
if len(sys.argv) < 2:
	print('Использование: python pw.py [имя учетной записи] - копирование пароля учетной записи')
	sys.exit()

account = sys.argv[1]


if account in PASSWORDS:
	pyperclips.copy(PASSWORDS[account])
	print('Пароль для ' + account + ' скопировать в буфер.')
else:
	print('Учетная запись ' + account + ' отсутсвует в списке.')