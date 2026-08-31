from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region
from rule_builder.rules import HasAll

if TYPE_CHECKING:
    from .world import IronNestWorld



def create_and_connect_regions(world: IronNestWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: IronNestWorld) -> None:
    iron_nest_map = Region("IronNest Map", world.player, world.multiworld)
    mission_1 = Region("Mission 1", world.player, world.multiworld)
    mission_2 = Region("Mission 2", world.player, world.multiworld)

    regions = [iron_nest_map, mission_1, mission_2]

    world.multiworld.regions += regions


def connect_regions(world: IronNestWorld) -> None:
    iron_nest_map = world.get_region("IronNest Map")
    mission_1 = world.get_region("Mission 1")
    mission_2 = world.get_region("Mission 2")

    iron_nest_map.connect(mission_1, "Mission 1", HasAll("Mission 1 Briefing"))
    iron_nest_map.connect(mission_2, "Mission 2", HasAll("Mission 2 Briefing"))

