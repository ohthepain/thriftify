# don't forget to add your mutator script to __init__.py

from __main__ import Log

def SoundClipLists(data):
	#print("SoundClipLists mutator ...")
	if hasattr(data, 'soundClips'):
		for soundClipId in data.soundClips:
			soundClip = data.soundClips[soundClipId]
			if soundClip.soundClipListId != None:
				if soundClip.soundClipListId not in data.soundClipLists:
					raise ValueError('Undefined soundClipListId <%s>' % soundClip.soundClipListId)
				if data.soundClipLists[soundClip.soundClipListId].soundClipIds == None:
					data.soundClipLists[soundClip.soundClipListId].soundClipIds = []
				data.soundClipLists[soundClip.soundClipListId].soundClipIds.append(soundClipId)

__mutators = [SoundClipLists]
