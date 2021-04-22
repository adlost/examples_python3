#! python3
#Программа для добавления маркировки Wiki.

import pyperclip

text = pyperclip.paste()

#TODO: разделить строки и добавить звездочки.
lines = text.split('\n')
for i in range(len(lines)):
	lines[i] = '* ' + lines[i]

text = '\n'.join(lines)


pyperclip.copy(text)

