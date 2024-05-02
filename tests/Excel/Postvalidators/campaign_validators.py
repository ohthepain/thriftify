from xl2thrift.validate import __Check
from xl2thrift.validate import __Warn
from xl2thrift.validate import Log

def EdgeElementEntries(data):
	Log("EdgeElementEntries postvalidator ...")
	if hasattr(data, 'levelScenes'):
		for levelSceneId in data.levelScenes:
			levelScene = data.levelScenes[levelSceneId]
			edgeElementsProfileId = levelScene.edgeElementsProfileId
			if edgeElementsProfileId:
				__Check.Contains(data.edgeElementsProfiles, edgeElementsProfileId, 'level scene <%s> refers to a non-existant edge element profile %s' % (levelSceneId, edgeElementsProfileId))

__validators = [EdgeElementEntries]
