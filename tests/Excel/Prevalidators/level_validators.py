from __main__ import __Check
from __main__ import __Warn
from __main__ import ConfigModule
from __main__ import Log

def Levels(data):
	Log("Levels prevalidator ...")
	for levelId in data.levels:
		level = data.levels[levelId]
		level.validate()
# 		campaignId = level.campaignId
# 		__Check.IsTrue(campaignId in data.campaigns, "Level '%s' has undefined campaign")
# 		__Check.ListsAreSameLength(level.items1, level.parms1, 'Level <%s>: items1 and parms1 list must have same length' % (levelId))
# 		__Check.ListsAreSameLength(level.items2, level.parms2, 'Level <%s>: items2 and parms2 list must have same length' % (levelId))
# 		__Check.ListsAreSameLength(level.items3, level.parms3, 'Level <%s>: items3 and parms3 list must have same length' % (levelId))
# 		__Check.ListsAreSameLength(level.items4, level.parms4, 'Level <%s>: items4 and parms4 list must have same length' % (levelId))
# 		__Check.ListsAreSameLength(level.items5, level.parms5, 'Level <%s>: items5 and parms5 list must have same length' % (levelId))
# 		__Check.ListsAreSameLength(level.items6, level.parms6, 'Level <%s>: items6 and parms6 list must have same length' % (levelId))
# 		__Check.ListsAreSameLength(level.items7, level.parms7, 'Level <%s>: items7 and parms7 list must have same length' % (levelId))
# 		__Check.ListsAreSameLength(level.items8, level.parms8, 'Level <%s>: items8 and parms8 list must have same length' % (levelId))
		if level.items1 != None:
			for gearItemId in level.items1:
				__Check.IsTrue(gearItemId in data.gearItems or gearItemId in data.currencies, 'Level <%s>: gearItemId is not defined, level %s' % (gearItemId, levelId))
		if level.items2 != None:
			for gearItemId in level.items2:
				__Check.IsTrue(gearItemId in data.gearItems or gearItemId in data.currencies, 'Level <%s>: gearItemId is not defined, level %s' % (gearItemId, levelId))
		if level.items3 != None:
			for gearItemId in level.items3:
				__Check.IsTrue(gearItemId in data.gearItems or gearItemId in data.currencies, 'Level <%s>: gearItemId is not defined, level %s' % (gearItemId, levelId))
		if level.items4 != None:
			for gearItemId in level.items4:
				__Check.IsTrue(gearItemId in data.gearItems or gearItemId in data.currencies, 'Level <%s>: gearItemId is not defined, level %s' % (gearItemId, levelId))
		if level.items5 != None:
			for gearItemId in level.items5:
				__Check.IsTrue(gearItemId in data.gearItems or gearItemId in data.currencies, 'Level <%s>: gearItemId is not defined, level %s' % (gearItemId, levelId))
		if level.items6 != None:
			for gearItemId in level.items6:
				__Check.IsTrue(gearItemId in data.gearItems or gearItemId in data.currencies, 'Level <%s>: gearItemId is not defined, level %s' % (gearItemId, levelId))
		if level.items7 != None:
			for gearItemId in level.items7:
				__Check.IsTrue(gearItemId in data.gearItems or gearItemId in data.currencies, 'Level <%s>: gearItemId is not defined, level %s' % (gearItemId, levelId))
		if level.items8 != None:
			for gearItemId in level.items8:
				__Check.IsTrue(gearItemId in data.gearItems or gearItemId in data.currencies, 'Level <%s>: gearItemId is not defined, level %s' % (gearItemId, levelId))

def SpawnPoints(data):
	Log("SpawnPoints prevalidator ...")
	if hasattr(data, 'enemySpawnPoints'):
		for enemySpawnPoint in data.enemySpawnPoints:
			evolutionLevel = enemySpawnPoint.evolutionLevel
			heroId = enemySpawnPoint.heroId
			__Check.IsTrue(enemySpawnPoint.attackGroup == None or enemySpawnPoint.attackGroup < 10, 'Enemy spawn point <%s>: Attack group number <%s> must be an integer less than 10' % (enemySpawnPoint.levelSceneId, enemySpawnPoint.attackGroup))
			if enemySpawnPoint.spawnTypeId == ConfigModule.SpawnTypeID.Respawn:
				__Check.IsTrue(len(enemySpawnPoint.spawnParams) == 2, 'Enemy spawn point <%s>.<%s> is respawn, so it must have 2 Spawn Params values' % (enemySpawnPoint.levelSceneId, heroId))
				__Check.IsFalse(enemySpawnPoint.attackGroup == 0 and enemySpawnPoint.attackWait != 0, 'Enemy spawn point in scene <%s>: attack group 0 cannot have a delay' % (enemySpawnPoint.levelSceneId))
			__Check.Contains(data.heroBodies, heroId, "Enemy spawn point for level scene <%s> has undefined hero <%s>" % (enemySpawnPoint.levelSceneId, heroId))
			if heroId in data.heroBodies:
				hero = data.heroBodies[heroId]
				rarity = data.rarities[hero.rarityId]
				maxEvolutionLevel = rarity.heroMaxEvolutionLevel
				__Check.IsTrue(hero.bodyTypeId != ConfigModule.BodyTypeID.Hero or evolutionLevel <= maxEvolutionLevel, 'Enemy spawn point <%s> evolution level is too high for non-enemy hero <%s>' % (enemySpawnPoint.levelSceneId, heroId))

def LevelScenes(data):
	Log("LevelScenes prevalidator ...")
	if hasattr(data, 'levelScenes'):
		for levelSceneId in data.levelScenes:
			levelScene = data.levelScenes[levelSceneId]
			__Check.AssetExists(levelScene.levelPrefabPath, 'LevelScene <%s>' % levelSceneId)
# 			__Check.ImageAssetExists(levelScene.backgroundImage, 'LevelScene <%s>' % levelSceneId)

__validators = [Levels, LevelScenes, SpawnPoints]
