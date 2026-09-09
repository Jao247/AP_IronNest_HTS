from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from .options import IronNestCRGoal, IronNestCRTraps

if TYPE_CHECKING:
    from .world import IronNestCRWorld

# Progressive Munitions?
# Progressive Explosive Munition - LE > HE > HCHE > ATMC
# Progressive Armor Piercing - AP > APHE > EQKE
# Progressive


ITEM_NAME_TO_ID = {
    #"Right Gun Unlock": 1,
    #"Requisition Table Unlock": 2,
    "Mission 1 Briefing": 3,
    "Mission 2 Briefing": 4,
    "Mission 3 Briefing": 5,
    "Mission 4 Briefing": 6,
    "Mission 5 Briefing": 7,
    "Mission 6 Briefing": 8,
    "Mission 7 Briefing": 9,
    "Mission 8 Briefing": 10,
    "Mission 9 Briefing": 11,
    "Mission 10 Briefing": 12,
    "Mission 11 Briefing": 13,
    "Mission 12 Briefing": 14,
    "Mission 13 Briefing": 15,
    "Mission 14 Briefing": 16,
    "Mission 15 Briefing": 17,
    # Card Packs
    "AP Munitions Card Pack" : 100,
    "Cluster Munitions Card Pack" : 101,
    "Chemical Munitions Card Pack" : 102,
    "Utility Munitions Card Pack" : 103,
    "Explosive Munitions Card Pack" : 104,
    "Incendiary Munitions Card Pack" : 105,
    "Movement Card Pack" : 106,
    "Scouting Card Pack" : 107,
    # Punchcards
    "Punchcard - HE Shell" : 1000,
    "Punchcard - AP Shell" : 1001,
    "Punchcard - LE Shell" : 1002,
    "Punchcard - STAR Shell" : 1003,
    "Punchcard - TEAR Shell" : 1004,
    "Punchcard - SMK Shell" : 1005,
    "Punchcard - APHE Shell" : 1006,
    "Punchcard - HCHE Shell" : 1007,
    "Punchcard - DRIL Shell" : 1008,
    "Punchcard - INCN Shell" : 1009,
    "Punchcard - PHGN Shell" : 1010,
    "Punchcard - CYAN Shell" : 1011,
    "Punchcard - CLMN Shell" : 1012,
    "Punchcard - FLCH Shell" : 1013,
    "Punchcard - PCLM Shell" : 1014,
    "Punchcard - THRM Shell" : 1015,
    "Punchcard - WP Shell" : 1016,
    "Punchcard - PRPG Shell" : 1017,
    "Punchcard - ATMC Shell" : 1018,
    "Punchcard - EQKE Shell" : 1019,
    "Punchcard - Powder Charge" : 1020,
    "Punchcard - Location Report" : 1021,
    "Punchcard - Spotter" : 1022,
    "Punchcard - Scout Plane" : 1023,
    "Punchcard - Emergency Move" : 1024,
    "Punchcard - Move Direction" : 1025,
    # Requisitions
    "Requisition - Spotter" : 5001,
    "Requisition - Location Report" : 5002,
    "Requisition - Powder Charges" : 5003,
    "Requisition - Requisition Points" : 5004,
    # Traps
    "Trap - Emergency Move": 90001,
    "Trap - Magazine Filler": 90002,
    "Trap - Sabotage": 90003,
    "Trap - Counter-Battery": 90004,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    #"Right Gun Unlock": ItemClassification.progression,
    #"Requisition Table Unlock": ItemClassification.progression,
    "Mission 1 Briefing": ItemClassification.progression,
    "Mission 2 Briefing": ItemClassification.progression,
    "Mission 3 Briefing": ItemClassification.progression,
    "Mission 4 Briefing": ItemClassification.progression,
    "Mission 5 Briefing": ItemClassification.progression,
    "Mission 6 Briefing": ItemClassification.progression,
    "Mission 7 Briefing": ItemClassification.progression,
    "Mission 8 Briefing": ItemClassification.progression,
    "Mission 9 Briefing": ItemClassification.progression,
    "Mission 10 Briefing": ItemClassification.progression,
    "Mission 11 Briefing": ItemClassification.progression,
    "Mission 12 Briefing": ItemClassification.progression,
    "Mission 13 Briefing": ItemClassification.progression,
    "Mission 14 Briefing": ItemClassification.progression,
    "Mission 15 Briefing": ItemClassification.progression,
    # Card Packs
    "AP Munitions Card Pack" : ItemClassification.progression,
    "Cluster Munitions Card Pack" : ItemClassification.useful,
    "Chemical Munitions Card Pack" : ItemClassification.useful,
    "Utility Munitions Card Pack" : ItemClassification.useful,
    "Explosive Munitions Card Pack" : ItemClassification.progression,
    "Incendiary Munitions Card Pack" : ItemClassification.useful,
    "Movement Card Pack" : ItemClassification.progression | ItemClassification.useful,
    "Scouting Card Pack" : ItemClassification.useful,
    # Punch cards
    "Punchcard - HE Shell" : ItemClassification.progression,
    "Punchcard - AP Shell" : ItemClassification.progression,
    "Punchcard - LE Shell" : ItemClassification.progression,
    "Punchcard - STAR Shell" : ItemClassification.progression,
    "Punchcard - TEAR Shell" : ItemClassification.progression,
    "Punchcard - SMK Shell" : ItemClassification.progression,
    "Punchcard - APHE Shell" : ItemClassification.progression,
    "Punchcard - HCHE Shell" : ItemClassification.progression,
    "Punchcard - DRIL Shell" : ItemClassification.progression,
    "Punchcard - INCN Shell" : ItemClassification.progression,
    "Punchcard - PHGN Shell" : ItemClassification.progression,
    "Punchcard - CYAN Shell" : ItemClassification.progression,
    "Punchcard - CLMN Shell" : ItemClassification.progression,
    "Punchcard - FLCH Shell" : ItemClassification.progression,
    "Punchcard - PCLM Shell" : ItemClassification.progression,
    "Punchcard - THRM Shell" : ItemClassification.progression,
    "Punchcard - WP Shell" : ItemClassification.progression,
    "Punchcard - PRPG Shell" : ItemClassification.progression,
    "Punchcard - ATMC Shell" : ItemClassification.progression,
    "Punchcard - EQKE Shell" : ItemClassification.progression,
    "Punchcard - Powder Charge" : ItemClassification.progression,
    "Punchcard - Location Report" : ItemClassification.useful,
    "Punchcard - Spotter" : ItemClassification.useful,
    "Punchcard - Scout Plane" : ItemClassification.progression,
    "Punchcard - Emergency Move" : ItemClassification.progression,
    "Punchcard - Move Direction" : ItemClassification.progression,
    # Requisitions
    "Requisition - Spotter" : ItemClassification.useful,
    "Requisition - Location Report" : ItemClassification.useful,
    "Requisition - Powder Charges" : ItemClassification.filler,
    "Requisition - Requisition Points" : ItemClassification.filler,
    # Traps
    "Trap - Emergency Move": ItemClassification.trap,
    "Trap - Magazine Filler": ItemClassification.trap,
    "Trap - Sabotage": ItemClassification.trap,
    "Trap - Counter-Battery": ItemClassification.trap,
}

