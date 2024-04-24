# don't forget to add your mutator script to __init__.py

from __main__ import Log

def HeroLevelXpMutator(data):
	Log("HeroLevelXpMutator mutator ...")
	for heroLevelXp in data.heroLevelXp:
# 		heroLevelXp.commonXpByEvo = [heroLevelXp.commonXpEvo1,heroLevelXp.commonXpEvo2,heroLevelXp.commonXpEvo3]
# 		heroLevelXp.rareXpByEvo = [heroLevelXp.rareXpEvo1,heroLevelXp.rareXpEvo2,heroLevelXp.rareXpEvo3,heroLevelXp.rareXpEvo4]
# 		heroLevelXp.epicXpByEvo = [heroLevelXp.epicXpEvo1,heroLevelXp.epicXpEvo2,heroLevelXp.epicXpEvo3,heroLevelXp.epicXpEvo4]
		if heroLevelXp.xpByEvoByRarity == None:
			heroLevelXp.xpByEvoByRarity = [
				[heroLevelXp.commonXpEvo1,heroLevelXp.commonXpEvo2],
				[heroLevelXp.uncommonXpEvo1,heroLevelXp.uncommonXpEvo2,heroLevelXp.uncommonXpEvo3],
				[heroLevelXp.rareXpEvo1,heroLevelXp.rareXpEvo2,heroLevelXp.rareXpEvo3,heroLevelXp.rareXpEvo4],
				[heroLevelXp.epicXpEvo1,heroLevelXp.epicXpEvo2,heroLevelXp.epicXpEvo3,heroLevelXp.epicXpEvo4],
			]
			heroLevelXp.commonXpEvo1 = None
			heroLevelXp.commonXpEvo2 = None
			heroLevelXp.commonXpEvo3 = None
			heroLevelXp.uncommonXpEvo1 = None
			heroLevelXp.uncommonXpEvo2 = None
			heroLevelXp.uncommonXpEvo3 = None
			heroLevelXp.rareXpEvo1 = None
			heroLevelXp.rareXpEvo2 = None
			heroLevelXp.rareXpEvo3 = None
			heroLevelXp.rareXpEvo4 = None
			heroLevelXp.epicXpEvo1 = None
			heroLevelXp.epicXpEvo2 = None
			heroLevelXp.epicXpEvo3 = None
			heroLevelXp.epicXpEvo4 = None

__mutators = [HeroLevelXpMutator]
