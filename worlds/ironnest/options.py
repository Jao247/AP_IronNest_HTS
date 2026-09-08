from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle


class ShuffleRightLoader(Toggle):
    """
    Toggle whether to include Right Loader in the item pool.
    """
    display_name = "Shuffle Right Loader"

class ShuffleMedals(Toggle):
    """
    Shuffle the medals into the item pool.
    """
    display_name = "Shuffle Medals"

class CardPacks (Toggle):
    """
    Organise Requisition cards into card packs.

    Converts 27 Cards into 5 Card Packs.
    """
    display_name = "Card Packs"

class Mission15Requirements(Choice):
    """
    Extra unlock requirements for Mission 15.

    Vanilla: Mission 15 Briefing only.
    Medals: Gold Medals earned from any mission.
    Missions: Successful missions required.
    Phantom Battery: Must attain and complete Mission 13
    """
    option_vanilla = 0
    option_medals = 1
    option_missions = 2
    option_phantom_battery = 3

    display_name = "Mission 15 Requirements"

class MedalsToUnlockGoal(Range):
    """
    How many Gold Medals need to be earned in addition to Mission 15 Briefing.
    """
    display_name = "Medals to Unlock Goal"
    range_start = 4
    range_end = 48
    default = 12

class MissionsToUnlockGoal(Range):
    """
    How many missions are required in addition to Mission 15 Briefing.

    This does not include Tutorial Missions.
    """
    display_name = "Mission to Unlock Goal"
    range_start = 3
    range_end = 12
    default = 5

class IronNestGoal(Choice):
    """
    What Goal do you want to achieve?
    """
    display_name = "Goal"
    option_medal_1 = 1
    option_medal_2 = 2
    option_medal_3 = 3
    option_medal_4 = 4
    option_phantom_battery = 5
    default = option_medal_1

class IronNestTraps(Toggle):
    """
    Enable Traps
    """
    display_name = "Traps"
    default = False


@dataclass
class IronNestOptions(PerGameCommonOptions):
    shuffle_right_loader: ShuffleRightLoader
    card_packs: CardPacks
    shuffle_medals: ShuffleMedals
    mission_15_requirements: Mission15Requirements
    medals_to_unlock_goal: MedalsToUnlockGoal
    missions_to_unlock_goal: MissionsToUnlockGoal
    iron_nest_goal: IronNestGoal
    iron_nest_traps: IronNestTraps

#option_groups = [
#    OptionGroup(
#        "Gameplay Options",
#        [ShuffleRightLoader, CardPacks, RandomiseMedalsAwarded],
#    ),
#    OptionGroup(
#        "Goal Options",
#        [Goal, Mission15Requirements, MedalsToUnlockGoal, MissionsToUnlockGoal],
#    )
#]

option_presets = {
    "default": {
        "shuffle_right_loader": False,
        "card_packs": False,
        "shuffle_medals": False,
        "iron_nest_goal": IronNestGoal.option_medal_1,
        "mission_15_requirements": Mission15Requirements.option_vanilla,
        "medals_to_unlock_goal": MedalsToUnlockGoal.default,
        "missions_to_unlock_goal": MissionsToUnlockGoal.default,
        "iron_nest_traps": False,
    },
}
