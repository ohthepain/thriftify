from __main__ import __Check
from __main__ import __Warn
from __main__ import Log
# from __main__ import ConfigModule

def Locations(data):
	Log("Locations prevalidator ...")
	for locationId in data.locations:
		location = data.locations[locationId]
		if location.flagImage != None:
			__Check.ImageAssetExists(location.flagImage, 'location <%s>' % locationId)

__validators = [Locations]
