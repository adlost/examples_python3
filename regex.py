#! python3
#  phoneAndEmail.py - Находит тлефонные номера и 
#адреса электронной почты в буфер обмена.


import pyperclip, re

phoneRegex = re.compile(r'''((\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10,14}(\s*)?)''', re.VERBOSE)

#TODO: Создать регулярное выражение для адресов электронной почты

emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+				# имя пользователя
	@								# символ @
	[a-zA-Z0-9.-]+					# имя домена
	(\.[a-zA-Z]{2,4})				# остальная чсть адреса
	)''', re.VERBOSE)


#TODO: Найти соответсвия в текстве, содержащемся в буфере обмена

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[0]])
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])


#TODO: Скопировать результат в буфер обмена.

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Скопировано в буфер обмена:')
	print('\n'.join(matches))
else:
	print('ошибка')