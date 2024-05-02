from xl2thrift.validate import __Check
from xl2thrift.validate import __Warn
from xl2thrift.validate import Log

def RequestInfo(data):
	Log("RequestInfo prevalidator ...")
	for requestUrl in data.requestInfo:
		requestInfo = data.requestInfo[requestUrl]
		requestInfo.validate()
		__Check.IsFalse(requestInfo.userInBody == requestInfo.suppressUserObject, 'RequestInfo <%s>: userInBody must be opposite of suppressUserObject' % (requestUrl))
		__Check.IsFalse(requestInfo.userInBody and requestInfo.responseInBody, 'RequestInfo <%s>: Cannot have userInBody and responseInBody' % (requestUrl))

__validators = [RequestInfo]

