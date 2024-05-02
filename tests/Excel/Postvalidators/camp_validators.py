from xl2thrift.validate import __Check
from xl2thrift.validate import __Warn
from xl2thrift.validate import Log

def Camps(data):
	Log("Camps postvalidator ...")
	for trainingMethodLink in data.trainingMethodLinks:
		trainingMethodId = trainingMethodLink.trainingMethodId
		__Check.Contains(data.trainingMethods, trainingMethodId, 'training method <%s> does not exist for a trainingMethodLink' % (trainingMethodId))

__validators = [Camps]
