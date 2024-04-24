from __main__ import __Check
from __main__ import __Warn
from __main__ import Log
from __main__ import ConfigModule

def EnemySkills(data):
	Log("Heroes prevalidator ...")
	for heroId in data.heroBodies:
		heroBody = data.heroBodies[heroId]
		heroBody.validate()
		if hasattr(data, 'skills'):
			if heroBody.bodyTypeId == ConfigModule.BodyTypeID.Enemy or heroBody.bodyTypeId == ConfigModule.BodyTypeID.Boss:
				for skillId in heroBody.skillIds:
					if skillId in data.attacks:
						attack = data.attacks[skillId]
	# 					__Check.IsFalse(attack.attackLaunchTypeId == ConfigModule.AttackLaunchTypeID.OnePerTurn, 'Boss or Enemy <%s> cannot have one per turn attacks (%s)' % (heroId, skillId))

def EnemiesCannotHaveBumpCombos(data):
	Log("HeroesCannotHaveBumpCombos postvalidator ...")
	for heroId in data.heroBodies:
		heroBody = data.heroBodies[heroId]
		heroBody.validate()
		if hasattr(data, 'skills'):
			if heroBody.bodyTypeId == ConfigModule.BodyTypeID.Enemy or heroBody.bodyTypeId == ConfigModule.BodyTypeID.Boss:
				for skillId in heroBody.skillIds:
					if skillId in data.skills:
						skill = data.skills[skillId]
						__Check.IsFalse(skill.skillTypeId == ConfigModule.SkillTypeID.BumpCombo, "<%s> : Enemies and Bosses cannot have Bump Combos <%s>" % (heroId, skillId))


__validators = [EnemySkills, EnemiesCannotHaveBumpCombos]
