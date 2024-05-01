#
# MUTATORS
#
# Where the only rule is ...
#
# Mutators cannot consume any mutated data!!! This is because their execution order is undefined.
#
# don't forget to add your mutator script to __init__.py
#

from xl2thrift.mutate import Log

def Simulations(data):
	Log("Simulations mutator ...")
	if hasattr(data, 'simulationTestEntries'):
		for simulationTestEntry in data.simulationTestEntries:
			simulationTestId = simulationTestEntry.simulationTestId
# 			print('testId %s order %d' % (simulationTestId, simulationTestEntry.order))
			simulationTest = data.simulationTests[simulationTestId]
			if simulationTest.simulationTestEntries == None:
				simulationTest.simulationTestEntries = []
			while len(simulationTest.simulationTestEntries) <= simulationTestEntry.order:
# 				print(' appent to entries length %d order %d' % (len(simulationTest.simulationTestEntries), simulationTestEntry.order))
				simulationTest.simulationTestEntries.append(simulationTestEntry)
# 			print('set entry at order %d entry order %d' % (simulationTestEntry.order, simulationTestEntry.order))
			simulationTest.simulationTestEntries[simulationTestEntry.order] = simulationTestEntry

		# remove data.simulationTestEntries
		data.simulationTestEntries = None

__mutators = [Simulations]