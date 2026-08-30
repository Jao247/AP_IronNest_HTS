from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import IronNestWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
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
}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class IronNestLocation(Location):
    game = "IRON NEST: Heavy Turret Simulator"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: IronNestWorld) -> None:
    create_regular_locations(world)
    #create_events(world)


def create_regular_locations(world: IronNestWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    mission_1 = world.get_region("Mission 1")


#def create_events(world: IronNestWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
