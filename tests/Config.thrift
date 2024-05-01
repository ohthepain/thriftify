namespace py BadEnergy.Config
namespace java BadEnergy.Config
namespace js BadEnergy.Config

typedef string GameID
typedef string UserID
typedef string DeviceID
typedef string InstallID
typedef string AssetID
typedef string AssetListID

typedef string CurrencyID
typedef string CampaignID
typedef string LevelID
typedef string LevelSceneID
typedef string HeroID
typedef string SoundClipID
typedef string SoundClipListID
typedef string TutorialID
typedef string TutorialStepID
typedef string TutorialCheckpointID
typedef string ChestID
typedef string TutorialFlagID
typedef string RuntimePlatformID
typedef i32 ServerErrorID
typedef i32 ServerReasonID
typedef i32 RankID
typedef string BundleID
typedef string LocationID
typedef string InboxMessageID
typedef string HeroSummonID

// I think this belongs in User
typedef string GuildID
typedef i32 GuildRankID
typedef string GuildEmblemID
typedef string GuildFrameID
typedef i32 GuildLevelID

const string CurrencyId_Recruits = "Recruit"
const string CurrencyId_Gold = "Gold"
const string CurrencyId_Gems = "Gems"

typedef string SettingKey
typedef string SettingValue
typedef string SettingType

struct DateTimeUTC
{
	1: required i64 epochMilliseconds
}

struct SettingKeyValue
{
	1: optional SettingKey settingKey
	2: optional SettingValue settingValue
	3: optional SettingType settingType 
}

enum CurrencyTargetID
{
	Inventory = 0,
	HUD,
	User,
	Guild,
}

enum SpecialMoveTrigger
{
	Nothing = 0,
	AfterKill,
}

enum ArrowDirection
{
	Up,
	Right,
	Left,
	Down,
}

enum RarityID
{
	Common,
	Uncommon,
	Rare,
	Epic,
	Legendary,
}

// Only type 'Hero' are awarded from chests
// Enemies are not shown in shopText_UnlockSkillSlot
enum BodyTypeID
{
	Hero,
	Enemy,
	Wall,
	Trainer,
	Boss,
}

enum ActionID
{
	Nothing,
	GoToShop,
	GoToHeroCollection,
	GoToBattlePrep,
	GoToSocial,
	GoToRaidPrep,
	CloseTopModal,
	CloseAllModals,
	GoToHomeMenu,
}

enum HeroBodyTypeID
{
	Bump,
	Pierce,
}

enum AffinityID
{
	Nothing = 0,
	Red,
	Blue,
	Green,
	Yellow,
	Black,
}

enum ProgressionID
{
	MainCampaign,
	TrainingCamps,
}

enum ColorID
{
	Red,
	Green,
	Blue,
	Yellow,
	Purple,
	Black,
}

enum CrownChestState
{
	Nothing = 0,
	Animated,
	Unlocking,
	Collecting,
	Ready,
}

enum DailyAchievementsChestState
{
	Nothing = 0,
	Progress,
	Ready,
	Collected
}

enum ChestSlotState
{
	Nothing = 0,
	Unlocking,
	Ready,
	Animated,
}

enum TimedChestState
{
	Nothing = 0,
	Unlocking,
	Ready,
}

enum ExternalAccountTypeID
{
	GameCenter,
	GooglePlay,
}

struct CurrencyTarget
{
	1: required CurrencyTargetID currencyTargetId
	2: optional AssetID iconPath
}

typedef string ExternalAccountUserID

struct UserBasicInfo
{
	1: required UserID userId
	2: required RankID rank
	3: required DateTimeUTC lastActivity
	4: required string mostRecentDeviceName
	5: optional string nickname
	6: optional i32 vipLevel

	10: optional GuildEmblemID guildEmblemId
    11: optional GuildFrameID guildFrameId
    12: optional string guildName
	13: optional UserFrameID userFrameId
	14: optional UserIconID userIconId
}

typedef string LocalizedString

struct GuildLevel
{
	1: required GuildLevelID guildLevelId
	2: required LocalizedString display
}

enum GuildJoinTypeID
{
    Open=0,
    Request,
    Invite,
    Dead
}

struct GuildJoinType
{
	1: optional GuildJoinTypeID guildJoinTypeId
	10: optional LocalizedString display
	11: optional LocalizedString joinButtonText
}

enum GuildMemberTypeID
{
	Leader,
	Coleader,
	Boss,
	Manager,
	Member
}

struct GuildMemberType
{
	1: required GuildMemberTypeID guildMemberTypeId
	10: required LocalizedString display
	11: optional i32 maxMembers
	12: optional GuildMemberListSectionID guildMemberListSectionId
}

enum ServerErrorMessageID
{
	AlreadyApplied = 100,
	MemberAcceptInvite,
}

typedef string ServerErrorDialogTemplateID

struct ServerErrorDialogTemplate
{
	1: required ServerErrorDialogTemplateID serverErrorDialogTemplateId
	2: required AssetID prefab
}

typedef string GenericDialogTemplateID

struct GenericDialogTemplate
{
	1: required GenericDialogTemplateID genericDialogTemplateId
	2: required AssetID prefab
}

typedef string GenericDialogID

struct GenericDialog
{
	1: required GenericDialogID genericDialogId
	2: required GenericDialogTemplateID genericDialogTemplateId
	3: optional LocalizedString title
	4: optional LocalizedString body
	5: optional LocalizedString okayButtonText
	6: optional AssetID okayButtonImage
	7: optional AssetID backgroundImage
	8: optional AssetID featureImage
	9: optional LocalizedString secondButtonText
	10: optional AssetID secondButtonImage
	11: optional AssetID secondFeatureImage
	12: optional string firstButtonTutorialId
	13: optional string secondButtonTutorialId
	14: optional string openSoundId
}

struct ServerErrorMessage
{
	1: required ServerErrorMessageID serverErrorMessageId
	2: required ServerErrorDialogTemplateID serverErrorDialogTemplateId
	10: optional LocalizedString title
	11: optional LocalizedString body
	20: optional LocalizedString button1Text
	21: optional LocalizedString button2Text
}

// Deprecated
enum HudTypeID
{
	Default = 0,
	NoHud,
	Custom,
}

struct HudProfile
{
	1: required string hudProfileId
	// Deprecated - was required - need forced update
	2: optional HudTypeID hudTypeId
	// Deprecated - was required - need forced update
	3: optional bool showUser
	4: optional list<string> currencyIds
	5: optional bool showInventory
}

enum LeagueID
{
	Set
	Family
	Enterprise
	Syndicate
	Cartel
}

struct League
{
    1: required LeagueID leagueId
    2: required i64 guildPoints
    10: required LocalizedString display
    11: required LocalizedString displaySingular
}

struct GuildEmblem
{
    1: required GuildEmblemID guildEmblemId
    2: optional i32 displayOrder
    10: required AssetID image
    12: optional LeagueID minLeagueId
	13: optional bool hidden

}

struct GuildFrame
{
    1: required GuildFrameID guildFrameId
    2: optional i32 displayOrder
    10: required AssetID image
    11: optional i32 minGuild
    12: optional LeagueID minLeagueId
	13: optional bool hidden
}

typedef string UserIconID
struct UserIcon
{
    1: required UserIconID userIconId
    2: optional i32 displayOrder
    3: optional bool hidden
    10: required AssetID image
}

typedef string UserFrameID
struct UserFrame
{
    1: required UserFrameID userFrameId
    2: optional i32 displayOrder
    3: optional bool hidden
    4: optional AssetID rankBackgroundImage
    10: required AssetID image
}

// Global settings for all guilds
struct GuildSettings
{
    1: optional i32 maxMemberCount // Default max count
    2: optional i32 unlockRank
    3: optional i32 createRank

    10: optional i32 maxDisplayLength
    11: optional i32 maxDisplayTagLength
    12: optional i32 maxDescriptionLength
    13: optional i32 minDisplayLength
    14: optional i32 minDisplayTagLength
    15: optional i32 minDescriptionLength

    20: optional LocationID defaultLocationId
    21: optional GuildEmblemID defaultGuildEmblemId

    32: optional GuildEmblemID defaultEmblemId
    33: optional GuildFrameID defaultFrameId
    30: optional GuildEmblemID noGuildEmblemId
    31: optional GuildFrameID noGuildFrameId

    40: optional LocalizedString joinInvitationDefault
    41: optional LocalizedString joinApplicationDefault
    42: optional LocalizedString applicantAcceptedMessageTitle
    43: optional LocalizedString applicantRejectedMessageTitle
    44: optional LocalizedString cannotSendGuildInvitesText
    45: optional LocalizedString cannotJoinFullGuildText
    46: optional LocalizedString guildDisplayAndTagTakenText
    47: optional LocalizedString guildNameTakenText
    48: optional LocalizedString guildTagTakenText
    49: optional LocalizedString guildDeletedText
    50: optional LocalizedString guildErrorText

	51: optional GuildListSectionID guildSuggestSectionId
	52: optional GuildListSectionID guildSearchSectionId

	53: optional GuildMemberListSectionID guildMemberSectionId
	54: optional GuildMemberListSectionID guildLeaderSectionId
	55: optional GuildMemberListSectionID guildCoLeaderSectionId
	56: optional GuildMemberListSectionID guildBossSectionId
	57: optional GuildMemberListSectionID guildManagerSectionId

	58: optional GuildMemberListSectionID guildEmblemSectionId
	59: optional GuildMemberListSectionID guildRuleSectionId
    60: optional LocalizedString guildKickMessageText
}

const i32 NumDecks = 4
const i32 DeckNumSlots = 4
const i32 NumChestSlots = 4

struct Settings
{
	1: required string gameId
	2: required string thriftNamespace
	// this value is for debug output so that you can test your config edits end to end without breaking anything else
	3: optional i32 unusedNumber
	// set this number locally so that you can test whether local configs are working
	4: optional i32 testLocalConfig
	5: optional double chestGemsCostPerHour
    6: optional list<ChestID> dailyAchievementChestIds
    7: optional AssetID badEnergyMeterFullParticleEffectPath
    8: optional list<i32> testListI32
    9: optional list<double> testListDouble
    10: optional list<LeagueID> testListEnum

	11: optional i32 screenDarkerOpacity
	12: optional i32 sectionShadowOpacity
	13: optional i32 sectionShadowDistanceX
	14: optional i32 sectionShadowDistanceY
	15: optional i32 popupShadowOpacity
	16: optional i32 popupShadowDistanceX
	17: optional i32 popupShadowDistanceY
	18: optional string requiredAppVersion
	19: optional string recommendedAppVersion

	20: optional double victoryMenuGearItemDelaySeconds
	21: optional double victoryMenuChestDelaySeconds
	22: optional i32 shopCardOfferBaseCostCommon
    23: optional i32 shopCardOfferBaseCostRare
    24: optional i32 shopCardOfferBaseCostEpic
    25: optional double xpTransferAffinitiesMatch
    26: optional double xpTransferAffinitiesNoMatch
	27: optional i32 maxFusionSelectedCard
	28: optional i32 shopCardOfferBaseCostUncommon

	30: optional bool enableMinigameChestRewards
	31: optional string gemPassesTemplate
	32: optional string gemPassesSectionId
	33: optional string emptySectionTemplate
	34: optional AssetID gearBorderImageReadyToEquipPath
	35: optional AssetID gearBorderImageUnlockedPath
	36: optional AssetID gearBorderImageCraftPath
	38: optional AssetID tutorialArrowPrefabPath
	39: optional double selectedSkeletonScaleInOffer

