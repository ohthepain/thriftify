from __main__ import __Check
from __main__ import __Warn
from __main__ import Log

def SimplePopupTemplates(data):
	Log("SimplePopupTemplate prevalidator ...")
	if hasattr(data, 'simplePopupTemplates'):
		for simplePopupTemplateId in data.simplePopupTemplates:
			simplePopupTemplate = data.simplePopupTemplates[simplePopupTemplateId]
			simplePopupTemplate.validate()
			__Check.PrefabAssetExists(simplePopupTemplate.prefab, 'simplePopupTemplate <%s>' % simplePopupTemplateId)

def SimplePopups(data):
	Log("SimplePopup prevalidator ...")
	if hasattr(data, 'simplePopups'):
		for simplePopupId in data.simplePopups:
			simplePopup = data.simplePopups[simplePopupId]
			simplePopup.validate()
			if simplePopup.backgroundImage != None:
				__Check.ImageAssetExists(simplePopup.backgroundImage, 'simplePopup <%s>' % simplePopupId)
			if simplePopup.buttonImage != None:
				__Check.ImageAssetExists(simplePopup.buttonImage, 'simplePopup <%s>' % simplePopupId)

def GiftMessageTemplates(data):
	Log('GiftMessageTemplate prevalidator')
	if hasattr(data, 'giftMessageTemplates'):
		for giftMessageTemplateId in data.giftMessageTemplates:
			giftMessageTemplate = data.giftMessageTemplates[giftMessageTemplateId]
			giftMessageTemplate.validate()
			__Check.PrefabAssetExists(giftMessageTemplate.prefab, 'giftMessageTemplate <%s>' % giftMessageTemplateId)
			__Check.ImageAssetExists(giftMessageTemplate.backgroundImage, 'giftMessageTemplate <%s>' % giftMessageTemplateId)
			__Check.ImageAssetExists(giftMessageTemplate.buttonImage, 'giftMessageTemplate <%s>' % giftMessageTemplateId)

def GiftMessages(data):
	Log('GiftMessages prevalidator ...')
	if hasattr(data, 'giftMessages'):
		for giftMessageId in data.giftMessages:
			giftMessage = data.giftMessages[giftMessageId]
			giftMessage.validate()
			if giftMessage.topIcon != None:
				__Check.ImageAssetExists(giftMessage.topIcon, 'giftMessage <%s>' % giftMessageId)

def GiftMessagePopupTempates(data):
	Log('GiftMessagePopupTempate prevalidator ...')
	if hasattr(data, 'giftMessagePopupTempates'):
		for giftMessagePopupTempateId in data.giftMessagePopupTempates:
			giftMessagePopupTempate = data.giftMessagePopupTempates[giftMessagePopupTempateId]
			giftMessagePopupTempate.validate()
			__Check.PrefabAssetExists(giftMessagePopupTempate.prefab, 'giftMessagePopupTempate <%s>' % giftMessagePopupTempateId)

def GiftMessagePopups(data):
	Log('GiftMessagePopups validator')
	if hasattr(data, 'giftMessagePopups'):
		for giftMessagePopupId in data.giftMessagePopups:
			giftMessagePopup = data.giftMessagePopups[giftMessagePopupId]
			giftMessagePopup.validate()
			if giftMessagePopup.background != None:
				__Check.ImageAssetExists(giftMessagePopup.background, 'giftMessagePopup <%s>' % giftMessagePopupId)
			if giftMessagePopup.centerIcon != None:
				__Check.ImageAssetExists(giftMessagePopup.centerIcon, 'giftMessagePopup <%s>' % giftMessagePopupId)
			if giftMessagePopup.topIcon != None:
				__Check.ImageAssetExists(giftMessagePopup.topIcon, 'giftMessagePopup <%s>' % giftMessagePopupId)

