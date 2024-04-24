from __main__ import __Check
from __main__ import __Warn
from __main__ import ConfigModule
from __main__ import Log

def HeroSkillIcons(data):
	Log("HeroSkillIcons prevalidator ...")
	for heroSkillIconId in data.heroSkillIcons:
		heroSkillIcon = data.heroSkillIcons[heroSkillIconId]
		__Check.PrefabAssetExists(heroSkillIcon.prefabPath, 'HeroSkillIcon <%s>' % (heroSkillIconId))
		__Check.ImageAssetExists(heroSkillIcon.iconPath, 'HeroSkillIcon <%s>' % (heroSkillIconId))
		__Check.ImageAssetExists(heroSkillIcon.iconDisabledPath, 'HeroSkillIcon <%s>' % (heroSkillIconId))
# 		__Check.ImageAssetExists(heroSkillIcon.activeBorderImagePath, 'HeroSkillIcon <%s>' % (heroSkillIconId))

def Skills(data):
	Log("Skills prevalidator ...")
	if hasattr(data, 'skills'):
		for skillId in data.skills:
			skill = data.skills[skillId]
			skill.validate()
			__Check.IsTrue(hasattr(skill, 'heroSkillIconId'), 'Skill <%s>: Skill has no heroSkillIconId' % (skillId))
			__Check.IsTrue(hasattr(skill, 'skillTypeId'), 'Skill <%s>: Skill has no skilltypeid' % (skillId))
			__Check.IsTrue(hasattr(skill, 'hintSkillStatProfileId'), 'Skill <%s>: Skill has no hintSkillStatProfileId' % (skillId))
			__Check.IsTrue(skill.heroSkillIconId in data.heroSkillIcons, 'Skill %s has an undefined heroSkillIconId' % (skillId))
			__Check.IsTrue(skill.hintSkillStatProfileId in data.skillStatProfiles, 'Skill %s has an undefined hintSkillStatProfile' % (skillId))
	# 		__Check.IsTrue(skillId in data.skillStatProfiles, "Skill '%s' has no skillStatProfile" % (skillId))
			if skill.iconImagePath != None:
				__Check.ImageAssetExists(skill.iconImagePath, 'Skill <%s>' % (skillId))
			if skill.skillTypeId == ConfigModule.SkillTypeID.Enchantment:
				__Check.IsTrue(skillId in data.enchantments, 'Skill <%s> is of type Enchantment but no Enchantment object found' % (skillId))
			elif skill.skillTypeId == ConfigModule.SkillTypeID.PassiveSkill:
				__Check.IsTrue(skillId in data.passiveSkills, 'Skill <%s> is of type PassiveSkill but no PassiveSkill object found' % (skillId))
			elif skill.skillTypeId == ConfigModule.SkillTypeID.BumpCombo:
				__Check.IsTrue(skillId in data.attacks, 'Skill <%s> is of type BumpCombo but no Attack object found' % (skillId))
			elif skill.skillTypeId == ConfigModule.SkillTypeID.Attack:
				__Check.IsTrue(skillId in data.attacks, 'Skill <%s> is of type Attack but no attack object found' % (skillId))

def Enchantments(data):
	Log("Enchantments prevalidator ...")
	if hasattr(data, 'enchantments'):
		for enchantmentId in data.enchantments:
			enchantment = data.enchantments[enchantmentId]
			enchantment.validate()
			__Check.IsTrue(hasattr(enchantment, 'skillStatProfileId'), 'Enchantment <%s>: Enchantment has no skillStatProfileId' % (enchantmentId))
			__Check.IsTrue(enchantmentId in data.skills, "Enchantment '%s' has an undefined skill" % (enchantmentId))
			__Check.IsTrue(enchantment.skillStatProfileId in data.skillStatProfiles, 'Enchantment %s has an undefined skillStatProfile' % (enchantmentId))
			if enchantment.enchantAudioPath != None:
				__Check.AudioAssetExists(enchantment.enchantAudioPath, 'Enchantment <%s>' % (enchantmentId))
			if enchantment.actionAudioPath != None:
				__Check.AudioAudioAssetExists(enchantment.actionAudioPath, 'Enchantment <%s>' % (enchantmentId))
			if enchantment.effectPrefab != None:
				__Check.PrefabAssetExists(enchantment.effectPrefab, 'Enchantment <%s>' % (enchantmentId))
			if enchantment.actionPrefab != None:
				__Check.PrefabAssetExists(enchantment.actionPrefab, 'Enchantment <%s>' % (enchantmentId))
			if enchantment.prefabPath != None:
				__Check.PrefabAssetExists(enchantment.prefabPath, 'Enchantment <%s>' % (enchantmentId))
			if enchantment.badgeImage != None:
				__Check.ImageAssetExists(enchantment.badgeImage, 'Enchantment <%s>' % (enchantmentId))

