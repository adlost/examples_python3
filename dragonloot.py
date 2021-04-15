inv = {'gold coin': 42, 'rope': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin']


def displayInventory(inventory):
	print("Inventory:")
	item_total = 0
	for key, value in inventory.items():
		print(str(value) + ' ' + key)
		item_total += value
	print("Total number of items: " + str (item_total))


def addToInventory(inventory, addeditem):
	dirloot={}
	for i in addeditem:
		dirloot.update({i: addeditem.count(i)})
	




addToInventory(inv, dragonLoot)