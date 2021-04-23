import os

for folderName, subfolders, filenames in os.walk('/home/l1/python/examples_python3'):
	print ('Текущая директория - ' + folderName)

	for subfolder in subfolders:
		print('Подпапка директории ' + folderName + ': ' + subfolder)

	for filename in filenames:
		 print('Файл в папке ' + subfolder + ': ' + filename)

	print('')
