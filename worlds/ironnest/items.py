from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import IronNestWorld

ITEM_NAME_TO_ID = {
    "Right Gun Unlock": 1,
    "Requisition Table Unlock": 2,
    "Mission 1 Briefing": 3,
    "Mission 2 Briefing": 4,
    "Requisition Card Pack 1": 91,
    "Requisition Card Pack 2": 92,
    "Requisition Card Pack 3": 93,
    "+5 Requisition": 90003,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Right Gun Unlock": ItemClassification.progression,
    "Requisition Table Unlock": ItemClassification.progression,
    "Mission 1 Briefing": ItemClassification.progression,
    "Mission 2 Briefing": ItemClassification.progression,
    "Requisition Card Pack 1": ItemClassification.progression | ItemClassification.useful,
    "Requisition Card Pack 2": ItemClassification.progression | ItemClassification.useful,
    "Requisition Card Pack 3": ItemClassification.progression | ItemClassification.useful,
    "+5 Requisition": ItemClassification.filler,
}

class IronNestItem(Item):
    game = "IRON NEST: Heavy Turret Simulator"

def get_random_filler_item_name(world:  IronNestWorld) -> str:
    return "+5 Requisition"


def create_item_with_correct_classification(world:  IronNestWorld, name: str) -> IronNestItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return IronNestItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: IronNestWorld) -> None:

    itempool: list[Item] = [
        world.create_item("Right Gun Unlock"),
        world.create_item("Requisition Table Unlock"),
        world.create_item("Mission 1 Briefing"),
        world.create_item("Mission 2 Briefing"),
        world.create_item("Requisition Card Pack 1"),
        world.create_item("Requisition Card Pack 2"),
        world.create_item("Requisition Card Pack 3"),
    ]

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool
