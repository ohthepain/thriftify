from __main__ import __Check
from __main__ import __Warn
from __main__ import Log

def __listGearTables():
	# uncomment this if you want to generate loot tables
	#return True
	return False

def GearItems(data):
	for gearItemId in data.gearItems:
		gearItem = data.gearItems[gearItemId]
		__Check.ListsAreSameLength(gearItem.craftItemIds, gearItem.craftItemCounts, 'Gear Item <%s> craftItemIds and craftItemCounts are not the same length' % (gearItemId))
		__Check.ListsAreSameLength(gearItem.heroStatIds, gearItem.heroStatAmounts, 'Gear Item <%s> heroStatIds and heroStatAmounts are not the same length' % (gearItemId))
		__Check.AllItemsInListExistInTable(gearItem.craftItemIds, data.gearItems, 'Gear Item Component <%s> does not exist')
		__Check.Contains(data.currencies, gearItemId, 'Gear Item <%s> has not corresponding currency' % (gearItemId))

def __RotateItems(itemIds, rotation):
	numrotations = 0
	count = 0
	rotationcount = 0
	for gearItemId in itemIds:
		count += 1
		rotationcount += 1
		if rotationcount > rotation:
			numrotations += 1
			rotationcount = 0
		dalist = []
		for x in range(0,numrotations+1):
			index = count - 1 - x * numrotations
			#print('%d - 1  %d * %d = %d/%d' % (count, x, numrotations, index, len(itemIds)))
			dalist.append(itemIds[index])
		s = ','
# 		print(s.join(dalist))

def CommonItems(data):
	if __listGearTables():
		from validate import ThriftModule
		Log("---------- Common Items")
		itemIds = []
		for gearItemId in data.gearItems:
			gearItem = data.gearItems[gearItemId]
			if gearItem.dropTypeId != ThriftModule.DropTypeID.CraftOnly:
				if gearItem.rarityId == 0:
					itemIds.append(gearItem.gearItemId)
		__RotateItems(itemIds, 6)

def RareItems(data):
	if __listGearTables():
		from validate import ThriftModule
		Log("---------- Rare Items")
		itemIds = []
		for gearItemId in data.gearItems:
			gearItem = data.gearItems[gearItemId]
			if gearItem.dropTypeId != ThriftModule.DropTypeID.CraftOnly:
				if gearItem.rarityId == 1:
					itemIds.append(gearItem.gearItemId)
		__RotateItems(itemIds, 6)

def EpicItems(data):
	if __listGearTables():
		from validate import ThriftModule
		Log("--------- Epic Items")
		itemIds = []
		for gearItemId in data.gearItems:
			gearItem = data.gearItems[gearItemId]
			if gearItem.dropTypeId != ThriftModule.DropTypeID.CraftOnly:
				if gearItem.rarityId == 2:
					itemIds.append(gearItem.gearItemId)
		__RotateItems(itemIds, 6)

def LegendaryItems(data):
	if __listGearTables():
		from validate import ThriftModule
		Log("--------- Legendary Items")
		itemIds = []
		for gearItemId in data.gearItems:
			gearItem = data.gearItems[gearItemId]
			if gearItem.dropTypeId != ThriftModule.DropTypeID.CraftOnly:
				if gearItem.rarityId == 3:
					itemIds.append(gearItem.gearItemId)
		__RotateItems(itemIds, 6)

__validators = [GearItems, CommonItems, RareItems, EpicItems, LegendaryItems]
