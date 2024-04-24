# don't forget to add your mutator script to __init__.py

from __main__ import Log

def Vip(data):
	Log("Vip mutator ...")
	for vipLevel in data.vipLevels:
		if vipLevel.vipLevelId > 0:
# 			print('%s' % vipLevel.vipLevelId)
			vipLevel.benefitsDesc = ""
			if vipLevel.percentPurchaseGemsBonus != None:
				vipLevel.benefitsDesc += '\n<color=#008080ff>%s%%</color> bonus gems on <color=#008080ff>every gem purchase</color>' % vipLevel.percentPurchaseGemsBonus
			if vipLevel.numDailyLootTickets != None:
				vipLevel.benefitsDesc += '\n<color=#800000ff>%s</color> FREE loot tickets <color=#800000ff>every day</color>' % vipLevel.numDailyLootTickets
			if vipLevel.maxDailyStaminaPurchases != None:
				vipLevel.benefitsDesc += '\n<color=#ffa500ff>%s</color> max daily stamina purchases' % vipLevel.maxDailyStaminaPurchases
# 			print(vipLevel.benefitsDesc)

__mutators = [Vip]
