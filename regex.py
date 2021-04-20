#! python3
#  phoneAndEmail.py - Находит тлефонные номера и 
#адреса электронной почты в буфер обмена.


import pyperclip, re

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?				# териториалньый код, может отсутсвовать или быть 1 раз, сотоять из 3-х цыфр, в скобках или без
	(\s|-|\.)?						# разделитель, может отсутсвовать или быть 1 раз, в виде пробела, дефиса или точки
	\d{3}							# первые 3 цифры
	(\s|-|\.)						# разделитель, в виде пробела, дефиса или точки
	\d{4}							# 5						    # 7последние 4 цифры
	(\s*(ext|x|ext.)\s*\d{2,5})?	# добавочный номер
	)''', re.VERBOSE)

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
	print(groups)
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != ' ':
		phoneNum += ' x' + groups[8]
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