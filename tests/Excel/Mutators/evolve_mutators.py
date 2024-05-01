# don't forget to add your mutator script to __init__.py

import sys as __sys
from xl2thrift.mutate import Log

def EvolutionTables(data):
	Log('EvolutionTables mutators ...')

	for evolutionLevelProfileId in data.evolutionLevelProfiles_:
		evolutionLevelProfile = data.evolutionLevelProfiles_[evolutionLevelProfileId]
# 		print 'evolutionProfileId %s gets gearItemIds and gear item 0 is %s' % (evolutionLevelProfile.evolutionLevelProfileId, evolutionLevelProfile.gearItemId0)
		evolutionLevelProfile.gearItemIds = []
		evolutionLevelProfile.gearItemIds.append(evolutionLevelProfile.gearItemId0)
		evolutionLevelProfile.gearItemIds.append(evolutionLevelProfile.gearItemId1)
		evolutionLevelProfile.gearItemIds.append(evolutionLevelProfile.gearItemId2)
		evolutionLevelProfile.gearItemIds.append(evolutionLevelProfile.gearItemId3)
		if evolutionLevelProfile.gearItemId4 != None:
			evolutionLevelProfile.gearItemIds.append(evolutionLevelProfile.gearItemId4)
		if evolutionLevelProfile.gearItemId5 != None:
			evolutionLevelProfile.gearItemIds.append(evolutionLevelProfile.gearItemId5)
		evolutionLevelProfile.numGearSlots = len(evolutionLevelProfile.gearItemIds)
		evolutionLevelProfile.gearItemId0 = None
		evolutionLevelProfile.gearItemId1 = None
		evolutionLevelProfile.gearItemId2 = None
		evolutionLevelProfile.gearItemId3 = None
		evolutionLevelProfile.gearItemId4 = None
		evolutionLevelProfile.gearItemId5 = None

	for evolutionProfileId in data.evolutionProfiles:
		evolutionProfile = data.evolutionProfiles[evolutionProfileId]
# 		print 'evolutionProfileId %s gets evolutionLevelProfiles' % (evolutionProfile.evolutionProfileId)
		evolutionProfile.evolutionLevelProfiles = []

	for evolutionProfileLevelLink in data.evolutionProfileLevelLinks:
		evolutionProfile = data.evolutionProfiles[evolutionProfileLevelLink.evolutionProfileId]
		evolutionLevelProfile = data.evolutionLevelProfiles_[evolutionProfileLevelLink.evolutionLevelProfileId]
		# cheezy way to resize list if required
		while len(evolutionProfile.evolutionLevelProfiles) <= evolutionProfileLevelLink.evolutionLevelNum:
			evolutionProfile.evolutionLevelProfiles.append(evolutionLevelProfile)
		evolutionProfile.evolutionLevelProfiles[evolutionProfileLevelLink.evolutionLevelNum] = evolutionLevelProfile

	data.evolutionProfileLevelLinks = None

	for evolutionLevelProfileId in data.evolutionLevelProfiles_:
		evolutionLevelProfile = data.evolutionLevelProfiles_[evolutionLevelProfileId]

	data.evolutionLevelProfiles_ = None

__mutators = [EvolutionTables]
