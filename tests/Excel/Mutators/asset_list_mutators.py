# don't forget to add your mutator script to __init__.py

from __main__ import Log

def AssetLists(data):
	print("AssetLists mutator ...")
	if hasattr(data, 'assetListEntries'):
# 		if data.assetLists == None:
# 			data.assetLists = []
		for assetListEntry in data.assetListEntries:
			assetListId = assetListEntry.assetListId
			assetId = assetListEntry.assetId
			assetList = data.assetLists[assetListId]
			if assetList.assetIds == None:
				assetList.assetIds = []
			assetList.assetIds.append(assetId)

		data.assetListEntries = None

__mutators = [AssetLists]
