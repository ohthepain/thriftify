from __main__ import __Check
from __main__ import __Warn
from __main__ import Log

def EvolutionTables(data):
	Log("EvolutionTables pre-validators")
	for evolutionProfileId in data.evolutionProfiles:
		#print('validate %s' % (evolutionProfileId))
		evolutionProfile = data.evolutionProfiles[evolutionProfileId]

	for evolutionLevelProfileId in data.evolutionLevelProfiles_:
		evolutionLevelProfile = data.evolutionLevelProfiles_[evolutionLevelProfileId]
		if evolutionLevelProfile.gearItemId0 != None:
			__Check.Contains(data.gearItems, evolutionLevelProfile.gearItemId0, 'gear item <%s> does not exist for evolution level profile <%s>' % (evolutionLevelProfile.gearItemId0, evolutionLevelProfileId))
		if evolutionLevelProfile.gearItemId1 != None:
			__Check.Contains(data.gearItems, evolutionLevelProfile.gearItemId1, 'gear item <%s> does not exist for evolution level profile <%s>' % (evolutionLevelProfile.gearItemId1, evolutionLevelProfileId))
		if evolutionLevelProfile.gearItemId2 != None:
			__Check.Contains(data.gearItems, evolutionLevelProfile.gearItemId2, 'gear item <%s> does not exist for evolution level profile <%s>' % (evolutionLevelProfile.gearItemId2, evolutionLevelProfileId))
		if evolutionLevelProfile.gearItemId3 != None:
			__Check.Contains(data.gearItems, evolutionLevelProfile.gearItemId3, 'gear item <%s> does not exist for evolution level profile <%s>' % (evolutionLevelProfile.gearItemId3, evolutionLevelProfileId))
		if evolutionLevelProfile.gearItemId4 != None:
			__Check.Contains(data.gearItems, evolutionLevelProfile.gearItemId4, 'gear item <%s> does not exist for evolution level profile <%s>' % (evolutionLevelProfile.gearItemId4, evolutionLevelProfileId))
		if evolutionLevelProfile.gearItemId5 != None:
			__Check.Contains(data.gearItems, evolutionLevelProfile.gearItemId5, 'gear item <%s> does not exist for evolution level profile <%s>' % (evolutionLevelProfile.gearItemId5, evolutionLevelProfileId))

	for evolutionProfileLevelLink in data.evolutionProfileLevelLinks:
		__Check.Contains(data.evolutionLevelProfiles_, evolutionProfileLevelLink.evolutionLevelProfileId, 'Evolution level profile <%s> does not exist -- sese evolution level profile level links for <%s>' % (evolutionProfileLevelLink.evolutionLevelProfileId, evolutionProfileLevelLink.evolutionProfileId))

__validators = [EvolutionTables]