	40: optional AssetID gearBorderImageLockedPath
	41: optional double textFlyoffsVisibilityDuration
	42: optional double textFlyoffsFadeDuration
	43: optional double minigameTimeoutMinutes
	44: optional i32 heroSummonMainMenuButtonUnlockRankId
	45: optional double minigameHealthbarSeconds
	46: optional i32 minigameTimerMinRank
	47: optional string emptySectionTemplateInbox
	48: optional string emptySectionTemplateShop
	49: optional string emptySectionTemplateGuilds

	50: optional string autoWinCurrencyId
	51: optional i32 currentConfigCleanerNum
	52: optional i32 numSkillSlots
	53: optional i32 maxSkillLevel
    54: optional double energyGainHitOpponent
    55: optional double energyGainDamageOpponent
	56: optional double energyGainBumpTeammate
    57: optional double energyGainBumpedByTeammate
    58: optional double energyGainLoseHealth
    59: optional double energyGainKillOpponent
    60: optional double energyGainEnchantOpponent
    61: optional double energyGainEnchantTeammate
    62: optional double cardRevealFlyingDuration
    63: optional double cardRevealDelayDuration
    64: optional i32 unlockedStarterPackIconRank
    65: optional i32 unlockedAchievementButtonRank
    66: optional i32 unlockedRaidButtonRank
    67: optional i32 unlockedDailyQuestsButtonRank

    70: optional AssetID cardBackImageDefault
    71: optional AssetID cardBackImageHidden
    72: optional AssetID cardBackImageCommon
    73: optional AssetID cardBackImageRare
    74: optional AssetID cardBackImageEpic
    75: optional AssetID cardBackImageLegendary
    76: optional bool minigameShowNextTurn
    77: optional bool minigameShowShotFeedback

    80: optional AssetID cellViewWhereToFindBgDisable
    81: optional AssetID cellViewWhereToFindBgEnable
    82: optional AssetID guildProfileInfoLoadingSectionTemplate
    83: optional AssetID guildProfileInfoLeaveSectionTemplate
    84: optional AssetID currencyDefaultCellViewPrefab
    85: optional AssetID autoWinCurrencyCellViewPrefab

    86: optional string forcedUpdateUrlAndroid
    87: optional string forcedUpdateUrlIos

    90: optional AssetID shopRibbonHeadingSectionTemplate
    91: optional AssetID shopHeadingSectionTemplate
    92: optional AssetID shopSingleItemSectionTemplate
    93: optional AssetID shopMultipleItemSectionTemplate
    94: optional AssetID minigameFloatingHealPrefab
	95: optional AssetID minigameFloatingDamagePrefab

    100: optional AssetID eventRibbonHeadingSectionTemplate
    101: optional AssetID eventHeadingSectionTemplate
    102: optional AssetID eventSingleItemSectionTemplate
    103: optional AssetID eventMultipleItemSectionTemplate
    104: optional string emptySectionTemplateEvent
}

struct Text
{
	1: optional string editUserMenuAllowInvites_self
	2: optional string editUserMenuDontAllowInvites_self
	3: optional string editUserMenuAllowInvites_other
	4: optional string editUserMenuDontAllowInvites_other
	5: optional string noCrew
	6: optional string joinCrewNow
	7: optional string crew
	8: optional string damage
	9: optional string heal
	10: optional string chestSlotFull
	11: optional string okay
	12: optional string cancel
	13: optional string evolve
	14: optional string levelUp
	15: optional string level
	23: optional string commonOkay
	24: optional string editGuildSetUpEmblem
	25: optional string editGuildSelectIcon
	26: optional string editGuildSelectBorder
	27: optional string chestNextChestIn
	28: optional string purchaseConfirmation_NextPurchaseBonusInNumPurchases
	30: optional string heroInfoMenuPrefab
	31: optional string settingMenu_FindMyData
	32: optional string settingMenu_Connect
	34: optional string settingMenuPopup
	35: optional string settingMenu_SoundOn
	36: optional string settingMenu_SoundOff

	40: optional string fusion_HeroInASlot

	47: optional string winMenu_XpGained
	48: optional string winMenu_XpProgressLeft
	49: optional string winMenu_XpProgressRight
	50: optional string max
	51: optional string maxLevel
	52: optional string maxXp
	53: optional string xpColon
	54: optional string heroFusion_StatValue
	55: optional string heroFusion_PlusValue
	56: optional string heroFusion_Selected
	57: optional string heroFusion_Cost
	58: optional string commonFind
	59: optional string commonCraft
	60: optional string commonEquip
	61: optional string commonRequireHeroLevel
	63: optional string campUpradeToLevel
	64: optional string consumesThisGear
	//65: optional string heroLeveledUpResultMenuPrefab

	70: optional string xpGained
	71: optional string commonFull

	77: optional string freeTag

	79: optional string buyOnePack
	81: optional string youHave
	80: optional string heroEvolved
	83: optional string heroLeveledUp
	82: optional string getHeroes
	84: optional string thisAccount
	85: optional string heroFusion_SelectedMaxHero
	86: optional string heroFusion_MaxXP
	87: optional string heroFusion_NoStats

	91: optional string camp_Training
	92: optional string unlockAt

	95: optional string needMoreLootTicket
	96: optional string raidsWinLoseTrophies
	//97: optional string menuId_BattleMenuRaidMode
	98: optional string globalRank
	99: optional string text_Title_Ready_To_Battle
	100: optional string text_Edit_Team
	101: optional string text_Battle
	102: optional string text_Reroll
	103: optional string text_Defense_Team
	104: optional string text_Battle_Currency_Cost_Color
	105: optional string text_AutoWin
	106: optional string text_Title_Prepare_For_Battle
	
	107: optional string text_Title_Campaign_Name
	//108: optional string menuId_BattleMenuCampaignMode
	109: optional string text_Raid_Result_Trophy_Win
	110: optional string text_Raid_Result_Trophy_Lose
	111: optional string text_Title_League
	112: optional string text_Rematch
	
	113: optional string text_Battle_Menu_Team_Power
	114: optional string text_Guild_Online_Member
	//115: optional string menuId_GuildMenu
	116: optional string text_Guild_Members
	
	117: optional string text_AutoWin_Replay_Desc
	118: optional string text_AutoWin_YouHave
	119: optional string text_AutoWin_LootTickets
	120: optional string text_AutoWin_GetMore
	121: optional string text_AutoWin_ChanceOfWining
	122: optional string text_AutoWin_AmountReplays
	123: optional string text_AutoWin_MaxStamina
	124: optional string ability
	125: optional string enchantment
	126: optional string specialMove
	127: optional string nameColonDescription
	128: optional string text_Camp_Slot_Unlock
	129: optional string text_Camp_Slot_SkipWait
	130: optional string text_Camp_Slot_Collect
	131: optional string text_Camp_Slot_Train
	
	134: optional string text_Select_Border
	135: optional string text_Select_Avatar
	136: optional string text_Setup_Avatar
	137: optional string text_Save
	138: optional string text_Nothing
	139: optional string text_VIP
	140: optional string text_Create_Crew
	141: optional string text_Edit_Crew

	143: optional string text_AllowInvites
	144: optional string text_DoesNotAllowInvites
	145: optional string text_Promote
	146: optional string text_Rush
	147: optional string text_Train
	148: optional string text_Collect
	149: optional string text_Upgrade
	150: optional string text_Resources
	151: optional string text_TrainingTime
	152: optional string text_ChooseTraining
	153: optional string text_TrainingCamp
	154: optional string text_Achievements
	155: optional string text_HeroShop
	156: optional string text_Messages
	157: optional string text_VIPLevel
	158: optional string text_PlayerRank
	159: optional string text_MakeLeader
	160: optional string text_TimeLeft
	161: optional string text_Create
	162: optional string text_Search
	163: optional string text_EnterMessage
	164: optional string text_ReplyMessage
	165: optional string text_SearchInputPlaceHolder
	166: optional string text_MakeFriends
	167: optional string text_JoinCrewNow
	168: optional string text_Buy
	169: optional string text_EnemyTurn
	170: optional string text_NoConnection
	171: optional string text_Free
	172: optional string text_FinishTraining
	173: optional string text_Hero
	174: optional string text_Heroes
	176: optional string text_VIPLevelBenefits
	177: optional string text_VIPNextLevel
	178: optional string camp_Ready
	179: optional string text_Go
	180: optional string text_ReqMatAndRes
	181: optional string text_DailyQuests

	183: optional string text_NeedMoreSkillPoint
	184: optional string text_UnlockSkillSlot
	185: optional string text_RestoreAccount
	186: optional string text_SkillSlotUnlocked
	187: optional string text_ServerError

	191: optional string text_Credits
	192: optional string text_CreditsTitle
}

typedef string LocalizedStringEntryID

struct LocalizedStringEntry
{
	1: required LocalizedStringEntryID localizedStringEntryId
	2: required string value
}

struct HeroSummon
{
	1: required HeroSummonID heroSummonId
	// deprecated
	//2: optional PurchaseOfferID purchaseOfferId
	3: optional i32 minHeroes
	// If maxHeroes == 2, then the user can win 2 heroes
	4: optional i32 maxHeroes
	5: optional i32 weightCommon
	6: optional i32 weightUncommon
	7: optional i32 weightRare
	8: optional i32 weightEpic
	9: optional i32 weightLegendary
	10: optional AffinityID affinityId
	// deprecated
	11: optional CurrencyID tokenCurrencyId
	12: optional HeroSummonID overrideHeroSummonId
	13: optional i32 overridePurchaseCount
	14: optional map<i32, HeroSummon> heroSummonOverrides
	15: optional bool setUserAffinity
	16: optional list<HeroID> guaranteedHeroIds
	17: optional bool autoAddToTeam
	18: optional bool matchUserAffinity
}

enum SkillTypeID
{
	PassiveSkill = 0,
	BumpCombo,
	EnergyShot,
	Enchantment,
	// Deprecated
	//Ability,
	// Not implemented
	Mark,
	StatBumper,
	// Like a bump combo attack, but launched when hero hits an enemy
	BasicAttack,
	// Fired automatically - esp for enemy attacks
	Attack,
	NotUsed
}

enum WhenToShootID
{
	EveryTurn = 0,
	MyTurn,
	CycleSkills,
}

struct Skill
{
	1: required string skillId
	2: required LocalizedString display
//	3: optional string skillStatProfileId
	4: required SkillTypeID skillTypeId
	5: optional string hintSkillStatProfileId
	6: optional LocalizedString description
	7: optional AssetID iconImagePath
	8: optional WhenToShootID whenToShootId
//	9: optional bool highlight
	10: optional double predelaySeconds
	11: optional string heroSkillIconId
	12: optional double maxBadEnergy
}

struct HeroSkillIcon
{
	1: required string heroSkillIconId
	2: required AssetID prefabPath
	3: required AssetID iconPath
	4: required AssetID iconDisabledPath
	// does not seem to be used
	//5: optional AssetID activeBorderImagePath
}

struct SkillStatProfile
{
	1: required string skillStatProfileId
	// Populated by mutator
	2: optional list<SkillStatProfileEntry> skillStatProfileEntries
}

enum ModTypeID
{
	Physical,
	HeroStat,
}

enum DurationID
{
	Bump,
	Shot,
	Scene,
	Level
}

