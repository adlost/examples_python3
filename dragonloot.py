inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin']


def addToInventory(inventory, addeditem):
	dirloot={}
	#тут мы делаем из списка словарь
	for i in addeditem:
		dirloot.update({i: addeditem.count(i)})

	#тут творится магия)
	# цикл переперает ключи из лута
	for k, v in dirloot.items():
		var_loot = dirloot.get(k)
		var_inv = inventory.get(k)
		#проверяем есть ли в словаре ключ который есть в луте
		#если ключа нет, переменной присвается значение 0   
		if var_inv== None:
			var_inv = 0
		#тут обновляется значение для ключа
		var_fin = var_loot+var_inv
		inventory.update({k: var_fin})
	print(inventory)


print(inv)
print(dragonLoot)

addToInventory(inv, dragonLoot)