# don't forget to add your mutator script to __init__.py

import sys as __sys
from xl2thrift.mutate import Log

def __dumpTutorials(data):
	for tutorialId in data.tutorials:
		tutorial = data.tutorials[tutorialId]
		print("check2 %s" % (tutorial.tutorialId))
		for step in tutorial.tutorialSteps:
			Log("\tstep %s" % (step.tutorialStepId))
			if step.openCheckpoints:
				for checkpointId in step.openCheckpoints:
					Log("\t\topen on %s" % (checkpointId))
			else:
				Log("\t\tno open checkpoints")
			if step.passCheckpoints:
				for checkpointId in step.passCheckpoints:
					Log("\t\tpass on %s" % (checkpointId))
			else:
				Log("\t\tno pass checkpoints")

def TutorialSteps(data):
	for tutorialStepId in data.tutorialSteps:
		tutorialStep = data.tutorialSteps[tutorialStepId]
		tutorialId = tutorialStep.tutorialId
		tutorial = data.tutorials[tutorialId]
		if tutorial.tutorialSteps == None:
			tutorial.tutorialSteps = []
		while len(tutorial.tutorialSteps) <= tutorialStep.order:
			tutorial.tutorialSteps.append(-1)
		if tutorial.tutorialSteps[tutorialStep.order] != -1:
			__sys.exit("Error: Tutorial %s step `%s` - order slot %d is already taken" % (tutorialId, tutorialStepId, tutorialStep.order))
		tutorial.tutorialSteps[tutorialStep.order] = tutorialStep

	# Removed, as go button tutorials have no completion flag
	# for tutorialId in data.tutorials:
	# 	tutorial = data.tutorials[tutorialId]
	# 	if tutorial.completionFlag == None:
	# 		__sys.exit("Error: Tutorial \"%s\" - has no completion flag" % (tutorialId))

	# Remove empty steps from order
	for tutorialId in data.tutorials:
		#Log("check %s" % (tutorialId))
		tutorial = data.tutorials[tutorialId]
		tutorialSteps = tutorial.tutorialSteps
		tutorial.tutorialSteps = [x for x in tutorialSteps if x != -1]

	data.tutorialSteps = None

	#dumpTutorials(data)

__mutators = [TutorialSteps]