struct SkillStatProfileEntry
{
	1: required string skillStatProfileId
	2: required HeroStatID heroStatId
	3: required i32 inflectLevelNum
	4: required double baseValue
	5: required double maxValue
	6: required double inflectValue
	7: required DurationID durationId
	8: required ModTypeID modTypeId
}

struct StrengthProfile
{
	1: required string strengthProfileId
	2: optional list<i32> baseHealth
	3: optional list<i32> baseDamage
	5: optional list<i32> baseSpeed
	6: optional list<i32> baseRest
	7: optional list<i32> maxHealth
	8: optional list<i32> maxDamage
	10: optional list<i32> maxSpeed
	11: optional list<i32> maxRest
	12: optional list<i32> baseMass
	13: optional list<i32> maxMass
	14: optional list<i32> baseDrag
	15: optional list<i32> maxDrag
	// 16: optional list<i32> baseHeal
	// 17: optional list<i32> maxHeal
	18: optional i32 speedInflectLevelNum
	19: optional list<i32> inflectSpeed
	20: optional i32 healthInflectLevelNum
	21: optional list<i32> inflectHealth
	24: optional i32 damageInflectLevelNum
	25: optional list<i32> inflectDamage
	26: optional list<i32> basePhysicalAttack
	27: optional list<i32> maxPhysicalAttack
	28: optional list<i32> basePhysicalDefense
	29: optional list<i32> maxPhysicalDefense
	30: optional list<i32> baseMagicAttack
	31: optional list<i32> maxMagicAttack
	32: optional list<i32> baseMagicDefense
	33: optional list<i32> maxMagicDefense
}

struct PhysicsProfile
{
	1: required string physicsProfileId
	2: required double reactDurationSeconds
	3: optional double reactTranslate
	4: optional double reactTranslateHz
	5: optional double reactTranslateSeconds

	7: required double shakeFrequency
	8: optional double shakeBodyRotation
	9: optional double shakeBoneShear
	10: optional double shakeBoneScaleX
	11: optional double shakeBoneScaleY
	12: optional double shakePositionX
	13: optional double shakePositionY
	14: optional double shakeBonePositionX
	15: optional double shakeBonePositionY
	16: optional double shakeBoneRotation
}

struct AnimationProfile
{
	1: required string animationProfileId
	2: required double eyeSpeed
}

enum GenderID
{
	Male,
	Female,
}

struct Gender
{
	1: required GenderID genderId
	2: required LocalizedString display
}

enum MovementTypeID
{
	Normal = 0,
	Immobile,
}

typedef string EffectListID

struct EffectList
{
	1: required EffectListID effectListId
	// Populated by mutator
	3: optional list<EffectListEntry> effectListEntries
}

struct EffectListEntry
{
	// Removed by mutator
	1: optional EffectListID effectListId
	2: required AssetID prefabPath
	3: required bool autoReclaim
	4: required i32 poolSize
	6: optional double releaseSeconds
	// Checked by mutator
	7: optional bool disable
}

struct VisualEffectsProfile
{
	1: required string visualEffectsProfileId
	2: required string hitEnemyEffectListId
	3: required string physicalDamageEffectListId
	4: required string magicDamageEffectListId
	5: required string deathEffectListId
	6: required string energyShotZoomEffectListId
	7: required string energyShotParticlesEffectListId
	8: required string trailEffectListId
	9: required string enterSceneEffectListId
	10: required string hitWallEffectListId
	11: optional string hitTeammateEffectListId
	12: optional string hitByTeammateEffectListId
	13: optional string dramaticPauseEffectListId
}

enum CollisionLayerID
{
	DisableCollisions = 0,
	Hero = 1,
	Teammate = 2,
	Enemy = 3,
	Wall = 4,
	Projectile = 5,
	EdgeElement = 6,
}

struct HeroBody
{
	1: required HeroID heroId
	2: optional BodyTypeID bodyTypeId
	3: required HeroBodyTypeID heroBodyTypeId
	4: optional LocalizedString display
	5: required RarityID rarityId
	6: required AffinityID affinityId
	7: optional CampaignID unlockCampaignId
	8: optional EvolutionProfileID evolutionProfileId
	9: optional GenderID genderId
	10: optional string animationProfileId
	11: optional LocalizedString summary
	12: optional LocalizedString description
	// Deprecated
	13: optional double drag
	14: optional string strengthProfileId
	15: optional list<string> winAnimations
	16: optional list<string> loseAnimations
	17: optional AssetID bodyCirclePrefab
    18: optional list<string> heroInfoAnimations
    19: optional list<string> levelUpAnimations
	20: required AssetID heroPrefab
	21: optional AssetID cardImage
	22: optional AssetID bwCardImage
	23: optional SpecialMoveTrigger specialMoveTrigger
	// Populated by mutator
	24: optional list<string> skillIds
	25: optional i32 enchantmentSkillSlotNum
	26: optional i32 bumpComboSkillSlotNum
	27: optional i32 energyShotSkillSlotNum
	28: optional list<string> idleAnimations
	29: optional string visualEffectsProfileId
	// Deprecated
	30: optional string physicsProfileId
	31: optional string magicReactProfileId
	32: optional AssetID healthBarPrefab
	33: optional double healthBarYOffset
	37: optional string heroSoundProfileId
	38: optional string physicalReactProfileId
	// Removed by mutator - see skillIds
	40: optional string skillId0
	// Removed by mutator - see skillIds
	41: optional string skillId1
	// Removed by mutator - see skillIds
	42: optional string skillId2
	// Removed by mutator - see skillIds
	43: optional string skillId3
	44: optional MovementTypeID movementTypeId
	45: optional LifespanTypeID lifespanTypeId
	46: optional AssetID skillIconHolderPrefab
	47: optional double attackAnimDelaySeconds
	48: optional string Nickname
	// Deprecated
	//55: optional i32 maxBadEnergy
}

struct HeroSoundProfile
{
	1: required HeroID heroId
	2: optional AssetID shootClip
	3: optional AssetID myTurnClip
	4: optional AssetID deathClip
	5: optional AssetID energyShotClip
	6: optional AssetID worriedClip
	7: optional AssetID aimClip
	8: optional AssetID hitClip
	9: optional AssetID physicalDamageClip
}

enum ImageTypeID
{
	Simple = 0,
	Sliced,
	Tiled,
	Filled,
}

struct Campaign
{
	1: required CampaignID campaignId
	2: required LocalizedString display
	3: optional i32 order
	4: optional bool hideTitle
	5: optional string raidLevelSceneId
	10: optional AssetID imagePath
	
	11: optional AssetID backgroundImagePath
	12: optional AssetID campaignLoadingSignPath
	13: optional ImageTypeID backgroundImageTypeId
	20: optional list<HeroID> unlockedHeroIds
	21: optional list<LevelID> levelIds
	30: optional AssetID iconPrefabPath
	31: optional AssetID battleMenuImagePath
	32: optional AssetID campaignSignPath
	33: optional AssetID campaignLevelFontPath
	34: optional double highlightOpacity
	35: optional bool showIconShadow
}

struct Level
{
	1: required LevelID levelId
	2: required LocalizedString display
	3: optional CampaignID campaignId
	# Populated by mutator
	4: optional list<LevelSceneID> levelSceneIds
	5: required i32 order
	6: optional double difficulty
	7: optional double valueCents
	8: optional i32 heroXp
	9: optional i32 globalOrder
	10: optional list<GearItemID> items1
	11: optional list<GearItemID> items2
	12: optional list<GearItemID> items3
	13: optional list<GearItemID> items4
	15: optional list<double> parms1
	16: optional list<double> parms2
	17: optional list<double> parms3
	18: optional list<double> parms4
	21: optional list<GearItemID> items5
	22: optional list<GearItemID> items6
	23: optional list<double> parms5
	24: optional list<double> parms6
	25: optional list<GearItemID> items7
	26: optional list<GearItemID> items8
	27: optional list<double> parms7
	28: optional list<double> parms8
	30: optional CurrencyID costCurrencyId
	31: optional i32 currencyCost
}

struct EdgeElementEntry
{
	1: required LevelSceneID edgeElementsProfileId
	2: required string edgeElementId
	3: optional i32 firstMove
	4: optional i32 lastMove
	5: optional double probability
	6: optional string groupId
}

struct EdgeElementsProfile
{
	1: required string edgeElementsProfileId
	// Populated by mutator
	2: optional list<EdgeElementEntry> edgeElementEntries
}

struct LevelScene
{
	1: required LevelSceneID levelSceneId
	2: optional LevelID levelId
	3: optional list<EnemySpawnPoint> enemySpawnPoints
	4: optional list<string> minigameMusicThemeIds
	5: optional i32 order
	6: optional AssetID levelPrefabPath
	9: optional string edgeElementsProfileId
	10: optional bool hasBoss
	11: optional list<double> startCameraPosition
	12: optional list<double> cameraPosition
	13: optional AssetID fightEffectListId
	14: optional AssetID playerTurnEffectListId
	15: optional double transitionY
	16: optional AssetID fanTransitionPath
	17: optional AssetID enemyTurnEffectListId
}

typedef string HeroStateID

struct HeroState
{
	1: required HeroID heroId
	2: required i32 evolutionLevel
	3: optional HeroStateID heroStateId
	// One slot status per slot. there are 6 (Config.HeroNumGearSlots) slots
	5: optional list<bool> slotStatus
	6: optional i32 xp
	7: optional list<i32> skillLevels
}

enum SpawnTypeID
{
	Normal = 0,
	Respawn,
	Disable,
}

struct EnemySpawnPoint
{
	1: required LevelSceneID levelSceneId
	3: optional i32 level
	4: optional i32 evolutionLevel
	5: optional HeroID heroId
	6: optional list<i32> skillLevels
	7: optional SpawnTypeID spawnTypeId
	8: optional list<i32> spawnParams
	9: optional bool highlight
	10: required double x
	11: required double y
	// Populated by mutator
	12: optional list<bool> slotStatus
	// Populated by mutator
	14: optional HeroState heroState
	15: optional i32 attackGroup
	16: optional double attackWait
}

enum PlacementTypeID
{
	Point,
	Line
}

struct EdgeElement
{
	1: required string edgeElementId
	2: required string skillStatProfileId
	3: required PlacementTypeID placementTypeId
	4: optional AssetID controllerPath
	5: optional AssetID effectPath
	6: optional EffectListID collisionEffectListId
	7: optional AssetID heroBadgePath
	8: optional EffectListID heroEffectListId
	9: optional i32 level
	10: optional string appearSoundId
	11: optional string launchSoundId
}

struct Color
{
	1: required ColorID colorId
	2: required double red
	3: required double green
	4: required double blue
	5: required double alpha
}

struct Affinity
{
	1: required AffinityID affinityId
	2: required ColorID colorId
	3: optional LocalizedString display
	5: optional AssetID heroInfoBgPath
	6: optional AssetID levelRibbonImagePath
	7: optional AssetID heroSummaryBgPath
	8: optional AssetID heroPurchaseCardFrame
	9: optional AssetID evolveSequenceBgPath
	10: optional AssetID healthBarPrefab
	11: optional AssetID aimArrowPrefabPath
	12: optional AssetID playerShieldImagePath
	13: optional AssetID playerXpBarImagePath
	20: required AssetID activeHeroMarkerPrefab
	// deprecated - was required
	21: optional AssetID bodyCirclePrefab
	30: optional AssetID userIconBackgroundImage
}