def OfferPackShopItemTemplates(data):
	Log('OfferPackShopItemTemplates validator')
	if hasattr(data, 'offerPackShopItemTemplates'):
		for offerPackShopItemTemplateId in data.offerPackShopItemTemplates:
			offerPackShopItemTemplate = data.offerPackShopItemTemplates[offerPackShopItemTemplateId]
			__Check.PrefabAssetExists(offerPackShopItemTemplate.prefab, 'offerPackShopItemTemplate <%s>' % offerPackShopItemTemplateId)
			if offerPackShopItemTemplate.buyButtonImage != None:
				__Check.ImageAssetExists(offerPackShopItemTemplate.buyButtonImage, 'offerPackShopItemTemplate <%s>' % offerPackShopItemTemplateId)
			if offerPackShopItemTemplate.discountStickerImage != None:
				__Check.ImageAssetExists(offerPackShopItemTemplate.discountStickerImage, 'offerPackShopItemTemplate <%s>' % offerPackShopItemTemplateId)
			if offerPackShopItemTemplate.discountCrossoutImage != None:
				__Check.ImageAssetExists(offerPackShopItemTemplate.discountCrossoutImage, 'offerPackShopItemTemplate <%s>' % offerPackShopItemTemplateId)
			if offerPackShopItemTemplate.timerBgImage != None:
				__Check.ImageAssetExists(offerPackShopItemTemplate.timerBgImage, 'offerPackShopItemTemplate <%s>' % offerPackShopItemTemplateId)
			if offerPackShopItemTemplate.timerClockImage != None:
				__Check.ImageAssetExists(offerPackShopItemTemplate.timerClockImage, 'offerPackShopItemTemplate <%s>' % offerPackShopItemTemplateId)
			if offerPackShopItemTemplate.clockHandImage != None:
				__Check.ImageAssetExists(offerPackShopItemTemplate.clockHandImage, 'offerPackShopItemTemplate <%s>' % offerPackShopItemTemplateId)

def OfferPackShopItems(data):
	Log('OfferPackShopItems validator')
	if hasattr(data, 'offerPackShopItems'):
		for offerPackShopItemId in data.offerPackShopItems:
			offerPackShopItem = data.offerPackShopItems[offerPackShopItemId]
			offerPackShopItem.validate()
			__Check.ImageAssetExists(offerPackShopItem.backgroundImage, 'offerPackShopItem <%s>' % offerPackShopItemId)

def OfferPackZoomItemTemplates(data):
	Log('OfferPackZoomItemTemplates validator')
	if hasattr(data, 'offerPackZoomItemTemplates'):
		for offerPackZoomItemTemplateId in data.offerPackZoomItemTemplates:
			offerPackZoomItemTemplate = data.offerPackZoomItemTemplates[offerPackZoomItemTemplateId]
			__Check.PrefabAssetExists(offerPackZoomItemTemplate.prefab, 'offerPackZoomItemTemplate <%s>' % offerPackZoomItemTemplateId)
			if offerPackZoomItemTemplate.buyButtonImage != None:
				__Check.ImageAssetExists(offerPackZoomItemTemplate.buyButtonImage, 'offerPackZoomItemTemplate <%s>' % offerPackZoomItemTemplateId)
			if offerPackZoomItemTemplate.discountStickerImage != None:
				__Check.ImageAssetExists(offerPackZoomItemTemplate.discountStickerImage, 'offerPackZoomItemTemplate <%s>' % offerPackZoomItemTemplateId)
			if offerPackZoomItemTemplate.discountCrossoutImage != None:
				__Check.ImageAssetExists(offerPackZoomItemTemplate.discountCrossoutImage, 'offerPackZoomItemTemplate <%s>' % offerPackZoomItemTemplateId)
			if offerPackZoomItemTemplate.timerBgImage != None:
				__Check.ImageAssetExists(offerPackZoomItemTemplate.timerBgImage, 'offerPackZoomItemTemplate <%s>' % offerPackZoomItemTemplateId)
			if offerPackZoomItemTemplate.timerClockImage != None:
				__Check.ImageAssetExists(offerPackZoomItemTemplate.timerClockImage, 'offerPackZoomItemTemplate <%s>' % offerPackZoomItemTemplateId)
			if offerPackZoomItemTemplate.timerHandImage != None:
				__Check.ImageAssetExists(offerPackZoomItemTemplate.timerHandImage, 'offerPackZoomItemTemplate <%s>' % offerPackZoomItemTemplateId)

def OfferPackZoomItems(data):
	Log('OfferPackZoomItems validator')
	if hasattr(data, 'offerPackZoomItems'):
		for offerPackZoomItemId in data.offerPackZoomItems:
			offerPackZoomItem = data.offerPackZoomItems[offerPackZoomItemId]
			offerPackZoomItem.validate()
			__Check.ImageAssetExists(offerPackZoomItem.backgroundImage, 'offerPackZoomItem <%s>' % offerPackZoomItemId)

