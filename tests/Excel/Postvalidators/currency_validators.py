from xl2thrift.validate import __Check
from xl2thrift.validate import __Warn
from xl2thrift.validate import Log

def Currencies(data):
	Log("Currencies postvalidator ...")
	for currencyId in data.currencies:
		currency = data.currencies[currencyId]
		#if currency.startBalance != None:
		#print('Currency %s has startBalance %s, type %s' % (currencyId, currency.startBalance, type(currency.startBalance)))

__validators = [Currencies]