struct SoundClip
{
	1: required SoundClipID soundClipId
	2: optional string audioSourceId
	3: optional bool loop
	10: optional SoundClipListID soundClipListId
	20: optional AssetID path
}

struct SoundClipList
{
	1: required SoundClipListID soundClipListId
	10: optional list<SoundClipID> soundClipIds
}

struct ShopSection
{
	1: required string shopSectionId
	2: required i32 priority
	3: required LocalizedString display
	// Required only if section has a heading <--- this comment makes no sense
	//4: optional AssetID prefab
	5: optional i32 numItemsPerRow
	6: optional string sectionGroupId
	7: optional string sectionHeadingTemplate
	8: optional i32 rowHeightHint
	9: optional bool isDebug
}

struct EventSection
{
	1: required string eventSectionId
	2: required i32 priority
	3: required LocalizedString display
	5: optional i32 numItemsPerRow
	6: optional string sectionGroupId
	7: optional string sectionHeadingTemplate
	8: optional i32 rowHeightHint
	9: optional bool isDebug
}

//typedef string ShopOfferTemplateID
//
//struct ShopOfferTemplate
//{
//	1: required ShopOfferTemplateID shopOfferTemplateId
//	2: required AssetID prefab
//}

// WIP - do not use
typedef string PurchaseOfferID

// WIP - do not use
enum PurchaseOfferResetTypeID
{
	SystemMidnight,
	SystemTime,
	UserMidnight,
	UserTime,
}

struct PurchaseOffer
{
	1: required PurchaseOfferID purchaseOfferId
	2: optional string shopSectionId
//	3: optional ShopOfferTemplateID shopOfferTemplateID
	// NEW - move section prefabs to offer prefabs
	3: optional AssetID shopItemPrefab
	4: optional RankID rankMin
	5: optional RankID rankMax
	6: optional i32 priority
	7: optional PurchaseOfferID multiPackId
	// Danger flag means not to use optimistic update
	8: optional bool danger
	9: optional AssetID mainMenuIconPrefab
	10: optional VipLevelID vipLevelMin
	11: optional VipLevelID vipLevelMax
	12: optional CurrencyID productCurrencyId
	13: optional i32 productCurrencyCount
	14: optional CurrencyID tokenCurrencyId
	17: optional GuildRankID guildRankMin
	18: optional GuildRankID guildRankMax
	19: optional LocalizedString productTitle
	20: required CurrencyID costCurrencyId
	21: optional i32 currencyCost
	// maxPurchases - offer disappears once user has made this many purchases of this item
	22: optional i32 maxPurchases
	// Default - SystemMidnight
	23: optional PurchaseOfferResetTypeID purchaseOfferResetTypeId
	24: optional i32 purchaseResetSeconds
	// Unlocked when the specified purchaseOffer has reached maxPurchases and disappears
	25: optional PurchaseOfferID unlockPurchaseOfferId
	// iOS Price Tier - required for Cash purchases
	// Google Price Tier - required for Cash purchases
	26: optional i32 vipPointsAwarded
	27: optional AssetID bannerImage
	28: optional LocalizedString bannerText
	29: optional string itemImage
	30: optional string itemDescription
	31: optional string inboxPreviewImage
	32: optional string inboxBannerImage
	33: optional string inboxRibbonImage
	34: optional string inboxRibbonTitle
	35: optional i32 inboxPriority
	36: optional AssetID borderImage
	40: optional list<EventID> eventIds
	41: optional list<EventPhaseID> eventPhaseIds
	42: optional list<EventID> previewEventIds
	43: optional list<EventPhaseID> previewEventPhaseIds
	// Deprecated
	//44: optional AssetID effectIconPath
	// Deprecated
	//45: optional i32 effectNumber
}

struct GemPass
{
	1: required PurchaseOfferID purchaseOfferId
	3: required LocalizedString description
	5: required GiftMessageID welcomeGiftMessageId
	6: required i32 durationDays
	7: required i32 numGemsPerDay
	10: optional string iOSProductId
	11: optional string googleProductId
	// Deprecated - we now have separate PurchaseOffers for subscriptions. Use iOSProductId instead
	12: optional string iOSSubscriptionProductId
	// Deprecated - we now have separate PurchaseOffers for subscriptions. Use googleProductId instead
	13: optional string googleSubscriptionProductId
	14: optional GenericDialogID welcomeGenericDialogId
	15: optional InboxMessageID subscriptionBonusMessageId
}

struct SubscriptionPurchaseOffer
{
	1: required string subscriptionPurchaseOfferId
	2: required string purchaseOfferId
	3: optional i32 subscriptionBonusGems
}

struct GemPack
{
	1: required PurchaseOfferID purchaseOfferId
	3: required LocalizedString description
	7: required i32 numGems
	10: optional string iOSProductId
	11: optional string googleProductId
}

struct CashPurchaseInfo
{
	1: required PurchaseOfferID purchaseOfferId
	10: optional string iOSProductId
	11: optional string googleProductId
	12: optional string iOSProductIdUndiscounted
	13: optional string googleProductIdUndiscounted
}

enum CurrencyTypeID
{
	Resource,
	Hero,
	Cash,
	Gear,
	Chest,
	// Deprecated
	HeroSummon
}

struct Currency
{
	1: required CurrencyID currencyId
	2: optional LocalizedString pluralName
	3: optional LocalizedString singularName
	// Populated by mutator
    4: optional list<i32> maxByRank
	5: optional CurrencyTargetID currencyTargetId
	6: optional i32 startBalance
	7: optional CurrencyTypeID currencyTypeId
	8: optional list<i32> textColorRgba
	9: optional AssetID iconImagePath
	10: optional AssetID cardImagePath
	11: optional AssetID inboxIconImagePath
	12: optional i32 goldExchangeValue
	13: optional i32 value
	14: optional AssetID hudElementPrefabPath
	15: optional i32 hudSlotNum
	16: optional string purchaseMenuId
	17: optional AssetID cardImagePathDisabled
	18: optional bool hideInRewards
}

struct CurrencyRecharge
{
	1: required CurrencyID currencyId
	2: required i32 defaultRechargeSeconds
}

// removed by mutator
struct CurrencyRankMaxEntry
{
	1: required CurrencyID currencyId
	2: required i32 rankId
	3: required i32 max
}

struct Rank
{
	1: required RankID rankId
	2: required i32 xp
	3: optional i32 maxStamina
	4: optional i32 maxHeroes
	5: optional i32 maxRecruits
	6: optional ChestID rewardChestId
	7: optional list<CurrencyID> rewardCurrencies
    8: optional list<i32> rewardCurrencyCounts
}

typedef i32 VipLevelID

struct VipLevel
{
	1: required VipLevelID vipLevelId
	2: required i32 vipPoints
	3: required i32 percentPurchaseGemsBonus
	4: required i32 numFreeDailyLootTickets
	// Deprecated
	5: optional i32 maxDailyStaminaPurchases
	6: optional i32 numDailyLootTickets
	7: optional LocalizedString benefitsDesc
}

struct Location
{
	1: required LocationID locationId
	2: optional string countryCode
	3: optional i32 isoNumericId
	4: optional i32 displayOrder
	5: optional bool hide

	10: optional AssetID flagImage
	12: required LocalizedString countryDisplay
	16: optional LocalizedString shortDisplay

	20: optional string capital
	21: optional string continent
    22: optional string country
}

enum DamageType
{
	Physical,
	Magic,
	Pure
}

struct TutorialStep
{
	1: required TutorialStepID tutorialStepId
	2: required TutorialID tutorialId
	3: required i32 order
	4: optional double preDelaySeconds
	5: optional double postDelaySeconds
	6: optional i32 xOffset
	7: optional i32 yOffset
	8: optional bool darkener
	9: optional string soundId
	10: optional bool isCheckpoint
	11: optional bool blockMouse
	19: optional LocalizedString titleText
	20: optional LocalizedString bodyText
	21: optional AssetID imagePath
	22: optional AssetID panelPrefabPath
	23: optional string animationName
	30: optional double arrowScale
	31: optional ArrowDirection arrowDirection
	32: optional string arrowTarget
	33: optional i32 arrowOffsetX
	34: optional i32 arrowOffsetY
	40: optional list<TutorialCheckpointID> openCheckpoints
	41: optional list<TutorialCheckpointID> blockerCheckpoints
	42: optional list<TutorialCheckpointID> passCheckpoints
	
	48: optional list<TutorialCheckpointID> cancelCheckpoints
	49: optional list<TutorialCheckpointID> allowCheckpoints
	
	51: optional ActionID okayButtonActionId
	52: optional ActionID openActionId
	53: optional LocalizedString okayButtonText
	60: optional string highlightTarget
	61: optional double highlightOffsetX
	62: optional double highlightOffsetY
	63: optional double highlightScaleX
	64: optional double highlightScaleY
	// New
	65: optional double highlightOpacity
	66: optional double highlightFadeInSeconds
	67: optional double highlightFadeOutSeconds
	// New
	68: optional AssetID highlightImage
	// New
	69: optional double highlightZoomInSeconds
	// New
	70: optional double highlightZoomOutSeconds
}

enum TutorialSpecialFlag
{
	CloseAllModalsOnStart,
}

struct Tutorial
{
	1: required TutorialID tutorialId
	3: optional bool autoCancel
	4: optional i32 minRank
	5: optional list<string> dontCancelPoints
	6: optional list<TutorialSpecialFlag> specialFlags
	10: optional list<TutorialStep> tutorialSteps
	20: optional string completionFlag
	31: optional list<string> enableFlags
}

struct Chest
{
	1: required ChestID chestId
	2: optional i32 offerCost
	3: optional bool autoPlace
	10: optional i32 duration
	11: optional LocalizedString display
	20: optional i32 numCommon
	21: optional i32 numRare
	22: optional i32 numEpic
	23: optional i32 numLegendary
	24: optional i32 numCommonGuaranteed
	25: optional i32 numRareGuaranteed
	26: optional i32 numEpicGuaranteed
	27: optional i32 numUncommon
	28: optional i32 numUncommonGuaranteed
	30: optional i32 minGold
	31: optional i32 maxGold
	32: optional i32 minGems
	33: optional i32 maxGems
	34: optional i32 maxHeroes
	40: optional bool matchUserAffinity
	41: optional AffinityID setUserAffinity
	50: optional AssetID imageSprite
	51: optional AssetID awardChestClip
	52: optional AssetID openChestClip
	60: optional bool goToMinigame
	# populated by mutator
	70: optional list<HeroID> guaranteedHeroes
	71: optional AssetID chestPrefab
	# populated by mutator
	72: optional list<GuaranteedCurrency> guaranteedCurrencies
}

struct GuaranteedHero
{
	1: required ChestID chestId
	2: required HeroID heroId
}

struct GuaranteedCurrency
{
	1: required ChestID chestId
	2: required CurrencyID currencyId
	3: required i32 count
	4: optional string rewardGroupId
}

struct RuntimePlatform
{
	1: required RuntimePlatformID runtimePlatformId
}

struct Header
{
	1: required i32 schemaVersion
	2: required i32 configVersion
}

