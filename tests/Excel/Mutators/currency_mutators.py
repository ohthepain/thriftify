# don't forget to add your mutator script to __init__.py

from xl2thrift.mutate import Log

def CurrencyMaxByRank(data):
	for currencyRankMaxEntry in data.currencyRankMaxEntries:
		currency = data.currencies[currencyRankMaxEntry.currencyId]
		if currency.maxByRank == None:
			currency.maxByRank = []
		while len(currency.maxByRank) <= currencyRankMaxEntry.rankId:
 			# grow list
			currency.maxByRank.append(currencyRankMaxEntry.max)
		currency.maxByRank[currencyRankMaxEntry.rankId] = currencyRankMaxEntry.max

	data.currencyRankMaxEntries	= None

__mutators = [CurrencyMaxByRank]