def Enchantments(data):
	Log('Enchantments validator ...')
	if hasattr(data, 'enchantments'):
		for enchantmentId in data.enchantments:
			enchantment = data.enchantments[enchantmentId]
			enchantment.validate()
			if enchantment.enchantAudioPath != None:
				__Check.AudioAssetExists(enchantment.enchantAudioPath, 'enchantment <%s>' % enchantmentId)
			if enchantment.actionAudioPath != None:
				__Check.AudioAssetExists(enchantment.actionAudioPath, 'enchantment <%s>' % enchantmentId)
			if enchantment.effectPrefab != None:
				__Check.PrefabAssetExists(enchantment.effectPrefab, 'enchantment <%s>' % enchantmentId)
			if enchantment.actionPrefab != None:
				__Check.PrefabAssetExists(enchantment.actionPrefab, 'enchantment <%s>' % enchantmentId)
			if enchantment.prefabPath != None:
				__Check.PrefabAssetExists(enchantment.prefabPath, 'enchantment <%s>' % enchantmentId)
			if enchantment.badgeImage != None:
				__Check.ImageAssetExists(enchantment.badgeImage, 'enchantment <%s>' % enchantmentId)

def StatBumpers(data):
	Log('StatBumpers validator')
	if hasattr(data, 'statBumpers'):
		for statBumperId in data.statBumpers:
			statBumper = data.statBumpers[statBumperId]
			statBumper.validate()
			__Check.PrefabAssetExists(statBumper.effectPrefabPath, 'statBumper <%s>' % statBumperId)

def HeroStats(data):
	Log('HeroStats validator')
	if hasattr(data, 'heroStats'):
		for heroStatId in data.heroStats:
			heroStat = data.heroStats[heroStatId]
			heroStat.validate()
			__Check.ImageAssetExists(heroStat.icon, 'heroStat <%s>' % heroStatId)

def HeroStatistics(data):
	Log('HeroStatistics validator')
	if hasattr(data, 'heroStatistics'):
		for heroStatisticId in data.heroStatistics:
			heroStatistic = data.heroStatistics[heroStatisticId]
			heroStatistic.validate()
			__Check.ImageAssetExists(heroStatistic.icon, 'heroStatistic <%s>' % heroStatisticId)

def GearItems(data):
	Log('GearItems validator')
	if hasattr(data, 'gearItems'):
		for gearItemId in data.gearItems:
			gearItem = data.gearItems[gearItemId]
			gearItem.validate()
	# 		__Check.ImageAssetExists(gearItem.catalogImage, 'gearItem <%s>' % gearItemId)
	#		__Check.ImageAssetExists(gearItem.catalogImageDisabled, 'gearItem <%s>' % gearItemId)

def Menus(data):
	Log('Menus validator')
	if hasattr(data, 'menus'):
		for menuId in data.menus:
			menu = data.menus[menuId]
			menu.validate()
			__Check.PrefabAssetExists(menu.prefabPath, 'menu <%s>' % menuId)
			if menu.backgroundImage != None:
				__Check.ImageAssetExists(menu.backgroundImage, 'menu <%s>' % menuId)

def Rarities(data):
	Log('Rarities validator')
	if hasattr(data, 'rarities'):
		for rarityId in data.rarities:
			rarity = data.rarities[rarityId]
			rarity.validate()
			__Check.ImageAssetExists(rarity.iconFramePath, 'rarity <%s>' % rarityId)
			__Check.ImageAssetExists(rarity.gearIconFramePath, 'rarity <%s>' % rarityId)

def Achievements(data):
	Log('Achievements validator')
	for achievementId in data.quests:
		achievement = data.quests[achievementId]
		achievement.validate()
		if achievement.iconImage != None:
			__Check.ImageAssetExists(achievement.iconImage, 'achievement <%s>' % achievementId)

def TrainingMethods(data):
	Log('TrainingMethods validator')
	for trainingMethodId in data.trainingMethods:
		trainingMethod = data.trainingMethods[trainingMethodId]
		trainingMethod.validate()
		__Check.ImageAssetExists(trainingMethod.icon, 'trainingMethod <%s>' % trainingMethodId)

def RaidLeagues(data):
	Log('RaidLeagues validator')
	for raidLeagueId in data.raidLeagues:
		raidLeague = data.raidLeagues[raidLeagueId]
		raidLeague.validate()
		if raidLeague.titleImagePath != None:
			__Check.ImageAssetExists(raidLeague.titleImagePath, 'raidLeague <%s>' % raidLeagueId)
		if raidLeague.backgroundImagePath != None:
			__Check.ImageAssetExists(raidLeague.backgroundImagePath, 'raidLeague <%s>' % raidLeagueId)