struct HeroLevelXp
{
	1: required i32 heroLevel
	// Removed by mutator
	2: optional i32 commonXpEvo1
	// Removed by mutator
	3: optional i32 commonXpEvo2
	// Removed by mutator
	// DEPRECATED
	4: optional i32 commonXpEvo3
	// Removed by mutator
	5: optional i32 uncommonXpEvo1
	// Removed by mutator
	6: optional i32 uncommonXpEvo2
	// Removed by mutator
	7: optional i32 uncommonXpEvo3
	// Removed by mutator
	10: optional i32 rareXpEvo1
	// Removed by mutator
	11: optional i32 rareXpEvo2
	// Removed by mutator
	12: optional i32 rareXpEvo3
	// Removed by mutator
	13: optional i32 rareXpEvo4
	// Removed by mutator
	14: optional i32 epicXpEvo1
	// Removed by mutator
	20: optional i32 epicXpEvo2
	// Removed by mutator
	21: optional i32 epicXpEvo3
	// Removed by mutator
	22: optional i32 epicXpEvo4
//	// Created by mutator
//	30: optional list<i32> commonXpByEvo
//	// Created by mutator
//	31: optional list<i32> rareXpByEvo
//	// Created by mutator
//	32: optional list<i32> epicXpByEvo
	// Created by mutator
	35: optional list<list<i32>> xpByEvoByRarity
}

struct HeroUpgradeGoldCost
{
	1: required i32 heroLevel
	2: optional i32 commonUpgradeCost
	3: optional i32 rareUpgradeCost
	4: optional i32 epicUpgradeCost
	5: optional i32 legendaryUpgradeCost
	6: optional i32 uncommonUpgradeCost
}

typedef string InboxSectionID
typedef string GuildMemberListSectionID
typedef string SectionHeadingID
typedef string SectionHeadingTemplateID
typedef string SectionTopperID
typedef string SectionTopperTemplateID
typedef string SectionBottomID
typedef string SectionBottomTemplateID
typedef string GuildSectionItemTemplateID
typedef string GuildSectionItemID

# Header, top, bottom are shared between views. Only the items vary between views.
typedef string GuildMemberListItemTemplateID
typedef string GuildMemberListItemID
typedef string GiftMessageTemplateID
typedef string GiftMessageID

struct SectionHeadingTemplate
{
	1: required SectionHeadingTemplateID sectionHeadingTemplateId
	2: required AssetID prefab
	3: required AssetID backgroundImage
}

struct SectionHeading
{
	1: required SectionHeadingID sectionHeadingId
	2: required SectionHeadingTemplateID sectionHeadingTemplateId
	3: required LocalizedString display
}

struct SectionTopperTemplate
{
	1: required SectionTopperTemplateID sectionTopperTemplateId
	2: required AssetID prefab
	3: optional AssetID backgroundImage
}

struct SectionTopper
{
	1: required SectionTopperID sectionTopperId
	2: required SectionTopperTemplateID sectionTopperTemplateId
}

struct SectionBottomTemplate
{
	1: required SectionBottomTemplateID sectionBottomTemplateId
	2: required AssetID prefab
	3: required AssetID backgroundImage
}

struct SectionBottom
{
	1: required SectionBottomID sectionBottomId
	2: required SectionBottomTemplateID sectionBottomTemplateId
	3: optional LocalizedString display
	4: optional LocalizedString buttonText
}

struct GuildSectionItemTemplate
{
	1: optional GuildSectionItemTemplateID guildSectionItemTemplateId
	2: optional AssetID prefab
	3: optional AssetID backgroundImage
}

struct GuildSectionItem
{
	1: optional GuildSectionItemID guildSectionItemId
	2: optional GuildSectionItemTemplateID guildSectionItemTemplateId
}

struct GuildMemberListItemTemplate
{
	1: required GuildMemberListItemTemplateID guildMemberListItemTemplateId
	2: required AssetID prefab
	3: required AssetID backgroundImage
}

struct GuildMemberListItem
{
	1: required GuildMemberListItemID guildMemberListItemId
	2: required GuildMemberListItemTemplateID guildMemberListItemTemplateId
	3: required LocalizedString display
}

struct InboxSection
{
	1: required InboxSectionID inboxSectionId
	2: required i32 priority
	10: required SectionHeadingID sectionHeadingId
	11: required SectionTopperID sectionTopperId
	// Idk if this is necessary - item identifies the section, so this is redundant
    //12: required GiftMessageTemplateID giftMessageTemplateId
	13: required SectionBottomID sectionBottomId
}

struct GuildMemberListSection
{
	1: required GuildMemberListSectionID guildMemberListSectionId
	2: required i32 priority
	10: required SectionHeadingID sectionHeadingId
	11: required SectionTopperID sectionTopperId
	// Idk if this is necessary - item identifies the section, so this is redundant
	//12: required GuildMemberListItemID guildMemberListItemId
	13: required SectionBottomID sectionBottomId
	14: optional GuildSectionItemID guildSectionItemId
}

typedef string GuildListSectionID

struct GuildListSection
{
	1: required GuildListSectionID guildListSectionId
	2: required i32 priority
	10: required SectionHeadingID sectionHeadingId
	11: required SectionTopperID sectionTopperId
	13: required SectionBottomID sectionBottomId
	14: optional GuildSectionItemID guildSectionItemId
}

typedef string GuildListItemTemplateID
struct GuildListItemTemplate
{
	1: required GuildListItemTemplateID guildListItemTemplateId
	2: required AssetID prefab
}

typedef string GuildListItemID

struct GuildListItem
{
	1: required GuildListItemID guildListItemId
	2: required GuildListItemTemplateID guildListItemTemplateId
}

typedef string ChatMessageTemplateID

struct ChatMessageTemplate
{
	1: required ChatMessageTemplateID chatMessageTemplateId
	10: required AssetID itemPrefab
	11: required AssetID topperPrefab
	// Leaders and non-leaders see different bottom prefabs
	12: required AssetID bottomPrefab
	13: required AssetID bottomPrefabLeader
}

typedef string ChatMessageID

struct ChatMessage
{
	1: required ChatMessageID chatMessageId
	2: optional ChatMessageTemplateID chatMessageTemplateId
	3: optional LocalizedString body
	10: required AssetID itemImage
	11: required AssetID topperImage
	12: required AssetID bottomImage
}

struct CurrencyItem
{
	1: required CurrencyID currencyId
	2: required i32 count
}

// Mutator: Converted to CurrencyItem and moved into CsMessage.currencyItems
struct GiftMessageCurrencyItem
{
	1: required GiftMessageID giftMessageId
	2: required CurrencyID currencyId
	3: required i32 count
}

typedef string SimplePopupTemplateID

struct SimplePopupTemplate
{
	1: required SimplePopupTemplateID simplePopupTemplateId
	10: required AssetID prefab
}

typedef string SimplePopupID

struct SimplePopup
{
	1: required SimplePopupID simplePopupId
	2: required SimplePopupTemplateID simplePopupTemplateId
	11: required AssetID backgroundImage
	12: optional AssetID buttonImage
	20: optional LocalizedString title
	21: optional LocalizedString body
	22: optional LocalizedString buttonText
}

struct GiftMessageTemplate
{
	1: required GiftMessageTemplateID giftMessageTemplateId
	10: required AssetID prefab
	11: required AssetID backgroundImage
	12: required AssetID buttonImage
}

struct GiftMessage
{
	1: required GiftMessageID giftMessageId
	// TODO: template should come from section
	2: required GiftMessageTemplateID giftMessageTemplateId
    3: optional InboxSectionID inboxSectionId
    5: optional bool canClaimAll
    6: optional GiftMessagePopupID giftMessagePopupId
    7: optional AssetID topIcon
    8: optional string messageLimitId
    10: optional string title
    11: optional string subtitle
	12: optional string body
	13: optional LocalizedString okayButtonText
	14: optional LocalizedString cancelButtonText
	# type should just be CurrencyItem but I can't get thrift classes to work in our python mutators
    20: optional list<GiftMessageCurrencyItem> currencyItems
}

typedef string GiftMessagePopupTempateID

struct GiftMessagePopupTempate
{
	1: required GiftMessagePopupTempateID giftMessagePopupTempateId
	10: required AssetID prefab
}

typedef string GiftMessagePopupID

struct GiftMessagePopup
{
	1: required GiftMessagePopupID giftMessagePopupId
	2: required GiftMessagePopupTempateID giftMessagePopupTempateId
	10: optional AssetID background
	11: optional AssetID centerIcon
	12: optional AssetID topIcon
}

struct ScheduledGiftMessage
{
	1: required GiftMessageID giftMessageId
    2: required DateTimeUTC startTime
    3: required i32 repeatPeriodMinutes
    4: optional i32 repeatDurationMinutes
    5: optional i32 numNotificationDays
    6: optional i32 notificationCooldownSeconds
}

typedef string OfferPackShopItemTemplateID

struct OfferPackShopItemTemplate
{
	1: required OfferPackShopItemTemplateID offerPackShopItemTemplateId
	2: required AssetID prefab
	3: optional AssetID buyButtonImage
	4: optional AssetID discountStickerImage
	5: optional AssetID discountCrossoutImage
	6: optional AssetID timerBgImage
	7: optional AssetID timerClockImage
	8: optional AssetID clockHandImage
}

typedef string OfferPackShopItemID

struct OfferPackShopItem
{
	1: required OfferPackShopItemID offerPackShopItemId
	2: required OfferPackShopItemTemplateID offerPackShopItemTemplateId
	3: required AssetID backgroundImage
    4: optional string title
    5: optional string text1
    6: optional string text2
    7: optional string text3
	10: optional LocalizedString buyButtonText
    11: optional LocalizedString discountText
    12: optional LocalizedString undiscountedText
}

typedef string OfferPackZoomItemTemplateID

struct OfferPackZoomItemTemplate
{
	1: required OfferPackZoomItemTemplateID offerPackZoomItemTemplateId
	2: required AssetID prefab
	3: optional AssetID buyButtonImage
	4: optional AssetID discountStickerImage
	5: optional AssetID discountCrossoutImage
	6: optional AssetID timerBgImage
	7: optional AssetID timerClockImage
	8: optional AssetID timerHandImage
}

typedef string OfferPackZoomItemID

struct OfferPackZoomItem
{
	1: required OfferPackZoomItemID offerPackZoomItemId
	2: required OfferPackZoomItemTemplateID offerPackZoomItemTemplateId
	3: required AssetID backgroundImage
    4: optional string titleText
    5: optional string subtitleText
    6: optional string stickerText
    10: optional string text1
    11: optional string text2
    12: optional string text3
	13: optional LocalizedString buyButtonText
    14: optional LocalizedString discountText
    15: optional LocalizedString undiscountedText
}

typedef string EventID
typedef string ActivityID

enum EventPhaseID
{
    Nothing = 0,
    Preview,
    Main,
    Recap,
    PreviewMain,
    MainRecap,
}

struct Event
{
    1: required EventID eventId
    10: required DateTimeUTC previewStartTime
    11: required DateTimeUTC mainStartTime
    12: required DateTimeUTC mainEndTime
    13: required DateTimeUTC recapEndTime
    20: optional i32 repeatSeconds
}

struct EventActivity
{
	1: required string eventActivityId
	2: required string eventId
	3: optional AssetID eventListMainItemPrefab
	4: optional AssetID eventListMainSectionId
	5: optional AssetID eventListOfferItemPrefab
	6: optional AssetID eventListOfferSectionId
	7: optional LocalizedString display
	8: optional AssetID eventListMainItemImage
}

// this structure does not make sense
struct EventPhase
{
	1: required EventID eventId
	2: required EventPhaseID eventPhaseId
}

