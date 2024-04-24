from __main__ import __Check
from __main__ import __Warn
from __main__ import Log

def ChatMessageTemplates(data):
	for chatMessageTemplateId in data.chatMessageTemplates:
		chatMessageTemplate = data.chatMessageTemplates[chatMessageTemplateId]
		chatMessageTemplate.validate()
		__Check.PrefabAssetExists(chatMessageTemplate.itemPrefab, 'chatMessageTemplate <%s>' % (chatMessageTemplateId))
		__Check.PrefabAssetExists(chatMessageTemplate.topperPrefab, 'chatMessageTemplate <%s>' % (chatMessageTemplateId))
		__Check.PrefabAssetExists(chatMessageTemplate.bottomPrefab, 'chatMessageTemplate <%s>' % (chatMessageTemplateId))
		__Check.PrefabAssetExists(chatMessageTemplate.bottomPrefabLeader, 'chatMessageTemplate <%s>' % (chatMessageTemplateId))

def ChatMessages(data):
	for chatMessageId in data.chatMessages:
		chatMessage = data.chatMessages[chatMessageId]
		chatMessage.validate()
		__Check.ImageAssetExists(chatMessage.itemImage, 'chatMessage <%s>' % (chatMessageId))
		__Check.ImageAssetExists(chatMessage.topperImage, 'chatMessage <%s>' % (chatMessageId))
		__Check.ImageAssetExists(chatMessage.bottomImage, 'chatMessage <%s>' % (chatMessageId))

# ChatMessageTemplates is disabled for now because of the xxx strings
__validators = [ChatMessages]

