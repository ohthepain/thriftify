#
# MUTATORS
#
# Where the only rule is ...
#
# Mutators cannot consume any mutated data!!! This is because their execution order is undefined.
#
# don't forget to add your mutator script to __init__.py
#

from xl2thrift.mutate import Log

def SkillLevelUpGoldCost(data):
	Log("SkillLevelUpGoldCost mutator ...")
	for skillLevelUpCostEntry in data.skillLevelUpCostEntries:
		levelNum = skillLevelUpCostEntry.levelNum
		goldCost = skillLevelUpCostEntry.levelUpGoldCost
		if data.skillLevelUpGoldCosts == None:
			data.skillLevelUpGoldCosts = []
		while len(data.skillLevelUpGoldCosts) <= levelNum:
			data.skillLevelUpGoldCosts.append(-1)
		data.skillLevelUpGoldCosts[levelNum] = goldCost

	# erase source table
	data.skillLevelUpCostEntries = None

def SkillSlotMinimumLevels(data):
	Log("SkillSlotMinimumLevels mutator ...")
	for skillSlotMinLevelEntry in data.skillSlotMinLevelEntries:
		slotNum = skillSlotMinLevelEntry.slotNum
		minLevel = skillSlotMinLevelEntry.minLevel
		if data.skillSlotMinimumLevels == None:
			data.skillSlotMinimumLevels = []
		while len(data.skillSlotMinimumLevels) <= slotNum:
			data.skillSlotMinimumLevels.append(-1)
		data.skillSlotMinimumLevels[slotNum] = minLevel

	# erase source table
	data.skillSlotMinLevelEntries = None

def SkillStatProfileEntries(data):
	Log("SkillStatProfileEntries mutator ...")
	if hasattr(data, 'skillStatProfileEntries'):
		for skillStatProfileEntry in data.skillStatProfileEntries:
			skillStatProfileId = skillStatProfileEntry.skillStatProfileId
			skillStatProfile = data.skillStatProfiles[skillStatProfileId]
			if skillStatProfile.skillStatProfileEntries == None:
				skillStatProfile.skillStatProfileEntries = []
			skillStatProfile.skillStatProfileEntries.append(skillStatProfileEntry)

		# erase source table
		data.skillStatProfileEntries = None

__mutators = [SkillLevelUpGoldCost, SkillSlotMinimumLevels, SkillStatProfileEntries]
