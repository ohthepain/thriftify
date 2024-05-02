
from xl2thrift.validate import __Check
from xl2thrift.validate import __Warn
from xl2thrift.validate import Log

def SectionHeadingTemplates(data):
	if hasattr(data, 'sectionHeadingTemplates'):
		for sectionHeadingTemplateId in data.sectionHeadingTemplates:
			sectionHeadingTemplate = data.sectionHeadingTemplates[sectionHeadingTemplateId]
			sectionHeadingTemplate.validate()
			__Check.PrefabAssetExists(sectionHeadingTemplate.prefab, 'sectionHeadingTemplate <%s>' % sectionHeadingTemplateId)
			__Check.ImageAssetExists(sectionHeadingTemplate.backgroundImage, 'sectionHeadingTemplate <%s>' % sectionHeadingTemplateId)

def SectionHeadings(data):
	if hasattr(data, 'sectionHeadings'):
		for sectionHeadingId in data.sectionHeadings:
			sectionHeading = data.sectionHeadings[sectionHeadingId]
			sectionHeading.validate()
			__Check.IsValidString(sectionHeading.sectionHeadingTemplateId, 'SectionHeading %s has no sectionHeadingTemplateId' % (sectionHeadingId))

def SectionTopperTemplates(data):
	if hasattr(data, 'sectionTopperTemplates'):
		for sectionTopperTemplateId in data.sectionTopperTemplates:
			sectionTopperTemplate = data.sectionTopperTemplates[sectionTopperTemplateId]
			sectionTopperTemplate.validate()
			__Check.PrefabAssetExists(sectionTopperTemplate.prefab, 'sectionTopperTemplate <%s>' % sectionTopperTemplateId)
			__Check.ImageAssetExists(sectionTopperTemplate.backgroundImage, 'sectionTopperTemplate <%s>' % sectionTopperTemplateId)

def SectionToppers(data):
	if hasattr(data, 'sectionToppers'):
		for sectionTopperId in data.sectionToppers:
			sectionTopper = data.sectionToppers[sectionTopperId]
			sectionTopper.validate()
			__Check.IsValidString(sectionTopper.sectionTopperTemplateId, 'SectionTopper %s has no sectionTopperTemplateId' % (sectionTopperId))

def SectionBottomTemplates(data):
	if hasattr(data, 'sectionBottomTemplates'):
		for sectionBottomTemplateId in data.sectionBottomTemplates:
			sectionBottomTemplate = data.sectionBottomTemplates[sectionBottomTemplateId]
			sectionBottomTemplate.validate()
			__Check.PrefabAssetExists(sectionBottomTemplate.prefab, 'sectionBottomTemplate <%s>' % sectionBottomTemplateId)
			__Check.ImageAssetExists(sectionBottomTemplate.backgroundImage, 'sectionBottomTemplate <%s>' % sectionBottomTemplateId)

def SectionBottoms(data):
	if hasattr(data, 'sectionBottoms'):
		for sectionBottomId in data.sectionBottoms:
			sectionBottom = data.sectionBottoms[sectionBottomId]
			sectionBottom.validate()
			__Check.IsValidString(sectionBottom.sectionBottomTemplateId, 'SectionBottom %s has no sectionBottomTemplateId' % (sectionBottomId))

def InboxSections(data):
	if hasattr(data, 'inboxSections'):
		for inboxSectionId in data.inboxSections:
			inboxSection = data.inboxSections[inboxSectionId]
			inboxSection.validate()
			__Check.IsValidString(inboxSection.sectionHeadingId, 'InboxSection %s has no sectionHeadingId' % (inboxSectionId))
			__Check.IsValidString(inboxSection.sectionTopperId, 'InboxSection %s has no sectionTopperId' % (inboxSectionId))
			__Check.IsValidString(inboxSection.sectionBottomId, 'InboxSection %s has no sectionBottomId' % (inboxSectionId))

def GuildSectionItemTemplates(data):
	if hasattr(data, 'guildSectionItemTemplates'):
		for guildSectionItemTemplateId in data.guildSectionItemTemplates:
			guildSectionItemTemplate = data.guildSectionItemTemplates[guildSectionItemTemplateId]
			guildSectionItemTemplate.validate()
			__Check.PrefabAssetExists(guildSectionItemTemplate.prefab, 'guildSectionItemTemplate <%s>' % (guildSectionItemTemplateId))
			if guildSectionItemTemplate.backgroundImage != None:
				__Check.ImageAssetExists(guildSectionItemTemplate.backgroundImage, 'guildSectionItemTemplate <%s>' % (guildSectionItemTemplateId))

def GuildMemberListItemTemplates(data):
	if hasattr(data, 'guildMemberListItemTemplates'):
		if data.guildMemberListItemTemplates != None:
			for guildMemberListItemTemplateId in data.guildMemberListItemTemplates:
				guildMemberListItemTemplate = data.guildMemberListItemTemplates[guildMemberListItemTemplateId]
				guildMemberListItemTemplate.validate()
				__Check.PrefabAssetExists(guildMemberListItemTemplate.prefab, 'guildMemberListItemTemplate <%s>' % (guildMemberListItemTemplateId))
				__Check.ImageAssetExists(guildMemberListItemTemplate.backgroundImage, 'guildMemberListItemTemplate <%s>' % (guildMemberListItemTemplateId))
			else:
				print("WARNING: No data.guildMemberListItemTemplates are defined")

def GuildListItemTemplates(data):
	if hasattr(data, 'guildListItemTemplates'):
		for guildListItemTemplateId in data.guildListItemTemplates:
			guildListItemTemplate = data.guildListItemTemplates[guildListItemTemplateId]
			guildListItemTemplate.validate()
			__Check.PrefabAssetExists(guildListItemTemplate.prefab, 'guildListItemTemplate <%s>' % (guildListItemTemplateId))

def GuildMemberListSections(data):
	if hasattr(data, 'guildMemberListSections'):
		for guildMemberListSectionId in data.guildMemberListSections:
			guildMemberListSection = data.guildMemberListSections[guildMemberListSectionId]
			guildMemberListSection.validate()
			__Check.IsValidString(guildMemberListSection.sectionHeadingId, 'GuildMemberListSection %s has no sectionHeadingId' % (guildMemberListSectionId))
			__Check.IsValidString(guildMemberListSection.sectionTopperId, 'GuildMemberListSection %s has no sectionTopperId' % (guildMemberListSectionId))
			__Check.IsValidString(guildMemberListSection.sectionBottomId, 'GuildMemberListSection %s has no sectionBottomId' % (guildMemberListSectionId))

__validators = [SectionHeadingTemplates,
				SectionHeadings,
				SectionTopperTemplates,
				SectionToppers,
				SectionBottomTemplates,
				SectionBottoms,
				InboxSections,
				GuildSectionItemTemplates,
				GuildMemberListItemTemplates,
				GuildListItemTemplates,
				GuildMemberListSections]
