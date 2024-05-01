from __main__ import __Check
from __main__ import __Warn
from __main__ import Log

def PurchaseOffers(data):
	Log("PurchaseOffers prevalidator ...")
	for purchaseOfferId in data.purchaseOffers:
		purchaseOffer = data.purchaseOffers[purchaseOfferId]
		if purchaseOffer.shopItemPrefab != None:
			__Check.PrefabAssetExists(purchaseOffer.shopItemPrefab, 'purchaseOffer <%s>' % purchaseOfferId)
		if purchaseOffer.bannerImage != None:
			__Check.ImageAssetExists(purchaseOffer.bannerImage, 'purchaseOffer <%s>' % purchaseOfferId)
		if purchaseOffer.borderImage != None:
			__Check.ImageAssetExists(purchaseOffer.borderImage, 'purchaseOffer <%s>' % purchaseOfferId)
# 		if purchaseOffer.effectIconPath != None:
# 			__Check.ImageAssetExists(purchaseOffer.effectIconPath, 'purchaseOffer <%s>' % purchaseOfferId)

	for heroSummonId in data.heroSummons:
		heroSummon = data.heroSummons[heroSummonId]
		if heroSummon.guaranteedHeroIds != None:
			for heroId in heroSummon.guaranteedHeroIds:
				__Check.Contains(data.heroBodies, heroId, 'heroSummonId <%s> contains undefined heroId <%s>' % (heroSummonId, heroId))

__validators = [PurchaseOffers]
