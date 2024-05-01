from __main__ import __Check
from __main__ import __Warn
from __main__ import Log
from xl2thrift.mutate import ConfigModule

def __listGearTables():
	# uncomment this if you want to generate loot tables
	#return True
	return False

def BumpComboSkills(data):
	for heroId in data.heroBodies:
		hero = data.heroBodies[heroId]
		if hasattr(hero, 'skillIds'):
			if hero.skillIds == None:
				__Check.IsTrue(hero.bodyTypeId == ConfigModule.BodyTypeID.Trainer, 'Hero <%s>: Heroes with no skills must have BodyTypeId Trainer' % (heroId))
			else:
				for skillId in hero.skillIds:
					skill = data.skills[skillId]
					__Check.Contains(data.skillStatProfiles, skill.hintSkillStatProfileId, 'Skill <%s> hint stat profile <%s> does not exist' % (skillId, skill.hintSkillStatProfileId))
					if skill.skillTypeId == ConfigModule.SkillTypeID.BumpCombo:
						__Check.Contains(data.attacks, skillId, 'Skill <%s> is type BumpCombo but has no corresponding Attack object' % (skillId))
					if skill.skillTypeId == ConfigModule.SkillTypeID.Enchantment:
						__Check.Contains(data.enchantments, skillId, 'Skill <%s> is type Enchantment but has no corresponding Enchantment object' % (skillId))

__validators = [BumpComboSkills]
