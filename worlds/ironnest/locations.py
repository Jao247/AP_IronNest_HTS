from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import IronNestWorld

LOCATION_NAME_TO_ID = {
    "Mission 1": 1,
    "Mission 1 - Medal 1 - Bronze": 2,
    "Mission 1 - Medal 2 - Bronze": 3,
    "Mission 1 - Medal 3 - Bronze": 4,
    "Mission 1 - Medal 4 - Bronze": 5,
    "Mission 1 - Medal 1 - Silver": 6,
    "Mission 1 - Medal 2 - Silver": 7,
    "Mission 1 - Medal 3 - Silver": 8,
    "Mission 1 - Medal 4 - Silver": 9,
    "Mission 1 - Medal 1 - Gold": 10,
    "Mission 1 - Medal 2 - Gold": 11,
    "Mission 1 - Medal 3 - Gold": 12,
    "Mission 1 - Medal 4 - Gold": 13,
    "Mission 2": 21,
    "Mission 2 - Medal 1 - Bronze": 22,
    "Mission 2 - Medal 2 - Bronze": 23,
    "Mission 2 - Medal 3 - Bronze": 24,
    "Mission 2 - Medal 4 - Bronze": 25,
    "Mission 2 - Medal 1 - Silver": 26,
    "Mission 2 - Medal 2 - Silver": 27,
    "Mission 2 - Medal 3 - Silver": 28,
    "Mission 2 - Medal 4 - Silver": 29,
    "Mission 2 - Medal 1 - Gold": 30,
    "Mission 2 - Medal 2 - Gold": 31,
    "Mission 2 - Medal 3 - Gold": 32,
    "Mission 2 - Medal 4 - Gold": 33,
}

class IronNestLocation(Location):
    game = "IRON NEST: Heavy Turret Simulator"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: IronNestWorld) -> None:
    create_regular_locations(world)
    #create_events(world)


def create_regular_locations(world: IronNestWorld) -> None:
    iron_nest_map = world.get_region("IronNest Map")
    mission_1 = world.get_region("Mission 1")
    mission_2 = world.get_region("Mission 2")

    iron_nest_map_locations = get_location_names_with_ids(
        ["Mission 1", "Mission 2"]
    )
    iron_nest_map.add_locations(iron_nest_map_locations, IronNestLocation)

    mission_1_locations = get_location_names_with_ids([
        "Mission 1 - Medal 1 - Bronze",
        "Mission 1 - Medal 2 - Bronze",
        "Mission 1 - Medal 3 - Bronze",
        "Mission 1 - Medal 4 - Bronze",
        "Mission 1 - Medal 1 - Silver",
        "Mission 1 - Medal 2 - Silver",
        "Mission 1 - Medal 3 - Silver",
        "Mission 1 - Medal 4 - Silver",
        "Mission 1 - Medal 1 - Gold",
        "Mission 1 - Medal 2 - Gold",
        "Mission 1 - Medal 3 - Gold",
        "Mission 1 - Medal 4 - Gold",
    ])
    mission_1.add_locations(mission_1_locations, IronNestLocation)

    mission_2_locations = get_location_names_with_ids([
        "Mission 2 - Medal 1 - Bronze",
        "Mission 2 - Medal 2 - Bronze",
        "Mission 2 - Medal 3 - Bronze",
        "Mission 2 - Medal 4 - Bronze",
        "Mission 2 - Medal 1 - Silver",
        "Mission 2 - Medal 2 - Silver",
        "Mission 2 - Medal 3 - Silver",
        "Mission 2 - Medal 4 - Silver",
        "Mission 2 - Medal 1 - Gold",
        "Mission 2 - Medal 2 - Gold",
        "Mission 2 - Medal 3 - Gold",
        "Mission 2 - Medal 4 - Gold",
    ])
    mission_2.add_locations(mission_2_locations, IronNestLocation)


#def create_events(world: IronNestWorld) -> None:
