# don't forget to add your mutator script to __init__.py

import sys
import importlib

from __main__ import ConfigModule
from xl2thrift.mutate import Log

def EffectLists(data):
	Log("EffectLists mutator ...")
	for effectListId in data.effectLists:
		effectList = data.effectLists[effectListId]
		if effectList.effectListEntries == None:
			effectList.effectListEntries = []

	for effectListEntry in data.effectListEntries:
		if not effectListEntry.disable:
			effectListId = effectListEntry.effectListId
			effectList = data.effectLists[effectListId]
			effectList.effectListEntries.append(effectListEntry)

		# Silly optimization
		effectListEntry.effectListId = None

	data.effectListEntries = None

__mutators = [EffectLists]