class IronNestCRItem(Item):
    game = "IRON NEST: Heavy Turret Simulator (CR)"

def get_random_filler_item_name(world:  IronNestCRWorld) -> str:
    cap = 60
    if world.options.iron_nest_cr_traps:
        cap = 99
    rand_choice = world.random.randint(0, cap)
    if rand_choice < 30:
        return "Requisition - Powder Charges"
    elif rand_choice < 60:
        return "Requisition - Requisition Points"
    elif rand_choice < 70:
        return "Trap - Magazine Filler"
    elif rand_choice < 80:
        return "Trap - Sabotage"
    elif rand_choice < 90:
        return "Trap - Counter-Battery"
    else:
        return "Trap - Emergency Move"


def create_item_with_correct_classification(world:  IronNestCRWorld, name: str) -> IronNestCRItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    # If Goal is Phantom Battery - Emergency Movement is a progression Item.
    if world.options.iron_nest_cr_goal == IronNestCRGoal.option_phantom_battery and (name == "Movement Card Pack" or name == "Emergency Move Requisition Card"):
        classification = ItemClassification.progression
    return IronNestCRItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: IronNestCRWorld) -> None:

    itempool: list[Item] = [
        #world.create_item("Right Gun Unlock"),
        #world.create_item("Requisition Table Unlock"),
        world.create_item("Mission 1 Briefing"),
        world.create_item("Mission 2 Briefing"),
        world.create_item("Mission 3 Briefing"),
        world.create_item("Mission 4 Briefing"),
        world.create_item("Mission 5 Briefing"),
        world.create_item("Mission 6 Briefing"),
        world.create_item("Mission 7 Briefing"),
        world.create_item("Mission 8 Briefing"),
        world.create_item("Mission 9 Briefing"),
        world.create_item("Mission 10 Briefing"),
        world.create_item("Mission 11 Briefing"),
        world.create_item("Mission 12 Briefing"),
        world.create_item("Mission 13 Briefing"),
        world.create_item("Mission 14 Briefing"),
        world.create_item("Mission 15 Briefing"),
        world.create_item("Punchcard - ATMC Shell"),
        world.create_item("Punchcard - EQKE Shell"),
        world.create_item("Punchcard - Powder Charge"),
    ]

    if world.options.card_packs:
        itempool += [
            world.create_item("AP Munitions Card Pack"),
            world.create_item("Cluster Munitions Card Pack"),
            world.create_item("Chemical Munitions Card Pack"),
            world.create_item("Utility Munitions Card Pack"),
            world.create_item("Explosive Munitions Card Pack"),
            world.create_item("Incendiary Munitions Card Pack"),
            world.create_item("Movement Card Pack"),
            world.create_item("Scouting Card Pack"),
        ]
    else :
        itempool += [
            # AP Munitions Pack
            world.create_item("Punchcard - AP Shell"),
            world.create_item("Punchcard - APHE Shell"),
            # Explosive Munitions Pack
            world.create_item("Punchcard - HE Shell"),
            world.create_item("Punchcard - LE Shell"),
            world.create_item("Punchcard - FLCH Shell"),
            world.create_item("Punchcard - HCHE Shell"),
            # Utility Munitions Pack
            world.create_item("Punchcard - STAR Shell"),
            world.create_item("Punchcard - SMK Shell"),
            world.create_item("Punchcard - PRPG Shell"),
            world.create_item("Punchcard - DRIL Shell"),
            # Chemical Munitions Pack
            world.create_item("Punchcard - TEAR Shell"),
            world.create_item("Punchcard - PHGN Shell"),
            world.create_item("Punchcard - CYAN Shell"),
            world.create_item("Punchcard - WP Shell"),
            # Cluster Munitions Pack
            world.create_item("Punchcard - CLMN Shell"),
            world.create_item("Punchcard - PCLM Shell"),
            # Incendiary Munitions Pack
            world.create_item("Punchcard - INCN Shell"),
            world.create_item("Punchcard - THRM Shell"),
            # Scouting Pack
            world.create_item("Punchcard - Scout Plane"),
            world.create_item("Punchcard - Spotter"),
            # Movement Pack
            world.create_item("Punchcard - Emergency Move"),
            world.create_item("Punchcard - Location Report"),
            world.create_item("Punchcard - Move Direction"),
        ]
    ## TODO - Add Medals as shuffled Items
    #if world.options.shuffle_medals:
    #    itempool += [
    #        world.create_item("Munitions Medal"),
    #    ]
    ##
    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool
