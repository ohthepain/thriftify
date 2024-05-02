from xl2thrift.validate import __Check
from xl2thrift.validate import __Warn
from xl2thrift.validate import Log

def SoundClips(data):
	Log("SoundClips prevalidator ...")
	if hasattr(data, 'soundClips'):
		for soundClipId in data.soundClips:
			soundClip = data.soundClips[soundClipId]
			__Check.AudioAssetExists(soundClip.path, 'SoundClip <%s>' % soundClipId)

__validators = [SoundClips]