struct Activity
{
	1: required ActivityID activityId
	# ordered lists, i.e., eventId[3] and eventPhases[3] go together:
	2: optional list<EventPhase> eventPhases
	10: required LocalizedString display
	20: required RankID showRank
	21: required RankID hideRank
	30: optional list<BundleID> bundleIds
}

typedef string EnchantmentID

enum TriggerTypeID
{
	Invisible = 0
	AlwaysOn,
	Temp,
	AfterHeroes,
	AfterEnemies,
	OverTime,
	OverDistance,
}

struct Enchantment
{
	1: required EnchantmentID enchantmentId
	2: optional AssetID enchantAudioPath
	3: optional AssetID actionAudioPath
	5: required bool isPositive
	6: optional AssetID effectPrefab
	8: optional AssetID actionPrefab
	9: optional string groupId
	11: optional TriggerTypeID triggerTypeId
	12: optional string skillStatProfileId
	13: optional double triggerParam
	15: optional AssetID prefabPath
	21: optional AssetID badgeImage
}

enum GenderMatchID
{
	DontCare = 0,
	Match,
	NotMatch,
	Male,
	Female,
}

enum AffinityMatchID
{
	DontCare = 0,
	Match,
	NotMatch,
	Red,
	Blue,
	Green,
	Yellow,
	Black
}

struct PassiveSkill
{
	1: required string skillId
	// Deprecated
	2: optional bool isStat
	// Deprecated
	3: optional bool isPositive
	// Deprecated
	4: optional bool matchAffinity
	// Deprecated
	5: optional bool matchGender
	// Deprecated
	6: optional bool oppositeGender
	7: optional AffinityMatchID affinityMatchId
	8: optional GenderMatchID genderMatchId
	9: optional string skillStatProfileId
}

//// Deprecated
//struct Ability
//{
//	1: required string skillId
//	2: optional bool isStat
//	3: optional bool isPositive
//	4: optional bool matchAffinity
//	5: optional bool matchGender
//	6: optional bool oppositeGender
//	10: optional AssetID abilityPrefabPath
//	11: optional AssetID effectPrefabPath
//}

struct StatBumper
{
	1: required string skillId
	2: optional AssetID effectPrefabPath
	3: optional string skillStatProfileId
}

enum HeroStatID
{
	Hp,
	Damage,
	Speed,
	Drag,
	Restitution,

	PhysicalAttack,
	PhysicalDefense,
	MagicAttack,
	MagicDefense,
}

struct HeroStat
{
	1: required HeroStatID heroStatId
	2: optional LocalizedString display
	3: optional AssetID icon
	4: optional i32 displayOrder
	5: optional bool showInHeroInfo
}

enum HeroStatisticID
{
	DamageDealt,
	HpDealt,
	HpReceived,
}

struct HeroStatistic
{
	1: required HeroStatisticID heroStatisticId
	2: optional LocalizedString display
	3: optional AssetID icon
	4: optional i32 displayOrder
}

enum DropTypeID
{
	All,
	DropOnly,
	CraftOnly
}

typedef string GearItemID
struct GearItem
{
	1: required GearItemID gearItemId
	2: required RarityID rarityId
	3: required LocalizedString display
	// Deprecated- use currency image instead
	//4: optional AssetID catalogImage
	5: optional i32 requiresLevel
	6: optional i32 craftGoldCost
	7: optional DropTypeID dropTypeId
	// Deprecated
	8: optional i32 orderDeprecated
	9: optional i32 valueCents
	10: optional list<GearItemID> craftItemIds
	11: optional list<i32> craftItemCounts
	// Deprecated- move to currency - was required
	//12: optional AssetID catalogImageDisabled
	13: optional ProgressionID progressionId
	14: optional list<i32> order
	22: optional CurrencyID sellCurrencyId
	23: optional i32 sellCurrencyAmount
	24: optional list<HeroStatID> heroStatIds
	25: optional list<double> heroStatAmounts
}

typedef string EvolutionProfileID
typedef string EvolutionLevelProfileID

struct EvolutionLevelProfile
{
	1: required EvolutionLevelProfileID evolutionLevelProfileId
	// Removed by mutator
	2: optional GearItemID gearItemId0
	// Removed by mutator
	3: optional GearItemID gearItemId1
	// Removed by mutator
	4: optional GearItemID gearItemId2
	// Removed by mutator
	5: optional GearItemID gearItemId3
	// Removed by mutator
	6: optional GearItemID gearItemId4
	// Removed by mutator
	7: optional GearItemID gearItemId5
	8: optional CurrencyID costCurrencyId
	9: optional i32 costCurrencyCount

	// Populated by mutator
	10: optional list<GearItemID> gearItemIds
	// What's this for?
//	11: optional LocalizedString display
	// Populated by mutator
	12: optional i32 numGearSlots
	13: optional i32 valueCents
}

struct EvolutionProfile
{
	1: required EvolutionProfileID evolutionProfileId
	2: optional list<EvolutionLevelProfile> evolutionLevelProfiles
	// Deprecated
	10: optional i32 baseEvolutionLevel
}

struct EvolutionProfileLevelLink
{
	1: required EvolutionProfileID evolutionProfileId
	2: required EvolutionLevelProfileID evolutionLevelProfileId
	3: required i32 evolutionLevelNum
}

typedef string MenuID

struct Menu
{
	1: required MenuID menuId
	2: required AssetID prefabPath
	3: optional AssetID backgroundImage
	4: optional SoundClipID openSoundId
	5: optional SoundClipID closeSoundId
	6: optional string hudProfileId
}

struct Prefab
{
	1: required string prefabId
	2: required AssetID prefabPath
}

struct Rarity
{
	1: required RarityID rarityId
	2: required LocalizedString display
	3: optional AssetID iconFramePath
	4: optional list<i32> heroMaxLevelByEvolutionLevel
	5: optional AssetID gearIconFramePath
	6: optional i32 heroFusionXpBase
	7: optional i32 heroFusionXpEffectiveLevelMultiplier
	8: optional i32 itemValue
	9: optional list<i32> heroUpgradeGoldCosts
	10: optional i32 heroMaxEvolutionLevel
}

typedef string AchievementEventID
typedef string AchievementID

struct Achievement
{
	1: required AchievementID achievementId
	3: optional i32 eventCount
	4: optional string groupId
	5: optional AchievementID unlockAchievementId
	6: optional bool isDaily
	// Deprecated
	7: optional i32 dailyChestNum
	8: optional RankID rankMin
	9: optional RankID rankMax
	// We might not use title
	10: optional LocalizedString title
	11: required LocalizedString description
	12: optional AssetID iconImage
	13: optional list<CurrencyID> rewardCurrencies
	14: optional list<i32> rewardCurrencyCounts
	15: optional list<AchievementEventID> achievementEventIds
	16: optional i32 displayOrder
	17: optional string clientGroupId
	// Deprecated
//	21: optional i32 dailyAchievementPoints
	23: optional TutorialID goButtonTutorialId
}

typedef i32 PurchaseBonusNumPurchases

struct PurchaseBonus
{
	1: required PurchaseBonusNumPurchases purchaseBonusNumPurchases
	3: required InboxMessageID inboxMessageId
	// Deprecated - the rewards are in the gift message now
	4: optional list<CurrencyID> rewardCurrencyIds
	// Deprecated - the rewards are in the gift message now
	5: optional list<i32> rewardCurrencyCounts
}

typedef string PushNotificationID

struct PushNotification
{
	1: required PushNotificationID pushNotificationId
	2: required LocalizedString message
}

enum AndroidNotificationChannelImportance
{
	Zero = 0,
	Low = 2,
	High = 4,
	Default = 3
}

enum AndroidNotificationLockScreenVisibility
{
	Private,
	Public,
	Secret
}

struct AndroidNotificationChannel
{
	1: required string channelId
	2: required string name
	3: required LocalizedString description
	4: required AndroidNotificationChannelImportance importance
	5: required bool canBypassDnd
	6: required bool canShowBadge
	7: required bool enabled
	8: required bool enableLights
	9: required bool enableVibration
	10: required AndroidNotificationLockScreenVisibility lockScreenVisibility
	11: optional list<i64> vibrationPattern
}

struct IosNotificationThread
{
	1: required string threadId
}

enum IosNotificationPresentationOption
{
	Nothing = 0,
	Badge = 1,
	Sound = 2,
	Alert = 3,
}

enum IosNotificationAlertStyle
{
	NoAlert = 0,
	Alert,
	Banner,
}

struct LocalNotification
{
	1: required string localNotificationId
	2: required string androidChannelId
	3: required string iosThreadId
	4: required LocalizedString title
	5: required LocalizedString text
	6: required i32 cooldownSeconds
	7: required IosNotificationPresentationOption iosPresentationOption
	8: required bool iosShowInForeground
	9: optional string iosSubtitle
}

enum TrainingCampStateID
{
	Locked,
	Idle,
	Upgrading,
	Training
}

typedef i32 TrainingCampID

struct TrainingCamp
{
	1: required TrainingCampID trainingCampId
	2: optional i32 unlockRankId
	3: optional VipLevelID unlockVipLevelId
	4: required EvolutionProfileID evolutionProfileId
	5: optional string unlockGenericDialogId
	6: optional AssetID upgradeCellPrefab
	//	Note: you need to traverse Data.trainingMethodLinks to find all of the training methods for each training camp
}

typedef string TrainingMethodID

struct TrainingMethod
{
	1: required TrainingMethodID trainingMethodId
	2: required LocalizedString display
	3: required LocalizedString description
	// Deprecated - was required
	4: optional AssetID icon
	5: optional CurrencyID freeRushTokenCurrencyId
	6: optional AssetID cellPrefab
	// Removed by mutator
	7: optional AssetListID assetListId
	10: required i32 trainingDurationMinutes
	11: required i32 costRecruits
	12: optional CurrencyID costCurrencyId
	13: optional i32 costCurrencyCount
	14: optional list<CurrencyID> costResourceIds
	15: optional list<i32> costResourceCounts
	16: required i32 rushCostGems
	30: required list<RarityID> rarities
	31: required list<i32> rarityDistributions
	32: optional list<AffinityID> affinities
	33: optional string heroDisplayId
}

struct TrainingMethodLink
{
	1: required TrainingMethodID trainingMethodId
	2: required TrainingCampID trainingCampId
	3: required i32 unlockTrainingCampLevel
}

struct MinigameMusicTheme
{
	1: required string minigameMusicThemeId
	3: required string path
	// Deprecated
	10: optional i32 numLevels
//	11: optional list<i32> heroTurnLevels
//	12: optional list<i32> enemyTurnLevels
//	13: optional list<i32> energyShotLevels
//	14: optional list<i32> energyShotReturnLevels
}

typedef string BadgeID

struct Badge
{
	1: required BadgeID badgeId
}

struct RaidLeague
{
	1: required i32 raidLeagueId
	2: required LocalizedString display
	3: required i32 numTrophiesPromote
	4: required i32 numTrophiesDemote
	5: required CurrencyID raidCostCurrencyId
	6: required i32 raidCostCurrencyCount
	7: required CurrencyID rerollCostCurrencyId
	8: required i32 rerollCostCurrencyCount
	9: optional AssetID titleImagePath
	10: optional AssetID backgroundImagePath
}

struct DailyHintItem
{
	1: required LocalizedString text
}

enum AttackLaunchTypeID
{
	OnePerTurn = 0,
	OneAtATime = 1,
	OnePerHit = 2,
}

enum ProjectileParentID
{
	Hero = 0,
	Background,
	Target,
}

typedef string AttackID

