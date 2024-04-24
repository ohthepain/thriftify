from __main__ import __Check
from __main__ import __Warn
from __main__ import Log

def Camps(data):
	Log("Camps postvalidator ...")
	for trainingMethodLink in data.trainingMethodLinks:
		trainingMethodId = trainingMethodLink.trainingMethodId
		__Check.Contains(data.trainingMethods, trainingMethodId, 'training method <%s> does not exist for a trainingMethodLink' % (trainingMethodId))

__validators = [Camps]
