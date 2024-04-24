from __main__ import __Check
from __main__ import __Warn
from __main__ import Log

def TrainingMethods(data):
	Log("TrainingMethods prevalidator ...")
	for trainingMethodId in data.trainingMethods:
		trainingMethod = data.trainingMethods[trainingMethodId]
		trainingMethod.validate()
		__Check.IsFalse(hasattr(trainingMethod, 'unlockTrainingCampLevel'), 'TrainingMethod <%s>: Do not specify unlockTrainingCampLevel in the method sheet - use the link sheet instead' % (trainingMethodId))
		__Check.IsTrue(len(trainingMethod.rarities) == len(trainingMethod.rarityDistributions), 'TrainingMethod <%s>: Rarities and Rarity Distributions list must have same length' % (trainingMethodId))
# 		__Check.IsTrue(trainingMethod.affinities == None or len(trainingMethod.rarities) == len(trainingMethod.affinities), 'TrainingMethod <%s>: Affinities list must be empty or same length as rarities' % trainingMethodId)

__validators = [TrainingMethods]

