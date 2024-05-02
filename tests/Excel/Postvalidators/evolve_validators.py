from xl2thrift.validate import __Check
from xl2thrift.validate import __Warn
from xl2thrift.validate import Log

def EvolutionTables(data):
	Log("hero evolve pre-validators")
	for evolutionProfileId in data.evolutionProfiles:
# 		print('validate %s' % (evolutionProfileId))
		evolutionProfile = data.evolutionProfiles[evolutionProfileId]
		__Check.Exists(evolutionProfile.evolutionLevelProfiles, 'evolutionLevelProfiles doesnt exist for evolutionProfile %s' % (evolutionProfile.evolutionProfileId))
		__Check.NotEmptyList(evolutionProfile.evolutionLevelProfiles, 'evolutionLevelProfiles list is empty')
# 		print '\nevolutionProfile %s:' % evolutionProfileId
		for evolutionLevelProfile in evolutionProfile.evolutionLevelProfiles:
# 			print '\tevolutionLevelProfileId %s' % (evolutionLevelProfile.evolutionLevelProfileId)
			for gearItemId in evolutionLevelProfile.gearItemIds:
				__Check.Contains(data.gearItems, gearItemId, 'gear item <%s> does not exist for evolution level profile <%s>' % (gearItemId, evolutionLevelProfile.evolutionLevelProfileId))

__validators = [EvolutionTables]
