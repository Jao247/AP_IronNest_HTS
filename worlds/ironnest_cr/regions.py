from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region
from rule_builder.rules import HasAll

if TYPE_CHECKING:
    from .world import IronNestCRWorld



def create_and_connect_regions(world: IronNestCRWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: IronNestCRWorld) -> None:
    mission_selection_map = Region("IronNest Map", world.player, world.multiworld)
    mission_1 = Region("Mission 1", world.player, world.multiworld)
    mission_2 = Region("Mission 2", world.player, world.multiworld)
    mission_3 = Region("Mission 3", world.player, world.multiworld)
    mission_4 = Region("Mission 4", world.player, world.multiworld)
    mission_5 = Region("Mission 5", world.player, world.multiworld)
    mission_6 = Region("Mission 6", world.player, world.multiworld)
    mission_7 = Region("Mission 7", world.player, world.multiworld)
    mission_8 = Region("Mission 8", world.player, world.multiworld)
    mission_9 = Region("Mission 9", world.player, world.multiworld)
    mission_10 = Region("Mission 10", world.player, world.multiworld)
    mission_11 = Region("Mission 11", world.player, world.multiworld)
    mission_12 = Region("Mission 12", world.player, world.multiworld)
    mission_13 = Region("Mission 13", world.player, world.multiworld)
    mission_14 = Region("Mission 14", world.player, world.multiworld)
    mission_15 = Region("Mission 15", world.player, world.multiworld)

    regions = [mission_selection_map, mission_1, mission_2, mission_3, mission_4, mission_5, mission_6, mission_7,
               mission_8, mission_9, mission_10, mission_11, mission_12, mission_13, mission_14, mission_15]

    world.multiworld.regions += regions


def connect_regions(world: IronNestCRWorld) -> None:
    mission_selection_map = world.get_region("IronNest Map")
    mission_1 = world.get_region("Mission 1")
    mission_2 = world.get_region("Mission 2")
    mission_3 = world.get_region("Mission 3")
    mission_4 = world.get_region("Mission 4")
    mission_5 = world.get_region("Mission 5")
    mission_6 = world.get_region("Mission 6")
    mission_7 = world.get_region("Mission 7")
    mission_8 = world.get_region("Mission 8")
    mission_9 = world.get_region("Mission 9")
    mission_10 = world.get_region("Mission 10")
    mission_11 = world.get_region("Mission 11")
    mission_12 = world.get_region("Mission 12")
    mission_13 = world.get_region("Mission 13")
    mission_14 = world.get_region("Mission 14")
    mission_15 = world.get_region("Mission 15")

    mission_selection_map.connect(mission_1, "Access to Mission 1", HasAll("Mission 1 Briefing"))
    mission_selection_map.connect(mission_2, "Access to Mission 2", HasAll("Mission 2 Briefing"))
    mission_selection_map.connect(mission_3, "Access to Mission 3", HasAll("Mission 3 Briefing"))
    mission_selection_map.connect(mission_4, "Access to Mission 4", HasAll("Mission 4 Briefing"))
    mission_selection_map.connect(mission_5, "Access to Mission 5", HasAll("Mission 5 Briefing"))
    mission_selection_map.connect(mission_6, "Access to Mission 6", HasAll("Mission 6 Briefing"))
    mission_selection_map.connect(mission_7, "Access to Mission 7", HasAll("Mission 7 Briefing"))
    mission_selection_map.connect(mission_8, "Access to Mission 8", HasAll("Mission 8 Briefing"))
    mission_selection_map.connect(mission_9, "Access to Mission 9", HasAll("Mission 9 Briefing"))
    mission_selection_map.connect(mission_10, "Access to Mission 10", HasAll("Mission 10 Briefing"))
    mission_selection_map.connect(mission_11, "Access to Mission 11", HasAll("Mission 11 Briefing"))
    mission_selection_map.connect(mission_12, "Access to Mission 12", HasAll("Mission 12 Briefing"))
    mission_selection_map.connect(mission_13, "Access to Mission 13", HasAll("Mission 13 Briefing"))
    mission_selection_map.connect(mission_14, "Access to Mission 14", HasAll("Mission 14 Briefing"))
    mission_selection_map.connect(mission_15, "Access to Mission 15", HasAll("Mission 15 Briefing"))