enum RechargeTypeID
{
	NoLimit = 0,
	Turn,
	Energy,
	Time,
}

struct BeamAttack
{
	1: required AttackID attackId
	2: optional string projectileId
}

enum AttackParentID
{
	Hero = 0,
	Background,
	Target
}

struct Attack
{
	1: required AttackID attackId
	2: required AttackLaunchTypeID attackLaunchTypeId
	// Used by enemy logic. Actual attack duration can be longer or shorter
	3: optional double durationSeconds
	// Deprecated
//	4: optional double duration
	// Deprecated
//	4: optional i32 damage
	5: optional AssetID launchEffectPrefab
	6: optional SoundClipID launchSoundClipId
	// Deprecated
	7: optional LocalizedString description
	8: optional AssetID prefabPath
//	9: optional RechargeTypeID rechargeTypeId
	// Deprecated
//	10: optional bool matchAffinity
	// Deprecated
//	11: optional bool matchGender
	// Deprecated
//	12: optional bool oppositeGender
	13: optional bool isPositive
	14: optional AffinityMatchID affinityMatchId
	15: optional GenderMatchID genderMatchId
	16: optional AttackParentID attackParentId
	17: optional TargetTypeID targetTypeId
}

typedef string ProjectileID

enum LifespanTypeID
{
	Normal = 0,
	Immortal,
	HeroCollision,
	EnemyCollision,
	BoundaryCollision,
	AnyCollision,
	Fixed,
	Target,
}

enum TargetTypeID
{
	NoTarget = 0,
	FurthestEnemy,
	WeakestTeammate,
	NearestEnemy,
}

enum AimTypeID
{
	Shooter = 0,
	// Same as Shooter, but 0 degrees is toward target
	TargetRelative,
	Right,
	Up,
	Left,
	Down,
	Random,
	AtTarget,
	SmartLeftRight,
	Predictive,
	DumbLeftRight,
}

enum MotionTypeID
{
	Illegal = 0,
	WallBounce,
	Boomerang,
	Spiral,
	Rotate,
	CatmullRom,
	ActionMoveTo,
	Guided,
	Homing,
}

enum MotionEaseID
{
	Linear,
	EaseIn,
	EaseOut,
	EaseInOut,
	EaseExponentialIn,
	EaseExponentialOut,
	EaseExponentialInOut,
	EaseSineIn,
	EaseSineOut,
	EaseSineInOut,
	EaseQuadIn,
	EaseQuadOut,
	EaseQuadInOut,
	EaseCubicIn,
	EaseCubicOut,
	EaseCubicInOut,
	EaseQuartIn,
	EaseQuartOut,
	EaseQuartInOut,
	EaseQuintIn,
	EaseQuintOut,
	EaseQuintInOut,
	EaseCircularIn,
	EaseCircularOut,
	EaseCircularInOut,
	EaseElasticIn,
	EaseElasticOut,
	EaseElasticInOut,
	EaseBackIn,
	EaseBackOut,
	EaseBackInOut,
	EaseBounceIn,
	EaseBounceOut,
	EaseBounceInOut,
	EaseQuadraticIn,
	EaseQuadraticOut,
	EaseQuadraticInOut,
}


enum OrientationTypeID
{
	Default = 0,
	Up,
	Forward,
}

enum WallBehaviorID
{
	Pierce = 0,
	Bounce,
	Stop
}

struct Projectile
{
	1: required ProjectileID projectileId
	// deprecated
//	2: optional AssetID effectId
	3: required double speed
	// deprecated
//	4: optional AssetID collisionAudioPath
	5: optional double polarVelocityDps
	6: optional AssetID prefabPath
	8: optional LifespanTypeID lifespanTypeId
	// Deprecated - see targetFxListId
	//9: optional AssetID targetEffectPath
	// Deprecated - see collisionFxListId
	//10: optional AssetID collisionEffectPath
	11: optional string skillStatProfileId
	12: optional string projectileTrailId
	13: optional TargetTypeID targetTypeId
	14: optional AimTypeID aimTypeId
	15: optional MotionTypeID motionTypeId
	// Deprecated
	16: optional double lifespan
	17: optional double durationSeconds
	18: optional WallBehaviorID wallBehaviorId
	19: optional AssetID wallEffectPrefabPath
//	20: optional SoundClipID magicDamageAudioPath
//	21: optional SoundClipID wallCollisionAudioPath
	22: optional OrientationTypeID orientationTypeId
	23: optional ProjectileParentID projectileParentId
	24: optional string targetFxListId
	25: optional MotionEaseID motionEaseId
	26: optional SoundClipID damageSoundId
	27: optional SoundClipID collisionSoundId
	28: optional string collisionFxListId
	29: optional string bodyFxListId
	30: optional string launchSoundId
}

struct BeamProjectile
{
	1: required ProjectileID projectileId
	2: optional string skillStatProfileId
	3: optional AssetID prefabPath
	4: optional double durationSeconds
	5: optional AssetID sourceEffectPath
	6: optional AssetID beamEffectPath
	// Deprecated
	7: optional AssetID targetEffectPath
	8: optional AssetID audioPath_notused
	9: optional double beamEffectLength
	10: optional string enchantmentId
	11: optional TargetTypeID targetTypeId
	12: optional string targetFxListId
}

struct RadialProjectileAttack
{
	1: required AttackID attackId
	2: required double degreesIncrement
	3: required double delayIncrementSeconds
	4: required double delayRotationSeconds
	5: optional i32 numRotationsOld
	// Deprecated
	//6: optional AssetID projectilePrefab
	7: optional ProjectileID projectileId
	8: optional double startDegrees
	9: optional double numRotations
}

struct LaserAttack
{
	1: required AttackID attackId
	// Deprecated - use attack direction instead
	2: optional double degreesStart
	3: optional double degreesIncrement
	4: required double damageRepeatSeconds
	// Deprecated - just put it into the prefab
	5: optional double laserWidth
	// Deprecated
	//6: optional AssetID laserPrefab
	7: optional ProjectileID projectileId
	8: optional double degreesSweep
}

// TODO
//struct EnergyShot
//{
//	1: required string skillId
//	2: required string skillStatProfileId
//}

struct ShootAttack
{
	1: required AttackID attackId
	2: optional double degreesStart
	// Deprecated
	3: optional double degreesIncrement
	// Deprecated
	4: optional double damageRepeatSeconds

	7: optional string projectileId
	8: optional double distanceRepeat
	9: optional double timeRepeat
	10: optional i32 maxProjectiles
}

struct ProjectileTrail
{
	1: required string projectileTrailId
	2: required string projectileId
	3: optional double spawnDistance
}

struct ParticlesAttack
{
	1: required AttackID attackId
	// Deprecated in favor of effectsListId
	//2: optional AssetID particleSystemPrefab
	3: optional string skillStatProfileId
	4: optional double damageRepeatSeconds
	5: optional double radius
	6: optional string effectListId
}

struct AutoPurchaseListEntry
{
	1: required CurrencyID currencyId
	2: required PurchaseOfferID purchaseOfferId
}

struct AutoPurchaseList
{
	1: required CurrencyID currencyId
	2: required list<PurchaseOfferID> purchaseOfferIds
}

enum ConfigCleanerTypeID
{
	Auto,
	ServerFunction
}

struct ConfigCleaner
{
	1: required i32 configCleanerNum
	2: required ConfigCleanerTypeID configCleanerTypeId
	3: required string display
	4: required string description
}

struct AutoConfigCleaner
{
	1: required i32 configCleanerNum
	2: required list<string> tableNames
	3: required list<string> tableKeys
	// keys cannot appear in these tables
	4: required list<string> errorTableNames
}

struct SkillLevelUpCostEntry
{
	1: required i32 levelNum
	2: required i32 levelUpGoldCost
}

struct SkillSlotMinLevelEntry
{
	1: required i32 slotNum
	2: required i32 minLevel
}

struct SimulationTestEntry
{
	1: required string simulationTestId
	2: required i32 order
	3: required i32 numSamples
	9: optional i32 resultTeam1WinCount
	10: optional i32 team1Hp
	11: optional i32 team1Damage
	12: optional i32 team1Strength
	14: optional i32 team1PhysicalAttack
	15: optional i32 team1PhysicalDefense
	16: optional i32 team1Intelligence
	17: optional i32 team1MagicAttack
	18: optional i32 team1MagicDefense
	20: optional i32 team2Hp
	21: optional i32 team2Damage
	22: optional i32 team2Strength
	24: optional i32 team2PhysicalAttack
	25: optional i32 team2PhysicalDefense
	26: optional i32 team2Intelligence
	27: optional i32 team2MagicAttack
	28: optional i32 team3MagicDefense
}

struct SimulationTest
{
	1: required string simulationTestId
	2: optional list<SimulationTestEntry> simulationTestEntries
	3: optional bool autoRun
}

enum UserFieldID
{
    Safe = 0,
    All = 1,
	ConfigCleanerNum = 2,
	SocialBasicInfo = 3,
	AffinityId = 4,
	Language = 5,
	NumPurchases = 6,
	GemPassStates = 7,
	VipLevel = 8,
	ExternalAccountIds = 9,
	LinkedUserIds = 10,
	Rank = 11,
	TrainingCamps = 12,
	ChestAwardSequencePosition = 14,
	CurrentCampaignNumber = 15,
	CurrentCampaignLevelNumber = 16,
	CurrencyBalances = 17,
	CurrencyTimeBalanceLastModified = 18,
	ChestSlots = 20,
	ChestSlotUnlockStartTime = 21,
	ChestSlotState = 22,
	//Achievements = 23,
	AchievementStates = 24,
	HeroCardStates = 26,
	BadgeStates = 30,
	NumCardsBoughtToday = 32,
	TimeLastShopRefresh = 33,
	PurchaseOfferHistories = 34,
	RaidOpponentMatches = 35,
	RaidMatchHistories = 56,
	CrownChestState = 40,
	CrownChestProgress = 41,
	CrownChestLockStartTime = 42,
	AccumulateCrownChest = 43,
	DailyAchievementsChestState = 44,
    DailyAchievementsChestNum = 45,
	TimedChestState = 50,
	TimedChestUnlockStartTime = 51,
	TutorialFlags = 60,
	OpenedSecondChest = 61,
	ChoseStarterChest = 62,
	Decks = 70,
	SelectedDeckNum = 71,
	DefenseDeckNum = 72,
	RaidAttackDeckNum = 73,
	LastestChestRewardList = 80,
	LastGuildApplication = 81,
	InboxGiftMessages = 90,
	InboxGuildInvites = 92,
	InboxGuildApplications = 93,
	GuildChatMessages = 94,
	NewGuildChatMessages = 95,
}

struct RequestInfo
{
    1: required string requestUrl
    2: optional list<UserFieldID> safeUserFieldIds
    3: optional list<UserFieldID> dangerUserFieldIds
    // Deprecated
    4: optional bool suppressUserObject
    5: optional bool userInBody
    6: optional bool responseInBody
}

struct RequestInfoFieldEntry
{
    1: required string requestUrl
    2: required UserFieldID userFieldId
}

struct AssetList
{
	1: required string assetListId
	2: optional list<AssetID> assetIds
}

struct AssetListEntry
{
	1: required string assetListId
	2: required AssetID assetId
}

struct TipOfTheDay
{
	1: string tipOfTheDayId
	2: string eventId
	3: LocalizedString text
}

