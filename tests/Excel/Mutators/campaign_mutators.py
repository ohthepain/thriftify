#
# MUTATORS
#
# Where the only rule is ...
#
# Mutators cannot consume any mutated data!!! This is because their execution order is undefined.
#
# don't forget to add your mutator script to __init__.py
#

from __main__ import ConfigModule
from xl2thrift.mutate import Log

def CreateUnlockedHeroesTables(data):
	#print("CreateUnlockedHeroesTables mutator ...")
	# Hero CampaignID unlockCampaignId
	# Campaign: list<shared.HeroID> unlockedHeroIds
	#print(data.heroes)
	for heroId in data.heroBodies:
		hero = data.heroBodies[heroId]
		##print("unlock at " + hero.unlockCampaignId)
		if hero.unlockCampaignId != None:
			campaign = data.campaigns[hero.unlockCampaignId]
			#print(campaign)
			if campaign.unlockedHeroIds == None:
				campaign.unlockedHeroIds = []
			campaign.unlockedHeroIds.append(heroId)

def EnemySpawnPoints(data):
	Log("EnemySpawnPoints mutator ...")
	if hasattr(data, 'enemySpawnPoints'):
		for enemySpawnPoint in data.enemySpawnPoints:
			enemySpawnPoint.heroState = ConfigModule.HeroState()
			enemySpawnPoint.heroState.heroId = enemySpawnPoint.heroId
	# 		TODO: I am not sure what to do here
			enemySpawnPoint.heroState.heroStateId = None
			enemySpawnPoint.heroState.slotStatus = enemySpawnPoint.slotStatus
			enemySpawnPoint.heroState.skillLevels = enemySpawnPoint.skillLevels
			enemySpawnPoint.heroState.evolutionLevel = enemySpawnPoint.evolutionLevel
			heroBody = data.heroBodies[enemySpawnPoint.heroId]
			rarity = heroBody.rarityId
			xp = 0
			level = 0
	# 		print '%s %s %d %d %d' % (enemySpawnPoint.levelSceneId, enemySpawnPoint.heroId, level, rarity, enemySpawnPoint.evolutionLevel)
			while level < enemySpawnPoint.level:
				heroLevelXp = data.heroLevelXp[level]
				xp += heroLevelXp.xpByEvoByRarity[rarity][enemySpawnPoint.evolutionLevel]
				xp += 100
				level += 1
			enemySpawnPoint.heroState.xp = xp

	#         enemySpawnPoint.level = None
	#         enemySpawnPoint.evolutionLevel = None
	#         enemySpawnPoint.skillLevels = None

			levelSceneId = enemySpawnPoint.levelSceneId
			levelScene = data.levelScenes[levelSceneId]
			if levelScene.enemySpawnPoints == None:
				levelScene.enemySpawnPoints = []
			levelScene.enemySpawnPoints.append(enemySpawnPoint)
	data.enemySpawnPoints = None

def CampaignOrder(data):
	#Log("CampaignOrder mutator ...")
	for campaignId in data.campaigns:
		campaign = data.campaigns[campaignId]
		if campaign.order != None:
			if data.campaignOrder == None:
				data.campaignOrder = []
			while len(data.campaignOrder) <= campaign.order:
				data.campaignOrder.append(-1)
			data.campaignOrder[campaign.order] = campaignId

def CampaignLevels(data):
	#Log("CampaignLevels mutator ...")
	for levelId in data.levels:
		##Log("levelId " + levelId)
		level = data.levels[levelId]
		campaignId = level.campaignId
		#Log("campaignId " + campaignId)
# 		if campaignId not in data.campaigns:
# 			exit("Level '%s' has an undefined campaign" % (levelId))
		if campaignId in data.campaigns:
			campaign = data.campaigns[campaignId]
			if campaign.levelIds == None:
				campaign.levelIds = []
			while len(campaign.levelIds) <= level.order:
				campaign.levelIds.append('')
			campaign.levelIds[level.order] = levelId

def LevelScenes(data):
	#Log("LevelScenes mutator ...")
	if hasattr(data, 'levelScenes'):
		for levelSceneId in data.levelScenes:
			##Log("levelSceneId " + levelSceneId)
			levelScene = data.levelScenes[levelSceneId]
			if levelScene.levelId != None:
				levelId = levelScene.levelId
				##Log("levelId " + levelId)
				level = data.levels[levelId]
				if level.levelSceneIds == None:
					level.levelSceneIds = []
				level.levelSceneIds.append(levelSceneId)
				level.levelSceneIds.sort(key=lambda levelSceneId: data.levelScenes[levelSceneId].order)

def EdgeElementEntries(data):
	Log("EdgeElementEntries mutator ...")
	if hasattr(data, 'edgeElementEntries'):
		for edgeElementEntry in data.edgeElementEntries:
			edgeElementsProfileId = edgeElementEntry.edgeElementsProfileId
			if data.edgeElementsProfiles == None:
				data.edgeElementsProfiles = {}
			if not edgeElementsProfileId in data.edgeElementsProfiles:
				data.edgeElementsProfiles[edgeElementsProfileId] = ConfigModule.EdgeElementsProfile()
				data.edgeElementsProfiles[edgeElementsProfileId].edgeElementsProfileId = edgeElementsProfileId
			edgeElementsProfile = data.edgeElementsProfiles[edgeElementsProfileId]
			if edgeElementsProfile.edgeElementEntries == None:
				edgeElementsProfile.edgeElementEntries = []
			edgeElementsProfile.edgeElementEntries.append(edgeElementEntry)

	data.levelSceneEdgeElementEntries = None

__mutators = [CreateUnlockedHeroesTables, EnemySpawnPoints, CampaignOrder, CampaignLevels, LevelScenes, EdgeElementEntries]