def Attacks(data):
	Log('Attacks validator')
	if hasattr(data, 'attacks'):
		for attackId in data.attacks:
			attack = data.attacks[attackId]
			attack.validate()
			if attack.launchEffectPrefab != None:
				__Check.AudioAssetExists(attack.launchEffectPrefab, 'attack <%s>' % attackId)
			if attack.prefabPath != None:
				__Check.PrefabAssetExists(attack.prefabPath, 'attack <%s>' % attackId)

def Projectiles(data):
	Log('Projectiles validator')
	if hasattr(data, 'projectiles'):
		for projectileId in data.projectiles:
			projectile = data.projectiles[projectileId]
			projectile.validate()
			if projectile.prefabPath != None:
				__Check.PrefabAssetExists(projectile.prefabPath, 'projectile <%s>' % projectileId)
	# 		if projectile.effectPath != None:
	# 			__Check.PrefabAssetExists(projectile.effectPath, 'projectile <%s>' % projectileId)
	# 		if projectile.targetEffectPath != None:
	# 			__Check.PrefabAssetExists(projectile.targetEffectPath, 'projectile <%s>' % projectileId)
	# 		if projectile.collisionEffectPath != None:
	# 			__Check.PrefabAssetExists(projectile.collisionEffectPath, 'projectile <%s>' % projectileId)
			if projectile.wallEffectPrefabPath != None:
				__Check.PrefabAssetExists(projectile.wallEffectPrefabPath, 'projectile <%s>' % projectileId)
			# these checks are redundant with skill_validators
			__Check.Contains(data.effectLists, projectile.bodyFxListId, 'Projectile <%s> has non-existent bodyFxListId <%s>' % (projectileId, projectile.bodyFxListId))
			if projectile.collisionFxListId != None:
				__Check.Contains(data.effectLists, projectile.collisionFxListId, 'Projectile <%s> has non-existent collisionFxListId <%s>' % (projectileId, projectile.collisionFxListId))
			if projectile.targetFxListId != None:
				__Check.Contains(data.effectLists, projectile.targetFxListId, 'Projectile <%s> has non-existent targetFxListId <%s>' % (projectileId, projectile.targetFxListId))

def BeamProjectiles(data):
	Log('BeamProjectiles validator')
	if hasattr(data, 'beamProjectiles'):
		for beamProjectileId in data.beamProjectiles:
			beamProjectile = data.beamProjectiles[beamProjectileId]
			beamProjectile.validate()
			if beamProjectile.prefabPath != None:
				__Check.PrefabAssetExists(beamProjectile.prefabPath, 'beamProjectile <%s>' % beamProjectileId)
			if beamProjectile.sourceEffectPath != None:
				__Check.PrefabAssetExists(beamProjectile.sourceEffectPath, 'beamProjectile <%s>' % beamProjectileId)
			if beamProjectile.beamEffectPath != None:
				__Check.PrefabAssetExists(beamProjectile.beamEffectPath, 'beamProjectile <%s>' % beamProjectileId)
			if beamProjectile.targetEffectPath != None:
				__Check.PrefabAssetExists(beamProjectile.targetEffectPath, 'beamProjectile <%s>' % beamProjectileId)
# 			if beamProjectile.audioPath != None:
# 				__Check.AudioAssetExists(beamProjectile.audioPath, 'beamProjectile <%s>' % beamProjectileId)

def RadialProjectileAttacks(data):
	Log('RadialProjectileAttacks validator')
	if hasattr(data, 'radialProjectileAttacks'):
		for radialProjectileAttackId in data.radialProjectileAttacks:
			radialProjectileAttack = data.radialProjectileAttacks[radialProjectileAttackId]
			radialProjectileAttack.validate()
# 			if radialProjectileAttack.projectilePrefab != None:
# 				__Check.PrefabAssetExists(radialProjectileAttack.projectilePrefab, 'radialProjectileAttack <%s>' % radialProjectileAttackId)

def LaserAttacks(data):
	Log('LaserAttacks validator')
	if hasattr(data, 'laserAttacks'):
		for laserAttackId in data.laserAttacks:
			laserAttack = data.laserAttacks[laserAttackId]
			laserAttack.validate()
# 			if laserAttack.laserPrefab != None:
# 				__Check.PrefabAssetExists(laserAttack.laserPrefab, 'laserAttack <%s>' % laserAttackId)

