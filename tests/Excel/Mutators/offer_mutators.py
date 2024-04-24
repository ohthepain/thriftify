# don't forget to add your mutator script to __init__.py

import sys
import importlib

from __main__ import ConfigModule
from __main__ import Log

def AutoOffers(data):
	Log("AutoOffers mutator ...")
	autoPurchaseLists = {}
	data.autoPurchaseLists = {}
	for autoPurchaseListEntry in data.autoPurchaseListEntries:
		currencyId = autoPurchaseListEntry.currencyId
		if not currencyId in autoPurchaseLists:
			autoPurchaseLists[currencyId] = []
		autoPurchaseLists[currencyId].append(autoPurchaseListEntry.purchaseOfferId)

	for currencyId in autoPurchaseLists:
		if not currencyId in data.autoPurchaseLists:
			data.autoPurchaseLists[currencyId] = ConfigModule.AutoPurchaseList()
			data.autoPurchaseLists[currencyId].currencyId = currencyId
		data.autoPurchaseLists[currencyId].purchaseOfferIds = sorted(autoPurchaseLists[currencyId], key=lambda offerId: data.purchaseOffers[offerId].priority)

	data.autoPurchaseListEntries = None

def HeroSummonOverrides(data):
	Log('HeroSummonOverrides mutator ...')
	removeUs = []
	for heroSummonId in data.heroSummons:
		heroSummon = data.heroSummons[heroSummonId]
		if heroSummon.overrideHeroSummonId != None:
			if not heroSummon.overrideHeroSummonId in data.heroSummons:
				print('ERROR: heroSummon <%s> cannot find overrideHeroSummonId <%s> not found' % (heroSummon.heroSummonId, heroSummon.overrideHeroSummonId))
			if heroSummon.overridePurchaseCount == None:
				print('ERROR: heroSummon <%s> overrides overrideHeroSummonId <%s> but has no overridePurchaseCount' % (heroSummon.heroSummonId, heroSummon.overrideHeroSummonId))
			targetHeroSummon = data.heroSummons[heroSummon.overrideHeroSummonId]
			if targetHeroSummon.heroSummonOverrides == None:
				targetHeroSummon.heroSummonOverrides = {}
			if heroSummon.overridePurchaseCount in targetHeroSummon.heroSummonOverrides:
				print('ERROR: heroSummon <%s> has multiple overrides at %d purchases' % (targetHeroSummon.heroSummonId, heroSummon.overridePurchaseCount))
			targetHeroSummon.heroSummonOverrides[heroSummon.overridePurchaseCount] = heroSummon
			# remove from config
			removeUs.append(heroSummonId)
	for heroSummonId in removeUs:
		del data.heroSummons[heroSummonId]

__mutators = [AutoOffers, HeroSummonOverrides]
