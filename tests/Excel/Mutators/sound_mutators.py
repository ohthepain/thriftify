# don't forget to add your mutator script to __init__.py

from xl2thrift.mutate import Log

def SoundClipLists(data):
	print("SoundClipLists mutator ...")
	if hasattr(data, 'soundClips'):
		for soundClipId in data.soundClips:
			soundClip = data.soundClips[soundClipId]
			if soundClip.soundClipListId != None:
				if soundClip.soundClipListId not in data.soundClipLists:
					raise ValueError('Undefined soundClipListId <%s>' % soundClip.soundClipListId)
				if data.soundClipLists[soundClip.soundClipListId].soundClipIds == None:
					data.soundClipLists[soundClip.soundClipListId].soundClipIds = []
				data.soundClipLists[soundClip.soundClipListId].soundClipIds.append(soundClipId)
	print("SoundClipLists mutator ... dunn")

__mutators = [SoundClipLists]
