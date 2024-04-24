# don't forget to add your mutator script to __init__.py

import sys
import importlib

from __main__ import ConfigModule
from __main__ import Log

def Skills(data):
	Log("Skills mutator ...")
	for heroId in data.heroBodies:
		heroBody = data.heroBodies[heroId]

		if hasattr(data, 'skills'):
			# Trainers don't have skills
			if heroBody.skillId0 != None:
				heroBody.skillIds = []
				heroBody.skillIds.append(heroBody.skillId0)
				if heroBody.skillId1 != None:
					heroBody.skillIds.append(heroBody.skillId1)
				if heroBody.skillId2 != None:
					heroBody.skillIds.append(heroBody.skillId2)
				if heroBody.skillId3 != None:
					heroBody.skillIds.append(heroBody.skillId3)

				if data.skills[heroBody.skillId0].skillTypeId == ConfigModule.SkillTypeID.EnergyShot:
					heroBody.energyShotSkillSlotNum = 0
				elif data.skills[heroBody.skillId0].skillTypeId == ConfigModule.SkillTypeID.BumpCombo:
					heroBody.bumpComboSkillSlotNum = 0
				elif data.skills[heroBody.skillId0].skillTypeId == ConfigModule.SkillTypeID.Enchantment:
					heroBody.enchantmentSkillSlotNum = 0

				if heroBody.skillId1 in data.skills:
					if data.skills[heroBody.skillId1].skillTypeId == ConfigModule.SkillTypeID.EnergyShot:
						heroBody.energyShotSkillSlotNum = 1
					elif data.skills[heroBody.skillId1].skillTypeId == ConfigModule.SkillTypeID.BumpCombo:
						heroBody.bumpComboSkillSlotNum = 1
					elif data.skills[heroBody.skillId1].skillTypeId == ConfigModule.SkillTypeID.Enchantment:
						heroBody.enchantmentSkillSlotNum = 1

				if heroBody.skillId2 in data.skills:
					if data.skills[heroBody.skillId2].skillTypeId == ConfigModule.SkillTypeID.EnergyShot:
						heroBody.energyShotSkillSlotNum = 2
					elif data.skills[heroBody.skillId2].skillTypeId == ConfigModule.SkillTypeID.BumpCombo:
						heroBody.bumpComboSkillSlotNum = 2
					elif data.skills[heroBody.skillId2].skillTypeId == ConfigModule.SkillTypeID.Enchantment:
						heroBody.enchantmentSkillSlotNum = 2

				if heroBody.skillId3 in data.skills:
					if data.skills[heroBody.skillId3].skillTypeId == ConfigModule.SkillTypeID.EnergyShot:
						heroBody.energyShotSkillSlotNum = 3
					elif data.skills[heroBody.skillId3].skillTypeId == ConfigModule.SkillTypeID.BumpCombo:
						heroBody.bumpComboSkillSlotNum = 3
					elif data.skills[heroBody.skillId3].skillTypeId == ConfigModule.SkillTypeID.Enchantment:
						heroBody.enchantmentSkillSlotNum = 3

		heroBody.skillId0 = None
		heroBody.skillId1 = None
		heroBody.skillId2 = None
		heroBody.skillId3 = None

__mutators = [Skills]
