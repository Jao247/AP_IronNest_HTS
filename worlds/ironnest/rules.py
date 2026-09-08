from __future__ import annotations

from typing import TYPE_CHECKING
from Options import OptionError
from .options import IronNestGoal
from rule_builder.rules import Has, HasAll, Rule, CanReachLocation, Or

if TYPE_CHECKING:
    from .world import IronNestWorld

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

def set_all_rules(world: IronNestWorld) -> None:

    #set_all_entrance_rules(world)
    #set_all_location_rules(world)
    set_completion_condition(world)


#def set_all_entrance_rules(world: IronNestWorld) -> None:
    #access_to_mission_1 = world.get_entrance("Mission 1")

#def set_all_location_rules(world: IronNestWorld) -> None:


def set_completion_condition(world: IronNestWorld) -> None:
    if world.options.iron_nest_goal == IronNestGoal.option_medal_1:
        world.set_completion_rule(CanReachLocation("Mission 15: White Shells - Ending 1"))
    elif world.options.iron_nest_goal == IronNestGoal.option_medal_2:
        world.set_completion_rule(CanReachLocation("Mission 15: White Shells - Ending 2"))
    elif world.options.iron_nest_goal == IronNestGoal.option_medal_3:
        world.set_completion_rule(CanReachLocation("Mission 15: White Shells - Ending 3"))
    elif world.options.iron_nest_goal == IronNestGoal.option_medal_4:
        world.set_completion_rule(CanReachLocation("Mission 15: White Shells - Ending 4"))
    elif world.options.iron_nest_goal == IronNestGoal.option_phantom_battery:
        world.set_completion_rule(CanReachLocation("Mission 13: Phantom Battery - Completion"))
    else:
        raise OptionError(f"Unknown option: {world.options.iron_nest_goal}")