from xl2thrift.validate import __Check
from xl2thrift.validate import __Warn
from xl2thrift.validate import Log

def Campaigns(data):
	Log("Campaigns prevalidator ...")
	for campaignId in data.campaigns:
		campaign = data.campaigns[campaignId]
		campaign.validate()
		if campaign.backgroundImagePath != None:
			__Check.ImageAssetExists(campaign.backgroundImagePath, 'Campaign <%s>' % campaignId)
		__Check.ImageAssetExists(campaign.campaignLoadingSignPath, 'Campaign <%s>' % campaignId)
		__Check.AssetExists(campaign.iconPrefabPath, 'Campaign <%s>' % campaignId)
		__Check.ImageAssetExists(campaign.battleMenuImagePath, 'Campaign <%s>' % campaignId)
		if campaign.campaignSignPath != None:
			__Check.ImageAssetExists(campaign.campaignSignPath, 'Campaign <%s>' % campaignId)
		__Check.ImageAssetExists(campaign.campaignLevelFontPath, 'Campaign <%s>' % campaignId)

__validators = [Campaigns]

