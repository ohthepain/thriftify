# don't forget to add your mutator script to __init__.py

from xl2thrift.mutate import Log

def GiftMessageRewards(data):
	#print("GiftMessageRewards mutator ...")
	for giftMessageCurrencyItem in data.giftMessageCurrencyItems:
		#print(giftMessageCurrencyItem.giftMessageId)
		giftMessage = data.giftMessages[giftMessageCurrencyItem.giftMessageId]
		if giftMessage.currencyItems == None:
			giftMessage.currencyItems = []
		giftMessage.currencyItems.append(giftMessageCurrencyItem)

	# erase table
	data.giftMessageCurrencyItems = None

__mutators = [GiftMessageRewards]
