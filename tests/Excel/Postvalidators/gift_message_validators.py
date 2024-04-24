from __main__ import __Check
from __main__ import __Warn
from __main__ import Log

def GiftMessages(data):
	Log("GiftMessages postvalidator ...")
	for giftMessageId in data.giftMessages:
		giftMessage = data.giftMessages[giftMessageId]
		__Check.IsValidString(giftMessage.title, "gift message %s has no title" % (giftMessageId))
		__Check.IsValidString(giftMessage.subtitle, "gift message %s has no subTitle" % (giftMessageId))
		__Check.IsValidString(giftMessage.body, "gift message %s has no body" % (giftMessageId))
		__Check.IsValidString(giftMessage.giftMessageTemplateId, "gift message %s has no giftMessageTemplateId" % (giftMessageId))
		__Check.Contains(data.giftMessageTemplates, giftMessage.giftMessageTemplateId, "Gift Message %s has no template" % (giftMessageId))
		__Check.Exists(giftMessage.currencyItems , "gift message %s reward list is empty" % (giftMessageId))
		__Check.NotEmpty(giftMessage.currencyItems , "gift message %s reward list is empty" % (giftMessageId))
		if giftMessage.currencyItems:
			for currencyItem in giftMessage.currencyItems:
				__Check.Contains(data.currencies, currencyItem.currencyId   , 'giftMessage %s currencyItem %s does not exist' % (giftMessageId, currencyItem.currencyId))
		if hasattr(data, 'inboxSections'):
			__Check.Contains(data.inboxSections, giftMessage.inboxSectionId, "Gift Message %s has indefined inbox section id <%s>" % (giftMessageId, giftMessage.inboxSectionId))

__validators = [GiftMessages]
