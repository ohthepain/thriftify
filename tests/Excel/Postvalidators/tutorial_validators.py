from __main__ import __Check
from __main__ import __Warn
from __main__ import Log


def TutorialSteps(data):
	Log("TutorialSteps postvalidator ...")
	for tutorialId in data.tutorials:
		tutorial = data.tutorials[tutorialId]
		__Check.IsTrue(data.tutorials[tutorialId] != None, "Tutorial %s undefined" % (tutorialId))
		__Check.Exists(data.tutorials[tutorialId].tutorialSteps, "Tutorial %s has no steps" % (tutorialId))
		__Check.IsTrue(data.tutorials[tutorialId].tutorialSteps, "Tutorial %s step list is empty" % (tutorialId))
		if data.tutorials[tutorialId].tutorialSteps:
			tutorialStep = data.tutorials[tutorialId].tutorialSteps[0]
			__Warn.IsTrue(tutorialStep.preDelaySeconds == None, "Tutorial step '%s' cannot have predelay on first step" % (tutorialStep.tutorialStepId))
			for tutorialStep in data.tutorials[tutorialId].tutorialSteps:
				__Warn.Exists(tutorialStep.passCheckpoints, "Tutorial step '%s' has no passCheckpoints" % (tutorialStep.tutorialStepId))
				if tutorialStep.passCheckpoints:
					__Warn.IsTrue(len(data.tutorials[tutorialId].tutorialSteps) > 0, "Tutorial %s step list is empty" % (tutorialId))

			# Can't check for duplicate order. Duh. 			
			# order = {}
			# for tutorialStep in data.tutorials[tutorialId].tutorialSteps:
			# 	__Check.IsTrue(tutorialStep.order not in order, "tutorialStep %s - duplicate order position %d" % (tutorialStep.tutorialStepId, tutorialStep.order))
			# 	order[tutorialStep.order] = 1

__validators = [TutorialSteps]
