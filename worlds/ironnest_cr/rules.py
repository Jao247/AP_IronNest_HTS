from __future__ import annotations

from typing import TYPE_CHECKING
from Options import OptionError
from .options import IronNestCRGoal
from rule_builder.rules import Has, HasAll, HasAny, CanReachLocation, Or, And

if TYPE_CHECKING:
    from .world import IronNestCRWorld

HAS_M1_BRIEFING = Has("Mission 1 Briefing")
HAS_M2_BRIEFING = Has("Mission 2 Briefing")
HAS_M3_BRIEFING = Has("Mission 3 Briefing")
HAS_M4_BRIEFING = Has("Mission 4 Briefing")
HAS_M5_BRIEFING = Has("Mission 5 Briefing")
HAS_M6_BRIEFING = Has("Mission 6 Briefing")
HAS_M7_BRIEFING = Has("Mission 7 Briefing")
HAS_M8_BRIEFING = Has("Mission 8 Briefing")
HAS_M9_BRIEFING = Has("Mission 9 Briefing")
HAS_M10_BRIEFING = Has("Mission 10 Briefing")
HAS_M11_BRIEFING = Has("Mission 11 Briefing")
HAS_M12_BRIEFING = Has("Mission 12 Briefing")
HAS_M13_BRIEFING = Has("Mission 13 Briefing")
HAS_M14_BRIEFING = Has("Mission 14 Briefing")
HAS_M15_BRIEFING = Has("Mission 15 Briefing")

def set_all_rules(world: IronNestCRWorld) -> None:

    set_all_entrance_rules(world)
    #set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: IronNestCRWorld) -> None:
    access_to_mission_1 = world.get_entrance("Access to Mission 1")
    access_to_mission_2 = world.get_entrance("Access to Mission 2")
    access_to_mission_3 = world.get_entrance("Access to Mission 3")
    access_to_mission_4 = world.get_entrance("Access to Mission 4")
    access_to_mission_5 = world.get_entrance("Access to Mission 5")
    access_to_mission_6 = world.get_entrance("Access to Mission 6")
    access_to_mission_7 = world.get_entrance("Access to Mission 7")
    access_to_mission_8 = world.get_entrance("Access to Mission 8")
    access_to_mission_9 = world.get_entrance("Access to Mission 9")
    access_to_mission_10 = world.get_entrance("Access to Mission 10")
    access_to_mission_11 = world.get_entrance("Access to Mission 11")
    access_to_mission_12 = world.get_entrance("Access to Mission 12")
    access_to_mission_13 = world.get_entrance("Access to Mission 13")
    access_to_mission_14 = world.get_entrance("Access to Mission 14")
    access_to_mission_15 = world.get_entrance("Access to Mission 15")

    # Provided full cargo of powder charges and enough Ammo
    world.set_rule(access_to_mission_1, HAS_M1_BRIEFING)
    world.set_rule(access_to_mission_2, HAS_M2_BRIEFING)

    can_buy_powder_charges = Has("Punchcard - Powder Charges")
    can_damage_enemies = HasAny("Punchcard - LE Shell", "Punchcard - HE Shell", "Punchcard - DRIL Shell",
                                "Explosive Munitions Card Pack")
    world.set_rule(access_to_mission_3, And(HAS_M3_BRIEFING,
                                                HasAny("Punchcard - AP Shell", "Punchcard - APHE Shell",
                                                       "AP Munitions Card Pack"), can_buy_powder_charges, can_damage_enemies))
    world.set_rule(access_to_mission_4, And(HAS_M4_BRIEFING, can_buy_powder_charges, can_damage_enemies))
    world.set_rule(access_to_mission_5, And(HAS_M5_BRIEFING, can_buy_powder_charges, can_damage_enemies))
    world.set_rule(access_to_mission_6, And(HAS_M6_BRIEFING,
                                                HasAny("Punchcard - SMK Shell", "Utility Munitions Card Pack",),
                                            can_buy_powder_charges, can_damage_enemies))
    world.set_rule(access_to_mission_7, And(HAS_M7_BRIEFING, can_buy_powder_charges, can_damage_enemies))
    world.set_rule(access_to_mission_8, And(HAS_M8_BRIEFING, can_buy_powder_charges, can_damage_enemies))
    world.set_rule(access_to_mission_9, And(HAS_M9_BRIEFING,
                                                HasAny("Punchcard - TEAR Shell", "Chemical Munitions Card Pack",)))
    world.set_rule(access_to_mission_10, And(HAS_M10_BRIEFING, can_buy_powder_charges, can_damage_enemies))
    world.set_rule(access_to_mission_11, And(HAS_M11_BRIEFING, can_buy_powder_charges, can_damage_enemies))
    world.set_rule(access_to_mission_12, And(HAS_M12_BRIEFING, can_buy_powder_charges, can_damage_enemies))
    world.set_rule(access_to_mission_13, And(HAS_M13_BRIEFING,
                                             HasAll("Punchcard - Emergency Move", "Punchcard - AP Shell"),
                                             can_buy_powder_charges, can_damage_enemies))
    world.set_rule(access_to_mission_14, And(HAS_M14_BRIEFING, can_buy_powder_charges, can_damage_enemies))
    world.set_rule(access_to_mission_15, And(HAS_M15_BRIEFING, can_buy_powder_charges, can_damage_enemies))

