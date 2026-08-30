from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import IronNestWorld

# Every item must have a unique integer ID associated with it.
# We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
# Even if an item doesn't exist on specific options, it must be present in this lookup.
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
    # Our world class must have a create_item() function that can create any of our items by name at any time.
    # So, we make this helper function that creates the item by name with the correct classification.
    # Note: This function's content could just be the contents of world.create_item in world.py directly,
    # but it seemed nicer to have it in its own function over here in items.py.
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    # It is perfectly normal and valid for an item's classification to differ based on the player's options.
    # In our case, Health Upgrades are only relevant to logic (and thus labeled as "progression") in hard mode.
    return IronNestItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


# With those two helper functions defined, let's now get to actually creating and submitting our itempool.
def create_all_items(world: IronNestWorld) -> None:
    # This is the function in which we will create all the items that this world submits to the multiworld item pool.
    # There must be exactly as many items as there are locations.
    # In our case, there are either six or seven locations.
    # We must make sure that when there are six locations, there are six items,
    # and when there are seven locations, there are seven items.

    # Creating items should generally be done via the world's create_item method.
    # First, we create a list containing all the items that always exist.

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

    # Archipelago requires that each world submits as many locations as it submits items.
    # This is where we can use our filler and trap items.
    # APQuest has two of these: The Confetti Cannon and the Math Trap.
    # (Unfortunately, Archipelago is a bit ambiguous about its terminology here:
    #  "filler" is an ItemClassification separate from "trap", but in a lot of its functions,
    #  Archipelago will use "filler" to just mean "an additional item created to fill out the itempool".
    #  "Filler" in this sense can technically have any ItemClassification,
    #  but most commonly ItemClassification.filler or ItemClassification.trap.
    #  Starting here, the word "filler" will be used to collectively refer to APQuest's Confetti Cannon and Math Trap,
    #  which are ItemClassification.filler and ItemClassification.trap respectively.)
    # Creating filler items works the same as any other item. But there is a question:
    # How many filler items do we actually need to create?
    # In regions.py, we created either six or seven locations depending on the "extra_starting_chest" option.
    # In this function, we have created five or six items depending on whether the "hammer" option is enabled.
    # We *could* have a really complicated if-else tree checking the options again, but there is a better way.
    # We can compare the size of our itempool so far to the number of locations in our world.

    # The length of our itempool is easy to determine, since we have it as a list.
    number_of_items = len(itempool)

    # The number of locations is also easy to determine, but we have to be careful.
    # Just calling len(world.get_locations()) would report an incorrect number, because of our *event locations*.
    # What we actually want is the number of *unfilled* locations. Luckily, there is a helper method for this:
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Now, we just subtract the number of items from the number of locations to get the number of empty item slots.
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Finally, we create that many filler items and add them to the itempool.
    # To create our filler, we could just use world.create_item("Confetti Cannon").
    # But there is an alternative that works even better for most worlds, including APQuest.
    # As discussed above, our world must have a get_filler_item_name() function defined,
    # which must return the name of an infinitely repeatable filler item.
    # Defining this function enables the use of a helper function called world.create_filler().
    # You can just use this function directly to create as many filler items as you need to complete your itempool.
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # But... is that the right option for your game? Let's explore that.
    # For some games, the concepts of "regular itempool filler" and "additionally created filler" are different.
    # These games might want / require specific amounts of specific filler items in their regular pool.
    # To achieve this, they will have to intentionally create the correct quantities using world.create_item().
    # They may still use world.create_filler() to fill up the rest of their itempool with "repeatable filler",
    # after creating their "specific quantity" filler and still having room left over.

    # But there are many other games which *only* have infinitely repeatable filler items.
    # They don't care about specific amounts of specific filler items, instead only caring about the proportions.
    # In this case, world.create_filler() can just be used for the entire filler itempool.
    # APQuest is one of these games:
    # Regardless of whether it's filler for the regular itempool or additional filler for item links / etc.,
    # we always just want a Confetti Cannon or a Math Trap depending on the "trap_chance" option.
    # We defined this behavior in our get_random_filler_item_name() function, which in world.py,
    # we'll bind to world.get_filler_item_name(). So, we can just use world.create_filler() for all of our filler.

    # Anyway. With our world's itempool finalized, we now need to submit it to the multiworld itempool.
    # This is how the generator actually knows about the existence of our items.
    world.multiworld.itempool += itempool

    # Sometimes, you might want the player to start with certain items already in their inventory.
    # These items are called "precollected items".
    # They will be sent as soon as they connect for the first time (depending on your client's item handling flag).
    # Players can add precollected items themselves via the generic "start_inventory" option.
    # If you want to add your own precollected items, you can do so via world.push_precollected().
