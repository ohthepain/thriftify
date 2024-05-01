# don't forget to add your mutator script to __init__.py
import sys
import importlib

from xl2thrift.mutate import ConfigModule
from xl2thrift.mutate import Log

def RequestInfo(data):
	Log("RequestInfo mutator ...")

	if data.requestInfo == None:
		data.requestInfo = {}

	for fieldEntry in data.safeFieldEntries:
		if not fieldEntry.requestUrl in data.requestInfo:
			requestInfo = ConfigModule.RequestInfo()
			requestInfo.requestUrl = fieldEntry.requestUrl
			data.requestInfo[fieldEntry.requestUrl] = requestInfo
		requestInfo = data.requestInfo[fieldEntry.requestUrl]
		if requestInfo.safeUserFieldIds == None:
			requestInfo.safeUserFieldIds = []
		data.requestInfo[fieldEntry.requestUrl].safeUserFieldIds.append(fieldEntry.userFieldId)

	for fieldEntry in data.dangerFieldEntries:
		if not fieldEntry.requestUrl in data.requestInfo:
			requestInfo = ConfigModule.RequestInfo()
			requestInfo.requestUrl = fieldEntry.requestUrl
			data.requestInfo[fieldEntry.requestUrl] = requestInfo
		requestInfo = data.requestInfo[fieldEntry.requestUrl]
		if requestInfo.dangerUserFieldIds == None:
			requestInfo.dangerUserFieldIds = []
		data.requestInfo[fieldEntry.requestUrl].dangerUserFieldIds.append(fieldEntry.userFieldId)

	# Remove these tables from the config
	data.safeFieldEntries = None
	data.dangerFieldEntries = None

__mutators = [RequestInfo]