def ParticlesAttacks(data):
	Log('ParticlesAttacks validator')
	if hasattr(data, 'particlesAttacks'):
		for particlesAttackId in data.particlesAttacks:
			particlesAttack = data.particlesAttacks[particlesAttackId]
			particlesAttack.validate()
	# 		if particlesAttack.particleSystemPrefab != None:
	# 			__Check.PrefabAssetExists(particlesAttack.particleSystemPrefab, 'particlesAttack <%s>' % particlesAttackId)

def ServerErrorDialogTemplates(data):
	Log('ServerErrorDialogTemplates validator')
	for serverErrorDialogTemplateId in data.serverErrorDialogTemplates:
		serverErrorDialogTemplate = data.serverErrorDialogTemplates[serverErrorDialogTemplateId]
		serverErrorDialogTemplate.validate()
		__Check.PrefabAssetExists(serverErrorDialogTemplate.prefab, 'serverErrorDialogTemplate <%s>' % serverErrorDialogTemplateId)

def GenericDialogTemplates(data):
	Log('GenericDialogTemplates validator')
	for genericDialogTemplateId in data.genericDialogTemplates:
		genericDialogTemplate = data.genericDialogTemplates[genericDialogTemplateId]
		genericDialogTemplate.validate()
		__Check.PrefabAssetExists(genericDialogTemplate.prefab, 'genericDialogTemplate <%s>' % genericDialogTemplateId)

def GenericDialogs(data):
	Log('GenericDialogs validator')
	for genericDialogId in data.genericDialogs:
		genericDialog = data.genericDialogs[genericDialogId]
		genericDialog.validate()
		if genericDialog.okayButtonImage != None:
			__Check.ImageAssetExists(genericDialog.okayButtonImage, 'genericDialog <%s>' % genericDialogId)
		if genericDialog.backgroundImage != None:
			__Check.ImageAssetExists(genericDialog.backgroundImage, 'genericDialog <%s>' % genericDialogId)
		if genericDialog.featureImage != None:
			__Check.ImageAssetExists(genericDialog.featureImage, 'genericDialog <%s>' % genericDialogId)
		if genericDialog.secondButtonImage != None:
			__Check.ImageAssetExists(genericDialog.secondButtonImage, 'genericDialog <%s>' % genericDialogId)
		if genericDialog.secondFeatureImage != None:
			__Check.ImageAssetExists(genericDialog.secondFeatureImage, 'genericDialog <%s>' % genericDialogId)

def GuildEmblems(data):
	Log('GuildEmblems validator')
	for guildEmblemId in data.guildEmblems:
		guildEmblem = data.guildEmblems[guildEmblemId]
		guildEmblem.validate()
		__Check.ImageAssetExists(guildEmblem.image, 'guildEmblem <%s>' % guildEmblemId)

def GuildFrames(data):
	Log('GuildFrames validator')
	for guildFrameId in data.guildFrames:
		guildFrame = data.guildFrames[guildFrameId]
		guildFrame.validate()
		__Check.ImageAssetExists(guildFrame.image, 'guildFrame <%s>' % guildFrameId)

def UserIcons(data):
	Log('UserIcons validator')
	for userIconId in data.userIcons:
		userIcon = data.userIcons[userIconId]
		userIcon.validate()
		__Check.ImageAssetExists(userIcon.image, 'userIcon <%s>' % userIconId)

def UserFrames(data):
	Log('UserFrames validator')
	for userFrameId in data.userFrames:
		userFrame = data.userFrames[userFrameId]
		userFrame.validate()
		__Check.ImageAssetExists(userFrame.image, 'userFrame <%s>' % userFrameId)

__validators = [SimplePopupTemplates,
				SimplePopups,
				GiftMessageTemplates,
				GiftMessages,
				GiftMessagePopupTempates,
				GiftMessagePopups,
				OfferPackShopItemTemplates,
				OfferPackShopItems,
				OfferPackZoomItemTemplates,
				OfferPackZoomItems,
				Enchantments,
				StatBumpers,
				HeroStats,
				HeroStatistics,
				GearItems,
				Menus,
				Rarities,
				Achievements,
				TrainingMethods,
				RaidLeagues,
				Attacks,
				Projectiles,
				BeamProjectiles,
				RadialProjectileAttacks,
				LaserAttacks,
				ParticlesAttacks,
				ServerErrorDialogTemplates,
				GenericDialogTemplates,
				GenericDialogs,
				GuildEmblems,
				GuildFrames,
				UserIcons,
				UserFrames,
				]