struct Data
{
	1: optional map<CampaignID,Campaign> campaigns
	2: optional map<LevelID,Level> levels
	3: optional map<LevelSceneID,LevelScene> levelScenes
	# Removed by mutator
	4: optional list<EnemySpawnPoint> enemySpawnPoints
	5: optional map<PurchaseBonusNumPurchases,PurchaseBonus> purchaseBonuses
	6: optional map<PurchaseOfferID, PurchaseOffer> purchaseOffers
	7: optional map<PurchaseOfferID, GemPass> gemPasses
	8: optional map<PurchaseOfferID, GemPack> gemPacks
	9: optional map<PurchaseOfferID, SubscriptionPurchaseOffer> subscriptionPurchaseOffers
	10: optional map<RankID, Rank> ranks
	// Deprecated
	11: optional list<CampaignID> campaignOrder
	12: optional map<HeroID,HeroBody> heroBodies
	13: optional map<RarityID, Rarity> rarities
	14: optional map<HeroStatisticID, HeroStatistic> heroStatistics
	15: optional map<PushNotificationID, PushNotification> pushNotifications
	16: optional list<ScheduledGiftMessage> scheduledGiftMessages
	17: optional list<HeroLevelXp> heroLevelXp
	18: optional map<string, StrengthProfile> strengthProfiles
	19: optional map<HeroID, HeroSoundProfile> heroSoundProfiles
	20: optional map<ColorID,Color> colors
	21: optional map<AchievementID, Achievement> quests
	22: optional map<AchievementEventID, AchievementEventID> achievementEventIdHints
	23: optional list<VipLevel> vipLevels
	24: optional map<GenericDialogTemplateID, GenericDialogTemplate> genericDialogTemplates
	25: optional map<GenericDialogID, GenericDialog> genericDialogs
	26: optional map<BadgeID, Badge> badges
	27: optional map<i32, RaidLeague> raidLeagues
	28: optional map<HeroStatID, HeroStat> heroStats
	30: optional map<AffinityID,Affinity> affinities
	31: optional map<string, ShopSection> shopSections
	32: optional map<string, EventSection> eventSections
	34: optional map<TrainingCampID, TrainingCamp> trainingCamps
	35: optional map<TrainingMethodID,TrainingMethod> trainingMethods
	36: optional list<TrainingMethodLink> trainingMethodLinks
	37: optional list<DailyHintItem> dailyHintItems
	38: optional map<string, PhysicsProfile> physicsProfiles
	39: optional map<string, AnimationProfile> animationProfiles
	// TODO: client
	40: optional map<SoundClipID,SoundClip> soundClips
	// TODO: client
	41: optional map<SoundClipListID,SoundClipList> soundClipLists
	42: optional map<string, MinigameMusicTheme> minigameMusicThemes
	43: optional list<CurrencyRankMaxEntry> currencyRankMaxEntries
	44: optional map<HeroSummonID, HeroSummon> heroSummons
	// Deprecated
	45: optional i32 currentConfigCleanerNum
	46: optional map<i32, ConfigCleaner> configCleaners
	47: optional map<i32, AutoConfigCleaner> autoConfigCleaners
	48: optional map<CurrencyTargetID, CurrencyTarget> currencyTargets
	49: optional map<PurchaseOfferID, CashPurchaseInfo> cashPurchaseInfos

	50: optional map<ChestID,Chest> chests
	# removed by mutator
	51: optional list<GuaranteedHero> guaranteedHeroes
	# Deprecated - was required
	52: optional list<ChestID> chestSequence
	53: optional map<GenderID, Gender> genders
	# removed by mutator
	54: optional list<GuaranteedCurrency> guaranteedCurrencies
	// TODO: client
	56: optional map<TutorialID, Tutorial> tutorials
	# removed by mutator
	57: optional map<TutorialStepID, TutorialStep> tutorialSteps
	// Removed by mutator
    59: optional list<AssetListEntry> assetListEntries
    // Populated by mutator
    60: optional map<string, AssetList> assetLists
	62: optional map<CurrencyID, Currency> currencies
	63: optional map<CurrencyID, CurrencyRecharge> currencyRecharges
	64: optional map<AttackID, Attack> attacks
	65: optional map<AttackID, RadialProjectileAttack> radialProjectileAttacks
	66: optional map<AttackID, LaserAttack> laserAttacks
	67: optional map<AttackID, ShootAttack> shootAttacks
	68: optional map<AttackID, ParticlesAttack> particlesAttacks
	69: optional map<AttackID, BeamAttack> beamAttacks

	# removed by mutator
	70: optional map<RuntimePlatformID, RuntimePlatform> runtimePlatforms
	# removed by mutator
	71: optional list<AutoPurchaseListEntry> autoPurchaseListEntries
	# populated by mutator
	72: optional map<CurrencyID, AutoPurchaseList> autoPurchaseLists
	73: optional map<ProjectileID, Projectile> projectiles
	// Removed by mutator
	74: optional list<SkillLevelUpCostEntry> skillLevelUpCostEntries
	// Populated by mutator
	75: optional list<i32> skillLevelUpGoldCosts
	// Removed by mutator
	76: optional list<SkillSlotMinLevelEntry> skillSlotMinLevelEntries
	// Populated by mutator
	77: optional list<i32> skillSlotMinimumLevels
	78: optional map<string, SkillStatProfile> skillStatProfiles
	79: optional map<string, Skill> skills
	80: optional map<string, ProjectileTrail> projectileTrails
	81: optional map<string, BeamProjectile> beamProjectiles
	82: optional map<string, EdgeElement> edgeElements
	83: optional list<SkillStatProfileEntry> skillStatProfileEntries

    // Populated by mutator
	85: optional map<string, RequestInfo> requestInfo
	// Removed by mutator
	86: optional list<RequestInfoFieldEntry> safeFieldEntries
	// Removed by mutator
	87: optional list<RequestInfoFieldEntry> dangerFieldEntries
	// Removed by mutator
	88: optional list<EdgeElementEntry> edgeElementEntries
	// Populated by mutator
	89: optional map<string, EdgeElementsProfile> edgeElementsProfiles

	90: optional map<string, SimulationTest> simulationTests
	91: optional list<SimulationTestEntry> simulationTestEntries

	93: optional map<OfferPackShopItemTemplateID, OfferPackShopItemTemplate> offerPackShopItemTemplates
	94: optional map<OfferPackShopItemID, OfferPackShopItem> offerPackShopItems
	95: optional map<OfferPackZoomItemTemplateID, OfferPackZoomItemTemplate> offerPackZoomItemTemplates
	96: optional map<OfferPackZoomItemID, OfferPackZoomItem> offerPackZoomItems
	98: optional map<string, VisualEffectsProfile> visualEffectsProfiles

	100: optional map<string, HeroSkillIcon> heroSkillIcons
	101: optional map<string, Prefab> prefabs

//	110: optional NewUserState newUserState
	111: optional Settings settings
	120: optional map<EventID, Event> events
	121: optional map<string, EffectList> effectLists
	// Removed by mutator
	122: optional list<EffectListEntry> effectListEntries
	123: optional map<string, HudProfile> hudProfiles
	124: optional map<string, TipOfTheDay> tipOfTheDays
	125: optional map<string, AndroidNotificationChannel> androidNotificationChannels
	126: optional map<string, IosNotificationThread> iosNotificationThreads
	127: optional map<string, LocalNotification> localNotifications

	130: optional map<LocationID, Location> locations
	131: optional map<string, EventActivity> eventActivities

	140: optional map<SectionHeadingTemplateID, SectionHeadingTemplate> sectionHeadingTemplates
	141: optional map<SectionHeadingID, SectionHeading> sectionHeadings
	142: optional map<SectionTopperTemplateID, SectionTopperTemplate> sectionTopperTemplates
	143: optional map<SectionTopperID, SectionTopper> sectionToppers
	144: optional map<SectionBottomTemplateID, SectionBottomTemplate> sectionBottomTemplates
	145: optional map<SectionBottomID, SectionBottom> sectionBottoms
	146: optional map<InboxSectionID, InboxSection> inboxSections
	// Guild list sections use the same structure as inbox sections
	147: optional map<GuildListSectionID, GuildListSection> guildListSections
	148: optional map<GuildListItemTemplateID, GuildListItemTemplate> guildListItemTemplates
	149: optional map<GuildListItemID, GuildListItem> guildListItems

	150: optional map<GuildMemberListItemTemplateID, GuildMemberListItemTemplate> guildMemberListItemTemplates
	151: optional map<GuildMemberListItemID, GuildMemberListItem> guildMemberListItems
	152: optional map<GuildMemberListSectionID, GuildMemberListSection> guildMemberListSections

	// Guild section item templates
	153: optional map<GuildSectionItemTemplateID,GuildSectionItemTemplate> guildSectionItemTemplates
	154: optional map<GuildSectionItemID,GuildSectionItem> guildSectionItems

	// Simple popup template
	155: optional map<SimplePopupID,SimplePopup> simplePopups
	156: optional map<SimplePopupTemplateID,SimplePopupTemplate> simplePopupTemplates

	// Removed by mutator
	160: optional list<GiftMessageCurrencyItem> giftMessageCurrencyItems
	161: optional map<GiftMessageTemplateID, GiftMessageTemplate> giftMessageTemplates
	162: optional map<GiftMessageID, GiftMessage> giftMessages
	163: optional map<GiftMessagePopupTempateID, GiftMessagePopupTempate> giftMessagePopupTempates
	164: optional map<GiftMessagePopupID, GiftMessagePopup> giftMessagePopups
	165: optional list<SettingKeyValue> GuildSettingssKeyValue

	170: optional map<EnchantmentID, Enchantment> enchantments
	171: optional map<GearItemID, GearItem> gearItems
	172: optional map<EvolutionProfileID, EvolutionProfile> evolutionProfiles
	// Removed by mutator
	// Deprecated
	173: optional map<EvolutionLevelProfileID, EvolutionLevelProfile> evolutionLevelProfiles_
	// Removed by mutator
	174: optional list<EvolutionProfileLevelLink> evolutionProfileLevelLinks
	175: optional map<string, PassiveSkill> passiveSkills
	// Deprecated
//	176: optional map<string, Ability> abilities
	177: optional map<string, StatBumper> statBumpers

	180: optional map<UserIconID, UserIcon> userIcons
	181: optional map<UserFrameID, UserFrame> userFrames
	182: optional map<string, string> stringTable
	183: optional map<string, bool> boolTable

	190: optional map<ChatMessageTemplateID, ChatMessageTemplate> chatMessageTemplates
	191: optional map<ChatMessageID, ChatMessage> chatMessages

	200: optional map<ServerErrorDialogTemplateID, ServerErrorDialogTemplate> serverErrorDialogTemplates
	201: optional map<ServerErrorMessageID, ServerErrorMessage> serverErrorMessages
	202: optional map<MenuID, Menu> menus
	1000: optional GuildSettings guildSettings

	1010: optional map<GuildMemberTypeID, GuildMemberType> guildMemberTypes
	1012: optional map<GuildJoinTypeID, GuildJoinType> guildJoinTypes
	1020: optional map<GuildEmblemID, GuildEmblem> guildEmblems
	1021: optional map<GuildFrameID, GuildFrame> guildFrames
	1022: optional list<string> guildNameSuggestFirst
	1023: optional list<string> guildNameSuggestSecond
	1024: optional map<LeagueID, League> leagues
	1030: optional list<string> userNameSuggestFirst
	1031: optional list<string> userNameSuggestSecond
	1032: optional Text text
}
