from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import IronNestWorld



def create_and_connect_regions(world: IronNestWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: IronNestWorld) -> None:
    mission_1 = Region("Mission 1", world.player, world.multiworld)

    regions = [mission_1]

    world.multiworld.regions += regions


def connect_regions(world: IronNestWorld) -> None:
    mission_1 = world.get_region("Mission 1")

