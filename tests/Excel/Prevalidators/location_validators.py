from xl2thrift.validate import __Check
from xl2thrift.validate import __Warn
from xl2thrift.validate import Log

def Locations(data):
	Log("Locations prevalidator ...")
	for locationId in data.locations:
		location = data.locations[locationId]
		if location.flagImage != None:
			__Check.ImageAssetExists(location.flagImage, 'location <%s>' % locationId)

__validators = [Locations]
