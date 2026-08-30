from collections.abc import Mapping
from typing import Any

# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

# Imports of your world's files must be relative.
from . import items, locations, regions, rules, web_world
from . import options as ironnest_options  # rename due to a name conflict with World.options


class IronNestWorld(World):
    """
    IRON NEST: Heavy Turret Simulator is a dieselpunk alternate history where the monarchists never lost power
    """

    game = "IRON NEST: Heavy Turret Simulator"

    web = web_world.IronNestWebWorld()

    options_dataclass = ironnest_options.IronNestOptions
    options: ironnest_options.IronNestOptions  # Common mistake: This has to be a colon (:), not an equals sign (=).

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Mission 1"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    #def set_rules(self) -> None:
     #   rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.IronNestItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "basic_toggle",
        )
