from xl2thrift.validate import __Check
from xl2thrift.validate import __Warn
from xl2thrift.validate import Log

def TutorialSteps(data):
	Log("TutorialSteps prevalidator ...")
	for tutorialStepId in data.tutorialSteps:
		tutorialStep = data.tutorialSteps[tutorialStepId]
		tutorialStep.validate()
		tutorialId = tutorialStep.tutorialId
		__Check.IsTrue(tutorialId in data.tutorials, "Tutorial step '%s' has an undefined tutorial '%s'" % (tutorialStepId, tutorialId))
		if tutorialStep.imagePath != None:
			__Check.ImageAssetExists(tutorialStep.imagePath, 'tutorialStep <%s>' % tutorialStepId)
		if tutorialStep.panelPrefabPath != None:
			__Check.PrefabAssetExists(tutorialStep.panelPrefabPath, 'tutorialStep <%s>' % tutorialStepId)

__validators = [TutorialSteps]
