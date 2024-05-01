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

def ParticleAttacks(data):
	Log("ParticleAttacks mutator ...")

__mutators = [ParticleAttacks]
