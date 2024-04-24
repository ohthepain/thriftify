# don't forget to add your mutator script to __init__.py

from __main__ import Log

def GuaranteedHeroes(data):
	Log("GuaranteedHeroes mutator ...")
	for guaranteedHero in data.guaranteedHeroes:
		chestId = guaranteedHero.chestId
		heroId = guaranteedHero.heroId
		chest = data.chests[chestId]
		if chest.guaranteedHeroes == None:
			chest.guaranteedHeroes = []
		chest.guaranteedHeroes.append(heroId)
	data.guaranteedHeroes = None

def GuaranteedCurrencies(data):
	Log("GuaranteedCurrencies mutator ...")
	for guaranteedCurrency in data.guaranteedCurrencies:
		chestId = guaranteedCurrency.chestId
		chest = data.chests[chestId]
		if chest.guaranteedCurrencies == None:
			chest.guaranteedCurrencies = []
		chest.guaranteedCurrencies.append(guaranteedCurrency)
	data.guaranteedCurrencies = None

__mutators = [GuaranteedHeroes, GuaranteedCurrencies]