def BumpCombos(data):
	Log("BumpCombos prevalidator ...")
	if hasattr(data, 'attacks'):
		for bumpComboId in data.attacks:
			bumpCombo = data.attacks[bumpComboId]
			bumpCombo.validate()
	# 		__Check.IsTrue(hasattr(bumpCombo, 'skillStatProfileId'), 'BumpCombo <%s>: bumpCombo has no skillStatProfileId' % (bumpComboId))
			__Check.IsTrue(bumpComboId in data.skills, "BumpCombo '%s' has an undefined skill" % (bumpComboId))
	# 		__Check.IsTrue(bumpCombo.skillStatProfileId in data.skillStatProfiles, 'BumpCombo %s has an undefined skillStatProfile' % (bumpComboId))

def Projectiles(data):
	Log("Projectiles prevalidator ...")
	if hasattr(data, 'projectiles'):
		for projectileId in data.projectiles:
			projectile = data.projectiles[projectileId]
			projectile.validate()
			__Check.IsTrue(hasattr(projectile, 'skillStatProfileId'), 'Projectile <%s>: projectile has no skillStatProfileId' % (projectileId))
			__Check.IsTrue(projectile.skillStatProfileId in data.skillStatProfiles, 'Projectile %s has an undefined skillStatProfile' % (projectileId))
			__Check.IsFalse(projectile.lifespanTypeId == ConfigModule.LifespanTypeID.BoundaryCollision and projectile.motionTypeId == ConfigModule.MotionTypeID.WallBounce, 'Projectile %s lifespan is BoundaryCollision but MotionTypeID is WallBounce' % (projectileId))
			__Check.PrefabAssetExists(projectile.prefabPath, 'Projectile <%s>' % projectileId)
			__Check.Contains(data.effectLists, projectile.bodyFxListId, 'Projectile <%s> has non-existent bodyFxListId <%s>' % (projectileId, projectile.bodyFxListId))
			if projectile.collisionFxListId != None:
				__Check.Contains(data.effectLists, projectile.collisionFxListId, 'Projectile <%s> has non-existent collisionFxListId <%s>' % (projectileId, projectile.collisionFxListId))
			if projectile.targetFxListId != None:
				__Check.Contains(data.effectLists, projectile.targetFxListId, 'Projectile <%s> has non-existent targetFxListId <%s>' % (projectileId, projectile.targetFxListId))
	# 		__Check.PrefabAssetExists(projectile.effectPath, 'Projectile <%s>' % projectileId)
	# 		__Check.PrefabAssetExists(projectile.collisionEffectPath, 'Projectile <%s>' % projectileId)
	# 		if projectile.targetEffectPath != None:
	# 			__Check.PrefabAssetExists(projectile.targetEffectPath, 'Projectile <%s>' % projectileId)
	# 		if projectile.targetEffectPath != None:
	# 			__Check.PrefabAssetExists(projectile.targetEffectPath, 'Projectile <%s>' % projectileId)
			if projectile.wallEffectPrefabPath != None:
				__Check.PrefabAssetExists(projectile.wallEffectPrefabPath, 'Projectile <%s>' % projectileId)
	# 		if projectile.magicDamageAudioPath != None:
	# 			__Check.AudioAssetExists(projectile.magicDamageAudioPath, 'Projectile <%s>' % projectileId)
	# 		if projectile.wallCollisionAudioPath != None:
	# 			__Check.AudioAssetExists(projectile.wallCollisionAudioPath, 'Projectile <%s>' % projectileId)
			if projectile.damageSoundId != None:
				__Check.IsTrue(projectile.damageSoundId in data.soundClipLists or projectile.damageSoundId in data.soundClips, 'Projectile %s has an undefined sound or sound clip id' % (projectile.damageSoundId))
			if projectile.collisionSoundId != None:
				__Check.IsTrue(projectile.collisionSoundId in data.soundClipLists or projectile.collisionSoundId in data.soundClips, 'Projectile %s has an undefined sound or sound clip id' % (projectile.collisionSoundId))

def BeamProjectiles(data):
	Log("BeamProjectiles prevalidator ...")
	if hasattr(data, 'beamProjectiles'):
		for projectileId in data.beamProjectiles:
			projectile = data.beamProjectiles[projectileId]
			projectile.validate()
			__Check.IsTrue(hasattr(projectile, 'skillStatProfileId'), 'Projectile <%s>: projectile has no skillStatProfileId' % (projectileId))
			__Check.IsTrue(projectile.skillStatProfileId in data.skillStatProfiles, 'Projectile %s has an undefined skillStatProfile' % (projectileId))
			__Check.PrefabAssetExists(projectile.prefabPath, 'BeamProjectile <%s>' % projectileId)
			__Check.PrefabAssetExists(projectile.sourceEffectPath, 'BeamProjectile <%s>' % projectileId)
			__Check.PrefabAssetExists(projectile.beamEffectPath, 'BeamProjectile <%s>' % projectileId)
			__Check.PrefabAssetExists(projectile.targetEffectPath, 'BeamProjectile <%s>' % projectileId)
