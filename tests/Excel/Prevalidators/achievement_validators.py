from __main__ import __Check
from __main__ import __Warn
from __main__ import Log

def Achievements(data):
	Log("Achievements prevalidator ...")
	for achievementId in data.quests:
		quest = data.quests[achievementId]
		for achievementEventId in quest.achievementEventIds:
			prefix = "UnlockSkill "
			if achievementEventId.startswith(prefix):
				skillId = achievementEventId[len(prefix):]
				if hasattr(data, "skills"):
					__Check.Contains(data.skills, skillId, 'Quest <%s> refers to an undefined skill <%s>' % (achievementId, skillId))
			__Check.IsTrue(len(quest.rewardCurrencies) == len(quest.rewardCurrencyCounts), 'Quest <%s> reward currency list reward counts list must be the same length' % (achievementId))

__validators = [Achievements]

