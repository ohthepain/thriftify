from __main__ import __Check
from __main__ import __Warn
from __main__ import Log

def Currencies(data):
	Log("Currencies prevalidator ...")
	for currencyId in data.currencies:
		currency = data.currencies[currencyId]
		currency.validate()
		#if currency.startBalance != None:
		#print('Currency %s has startBalance %s, type %s' % (currencyId, currency.startBalance, type(currency.startBalance)))
		if currency.iconImagePath != None:
			__Check.ImageAssetExists(currency.iconImagePath, 'currency <%s>' % currencyId)
		if currency.cardImagePath != None:
			__Check.ImageAssetExists(currency.cardImagePath, 'currency <%s>' % currencyId)
		if currency.inboxIconImagePath != None:
			__Check.ImageAssetExists(currency.inboxIconImagePath, 'currency <%s>' % currencyId)
		if currency.cardImagePathDisabled != None:
			__Check.ImageAssetExists(currency.cardImagePathDisabled, 'currency <%s>' % currencyId)

__validators = [Currencies]