# 			__Check.AudioAssetExists(projectile.audioPath, 'BeamProjectile <%s>' % projectileId)

def ParticlesAttacks(data):
	Log("ParticlesAttacks prevalidator ...")
	if hasattr(data, 'particlesAttacks'):
		for attackId in data.particlesAttacks:
			particlesAttack = data.particlesAttacks[attackId]
			particlesAttack.validate()
			__Check.IsTrue(hasattr(particlesAttack, 'skillStatProfileId'), 'ParticlesAttack <%s>: has no skillStatProfileId' % (attackId))
			__Check.IsTrue(hasattr(particlesAttack, 'effectListId'), 'ParticlesAttack <%s>: has no effectListId' % (attackId))
			__Check.IsTrue(particlesAttack.skillStatProfileId in data.skillStatProfiles, 'ParticlesAttack %s has an undefined skillStatProfile' % (attackId))
			__Check.IsTrue(particlesAttack.effectListId in data.effectLists, 'ParticlesAttack %s has an undefined effect list' % (attackId))

def LaserAttacks(data):
	Log("LaserAttacks prevalidator ...")
	if hasattr(data, 'laserAttacks'):
		for laserAttackId in data.laserAttacks:
			laserAttack = data.laserAttacks[laserAttackId]
			laserAttack.validate()
			projectileId = laserAttack.projectileId
			__Check.IsTrue(projectileId in data.projectiles, 'LaserAttack %s has an undefined projectile %s' % (laserAttackId, projectileId))
			if projectileId in data.projectiles:
				if laserAttack.degreesSweep != None:
					projectile = data.projectiles[projectileId]
					__Check.IsTrue(projectile.durationSeconds == None, 'LaserAttack %s has degreesSweep so projectile %s cannot have duration' % (laserAttackId, projectileId))

def StatBumpers(data):
	Log("StatBumpers prevalidator ...")
	if hasattr(data, 'statBumpers'):
		for attackId in data.statBumpers:
			statBumper = data.statBumpers[attackId]
			statBumper.validate()
			__Check.IsTrue(hasattr(statBumper, 'skillStatProfileId'), 'StatBumper <%s>: has no skillStatProfileId' % (attackId))
			__Check.IsTrue(statBumper.skillStatProfileId in data.skillStatProfiles, 'StatBumper %s has an undefined skillStatProfile' % (attackId))

def SkillStatProfileEntries(data):
	Log("SkillStatProfileEntries prevalidator ...")
	if hasattr(data, 'skillStatProfileEntries'):
		for skillStatProfileEntry in data.skillStatProfileEntries:
			skillStatProfileId = skillStatProfileEntry.skillStatProfileId
			__Check.IsTrue(skillStatProfileId in data.skillStatProfiles, 'SkillStatProfileEntry %s has an undefined skillStatProfile' % (skillStatProfileId))

def RadialProjectileAttacks(data):
	Log("RadialProjectileAttacks prevalidator ...")
	if hasattr(data, 'radialProjectileAttacks'):
		for radialProjectileAttackId in data.radialProjectileAttacks:
			radialProjectileAttack = data.radialProjectileAttacks[radialProjectileAttackId]
			projectileId = radialProjectileAttack.projectileId
			__Check.Contains(data.projectiles, projectileId, "Radial Projectile Attack <%s> has undefined projectild id <%s>" % (radialProjectileAttackId, projectileId))

def Attacks(data):
	Log("Attacks prevalidator ...")
	if hasattr(data, 'attacks'):
		for attackId in data.attacks:
			attack = data.attacks[attackId]
			__Check.IsTrue(attackId in data.radialProjectileAttacks
						or attackId in data.shootAttacks
						or attackId in data.beamAttacks
						or attackId in data.particlesAttacks
						or attackId in data.statBumpers
						or attackId in data.radialProjectileAttacks
						or attackId in data.laserAttacks
						or attackId in data.enchantments, "Attack <%s> does not exist in any specific Attack or Enchantment form" % (attackId))

__validators = [HeroSkillIcons, Skills, Attacks, RadialProjectileAttacks, Enchantments, BumpCombos, Projectiles, BeamProjectiles, ParticlesAttacks, LaserAttacks, StatBumpers, SkillStatProfileEntries]
