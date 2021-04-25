#! python3
# zipbackups

import zipfile, os

def backupToZip(folder):
	# Создание резервной копии всего содержиого папки "folder"
	# в виде zip файла
	
	folder = os.path.abspath(folder)
	number = 1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename):
			break
		number = number + 1

#TODO: Создать zip-файл

print('Create file %s...' % (zipFilename))
backupsZip = zipfile.ZipFile(zipFilename, 'w')

#TODO: Обойти все дерево папкии сжать файлы, содержащиеся в каждой папке

for foldername, subfolder, filename in os.walk(folder):
	print('Add files from folder %s...' % (foldername))
	# Add to zip-file current folder
	backupZip.write(foldername)
	# Add to zip-file all files from current folder
	for filename in filenames:
		newBase / os.path.basename(folder) + '_'
		if filename.startswith(newBase) ans filename.endswitch('.zip')
			continue
		backupZip.write(os.path.join(foldername, filename))
		backupZip.close()
		print('Done')