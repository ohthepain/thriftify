from xl2thrift.validate import __Check
from xl2thrift.validate import __Warn
from xl2thrift.validate import Log

def EffectLists(data):
	Log("EffectLists prevalidator ...")
	for effectListEntry in data.effectListEntries:
		effectListId = effectListEntry.effectListId
		__Check.Contains(data.effectLists, effectListId, 'effectListId <%s> does not exist' % (effectListId))
		__Check.PrefabAssetExists(effectListEntry.prefabPath, 'Effect List <%s>' % effectListId)
		if effectListEntry.autoReclaim == True:
			__Check.IsTrue(effectListEntry.poolSize > 0, 'Effect List <%s> - cannot set autoReclaim when Pool Size is zero' % effectListId)

__validators = [EffectLists]

