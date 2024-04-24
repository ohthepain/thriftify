from __main__ import __Check
from __main__ import __Warn
from __main__ import Log
# from __main__ import ConfigModule

def SoundClips(data):
	Log("SoundClips prevalidator ...")
	if hasattr(data, 'soundClips'):
		for soundClipId in data.soundClips:
			soundClip = data.soundClips[soundClipId]
			__Check.AudioAssetExists(soundClip.path, 'SoundClip <%s>' % soundClipId)

__validators = [SoundClips]
