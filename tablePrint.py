tableData = [['apple', 'orange', 'cherries', 'banana'],
				['Alice', 'Bob', 'Carol', 'David','reafbfbdb'],
				['dogs', 'cats', 'moose', 'goose']]


def check_max_count_in_items(qwerty):
	max_var = 0
	for i in range(len(qwerty)):
		length = len(qwerty[i])
		if length > max_var:
			max_var = length
	return max_var




def printTable(data):
	varstring = ''
	max_tab = check_max_count_in_items(data)
	for i in range(max_tab):
			for c in range(len(data)):
				try:
					varstring += str(data[c][i]).rjust(15)
				except IndexError:
					varstring += ' '.rjust(15)
			varstring += '\n'

	print(varstring)
	



printTable(tableData)
