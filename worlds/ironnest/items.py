from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import IronNestWorld

ITEM_NAME_TO_ID = {
    "Right Gun Unlock": 1,
    "Requisition Table Unlock": 2,
    "Mission 1 Briefing": 3,
    "Requisition Card Pack 1": 4,
    "Requisition Card Pack 2": 5,
    "Requisition Card Pack 3": 6,
    "Requisition Card Pack 4": 7,
    "Discount HE Requisition": 8,
    "Discount AP Requisition": 9,
    "Discount Air Reconnaissance Requisition": 10,
    "+5 Bonus Requisition": 11,
    "+10 Bonus Requisition": 12,
    "+25 Bonus Requisition": 13,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Right Gun Unlock": ItemClassification.progression,
    "Requisition Table Unlock": ItemClassification.progression,
    "Mission 1 Briefing": ItemClassification.progression,
    "Requisition Card Pack 1": ItemClassification.progression | ItemClassification.useful,
    "Requisition Card Pack 2": ItemClassification.progression | ItemClassification.useful,
    "Requisition Card Pack 3": ItemClassification.progression | ItemClassification.useful,
    "Requisition Card Pack 4": ItemClassification.progression | ItemClassification.useful,
    "Discount HE Requisition": ItemClassification.useful,
    "Discount AP Requisition": ItemClassification.useful,
    "Discount Air Reconnaissance Requisition": ItemClassification.useful,
    "+5 Bonus Requisition": ItemClassification.filler,
    "+10 Bonus Requisition": ItemClassification.filler,
    "+25 Bonus Requisition": ItemClassification.filler,
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
        world.create_item("Requisition Card Pack 1"),
        world.create_item("Requisition Card Pack 1"),
        world.create_item("Requisition Card Pack 1"),
        world.create_item("Requisition Card Pack 1"),
        world.create_item("Discount HE Requisition"),
        world.create_item("Discount AP Requisition"),
        world.create_item("Discount Air Reconnaissance Requisition"),
        world.create_item("+5 Bonus Requisition"),
        world.create_item("+10 Bonus Requisition"),
        world.create_item("+25 Bonus Requisition"),
    ]

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool
