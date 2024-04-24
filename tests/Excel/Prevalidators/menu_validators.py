from __main__ import __Check
from __main__ import __Warn
from __main__ import Log

def Menus(data):
	Log("menus postvalidator ...")
	for menuId in data.menus:
		menu = data.menus[menuId]
		if menu.hudProfileId != None:
			__Check.Contains(data.hudProfiles, menu.hudProfileId, 'hud profile <%s> does not exist for menu <%s>' % (menu.hudProfileId, menuId))
		__Check.PrefabAssetExists(menu.prefabPath, 'menu <%s>' % menuId)

def HudProfiles(data):
	Log("hud profiles postvalidator ...")
	for hudProfileId in data.hudProfiles:
		hudProfile = data.hudProfiles[hudProfileId]
		if hudProfile.currencyIds != None:
			for currencyId in hudProfile.currencyIds:
				 __Check.Contains(data.currencies, currencyId, 'hud profile <%s> contains an undefined currencyid <%s>' % (hudProfileId, currencyId))

__validators = [Menus, HudProfiles]
