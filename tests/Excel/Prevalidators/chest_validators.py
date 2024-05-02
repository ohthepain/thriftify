from xl2thrift.validate import __Check
from xl2thrift.validate import __Warn
from xl2thrift.validate import Log

def Chests(data):
	Log("Chests prevalidator ...")
	for chestId in data.chests:
		chest = data.chests[chestId]
		chest.validate()
		if chest.imageSprite != None:
			__Check.ImageAssetExists(chest.imageSprite, 'chest <%s>' % chestId)
		if chest.awardChestClip != None:
			__Check.AudioAssetExists(chest.awardChestClip, 'chest <%s>' % chestId)
		if chest.openChestClip != None:
			__Check.AudioAssetExists(chest.openChestClip, 'chest <%s>' % chestId)
		__Check.PrefabAssetExists(chest.chestPrefab, 'chest <%s>' % chestId)

__validators = [Chests]

