# hero_validators.py

from __main__ import __Check
from __main__ import __Warn
from __main__ import ConfigModule
from __main__ import Log

def Heroes(data):
	Log("Heroes prevalidator ...")
	for heroId in data.heroBodies:
		herobody = data.heroBodies[heroId]
		herobody.validate()
# 		__Check.IsValidString(herobody.heroSoundProfileId, 'Hero <%s> has no sound profile' % (heroId))
# 		if hasattr(data, 'heroSoundProfiles'):
		if herobody.heroSoundProfileId != None:
			__Check.Contains(data.heroSoundProfiles, herobody.heroSoundProfileId, 'Hero <%s> has non-existent sound profile <%s>' % (heroId, herobody.heroSoundProfileId))
		__Check.IsValidString(herobody.physicalReactProfileId, 'Hero <%s> has no physical reaction profile' % (heroId))
		if hasattr(data, 'physicsProfiles'):
			__Check.Contains(data.physicsProfiles, herobody.physicalReactProfileId, 'Hero <%s> has non-existent physics profile <%s>' % (heroId, herobody.physicsProfileId))
			__Check.Contains(data.physicsProfiles, herobody.magicReactProfileId, 'Hero <%s> has non-existent magic react profile <%s>' % (heroId, herobody.magicReactProfileId))
		__Check.Contains(data.evolutionProfiles, herobody.evolutionProfileId, 'Hero <%s> has non-existent evolution profile <%s>' % (heroId, herobody.evolutionProfileId))
		__Check.Contains(data.affinities, herobody.affinityId, 'Hero <%s> has non-existent affinity <%s>' % (heroId, herobody.affinityId))
		__Check.Contains(data.strengthProfiles, herobody.strengthProfileId, 'Hero <%s> has non-existent strength profile <%s>' % (heroId, herobody.strengthProfileId))
		if hasattr(data, 'skills'):
			if (herobody.skillId0 != None or herobody.skillId1 != None or herobody.skillId2 != None or herobody.skillId3 != None):
				if herobody.bodyTypeId != ConfigModule.BodyTypeID.Boss:
					if herobody.rarityId == 0:
						__Check.IsValidString(herobody.skillId0, 'Hero <%s> must have 2 skill ids' % (heroId))
						__Check.IsValidString(herobody.skillId1, 'Hero <%s> must have 2 skill ids' % (heroId))
						__Check.IsNotValidString(herobody.skillId2, 'Hero <%s> must have ONLY 2 skill ids' % (heroId))
						__Check.IsNotValidString(herobody.skillId3, 'Hero <%s> must have ONLY 2 skill ids' % (heroId))
					if herobody.rarityId == 1 or herobody.rarityId == 2:
						__Check.IsValidString(herobody.skillId0, 'Hero <%s> must have 3 skill ids' % (heroId))
						__Check.IsValidString(herobody.skillId1, 'Hero <%s> must have 3 skill ids' % (heroId))
						__Check.IsValidString(herobody.skillId2, 'Hero <%s> must have 3 skill ids' % (heroId))
						__Check.IsNotValidString(herobody.skillId3, 'Hero <%s> must have ONLY 3 skill ids' % (heroId))
					if herobody.rarityId >= 3:
						__Check.IsValidString(herobody.skillId0, 'Hero <%s> must have 4 skill ids' % (heroId))
						__Check.IsValidString(herobody.skillId1, 'Hero <%s> must have 4 skill ids' % (heroId))
						__Check.IsValidString(herobody.skillId2, 'Hero <%s> must have 4 skill ids' % (heroId))
						__Check.IsValidString(herobody.skillId3, 'Hero <%s> must have 4 skill ids' % (heroId))

					__Check.Contains(data.skills, herobody.skillId0, 'Skill <%s> does not exist for hero <%s>' % (herobody.skillId0, heroId))
					__Check.Contains(data.skills, herobody.skillId1, 'Skill <%s> does not exist for hero <%s>' % (herobody.skillId1, heroId))
					if herobody.skillId2 != None:
						__Check.Contains(data.skills, herobody.skillId2, 'Skill <%s> does not exist for hero <%s>' % (herobody.skillId2, heroId))
					if herobody.skillId3 != None:
						__Check.Contains(data.skills, herobody.skillId3, 'Skill <%s> does not exist for hero <%s>' % (herobody.skillId3, heroId))

		if herobody.skillIconHolderPrefab != None:
			__Check.PrefabAssetExists(herobody.skillIconHolderPrefab, 'Hero <%s>' % heroId)
		if herobody.bodyCirclePrefab != None:
			__Check.PrefabAssetExists(herobody.bodyCirclePrefab, 'Hero <%s>' % heroId)
		__Check.PrefabAssetExists(herobody.heroPrefab, 'Hero <%s>' % heroId)
		__Check.ImageAssetExists(herobody.cardImage, 'Hero <%s>' % heroId)
		if herobody.bwCardImage != None:
			__Check.ImageAssetExists(herobody.bwCardImage, 'Hero <%s>' % heroId)

def HeroAudio(data):
	Log("HeroAudio prevalidator ...")
	if hasattr(data, 'heroSoundProfiles'):
		for heroSoundProfileId in data.heroSoundProfiles:
			heroSoundProfile = data.heroSoundProfiles[heroSoundProfileId]
			if heroSoundProfile.shootClip != None:
				__Check.AudioAssetExists(heroSoundProfile.shootClip, 'Hero <%s>' % heroSoundProfileId)
			if heroSoundProfile.myTurnClip != None:
				__Check.AudioAssetExists(heroSoundProfile.myTurnClip, 'Hero <%s>' % heroSoundProfileId)
			if heroSoundProfile.deathClip != None:
				__Check.AudioAssetExists(heroSoundProfile.deathClip, 'Hero <%s>' % heroSoundProfileId)
			if heroSoundProfile.energyShotClip != None:
				__Check.AudioAssetExists(heroSoundProfile.energyShotClip, 'Hero <%s>' % heroSoundProfileId)
			if heroSoundProfile.worriedClip != None:
				__Check.AudioAssetExists(heroSoundProfile.worriedClip, 'Hero <%s>' % heroSoundProfileId)
			if heroSoundProfile.shootClip != None:
				__Check.AudioAssetExists(heroSoundProfile.shootClip, 'Hero <%s>' % heroSoundProfileId)
			if heroSoundProfile.aimClip != None:
				__Check.AudioAssetExists(heroSoundProfile.aimClip, 'Hero <%s>' % heroSoundProfileId)
			if heroSoundProfile.hitClip != None:
				__Check.AudioAssetExists(heroSoundProfile.hitClip, 'Hero <%s>' % heroSoundProfileId)
			if heroSoundProfile.physicalDamageClip != None:
				__Check.AudioAssetExists(heroSoundProfile.physicalDamageClip, 'Hero <%s>' % heroSoundProfileId)

__validators = [Heroes, HeroAudio]
