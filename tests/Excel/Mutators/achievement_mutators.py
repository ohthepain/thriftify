# don't forget to add your mutator script to __init__.py

from xl2thrift.mutate import Log

# Populate achievementEventHints
def Achievements(data):
	Log("Achievements mutator ...")
	if data.achievementEventIdHints == None:
		data.achievementEventIdHints = {}
	for achievementId in data.quests:
		quest = data.quests[achievementId]
		for achievementEventId in quest.achievementEventIds:
			data.achievementEventIdHints[achievementEventId] = achievementEventId

__mutators = [Achievements]