#def set_all_location_rules(world: IronNestWorld) -> None:


def set_completion_condition(world: IronNestCRWorld) -> None:
    if world.options.iron_nest_cr_goal == IronNestCRGoal.option_medal_1:
        world.set_completion_rule(And(CanReachLocation("Mission 15: White Shells - Ending 1"),
                                      HasAny("Punchcard - PRPG Shell", "Punchcard - SMK Shell",
                                             "Punchcard - STAR Shell", "Utility Munitions Card Pack")))
    elif world.options.iron_nest_cr_goal == IronNestCRGoal.option_medal_2:
        world.set_completion_rule(And(CanReachLocation("Mission 15: White Shells - Ending 2"),
                                      HasAny("Punchcard - TEAR Shell", "Punchcard - PHGN Shell",
                                             "Punchcard - CYAN Shell", "Punchcard - FLCH Shell", "Punchcard - WP Shell",
                                             "Chemical Munitions Card Pack",)))
    elif world.options.iron_nest_cr_goal == IronNestCRGoal.option_medal_3:
        world.set_completion_rule(And(CanReachLocation("Mission 15: White Shells - Ending 3"),
                                      Or(HasAll("Punchcard - SMK Shell", "Punchcard - EQKE Shell", ),
                                         HasAll("Explosive Munitions Card Pack",))))
    elif world.options.iron_nest_cr_goal == IronNestCRGoal.option_medal_4:
        world.set_completion_rule(And(CanReachLocation("Mission 15: White Shells - Ending 4"),
                                      HasAny("Punchcard - AP Shell", "Punchcard - APHE Shell",
                                             "Punchcard - ATMC Shell", "Punchcard - CLMN Shell", "Punchcard - DRIL Shell",
                                             "Punchcard - EQKE Shell", "Punchcard - HCHE Shell", "Punchcard - HE Shell",
                                             "Punchcard - INCN Shell", "Punchcard - LE Shell", "Punchcard - PLCM Shell",
                                             "Punchcard - THRM Shell", "AP Munitions Card Pack", "Explosive Munitions Card Pack",
                                             "Utility Munitions Card Pack", "Cluster Munitions Card Pack", "Incendiary Munitions Card Pack",)))
    elif world.options.iron_nest_cr_goal == IronNestCRGoal.option_phantom_battery:
        world.set_completion_rule(And(CanReachLocation("Mission 13: Phantom Battery - Completion"),
                                      HasAll("Punchcard - Emergency Move", "Punchcard - AP Shell",
                                             "Punchcard - Location Report", "Punchcard - Powder Charges")))
    else:
        raise OptionError(f"Unknown option: {world.options.iron_nest_cr_goal}")