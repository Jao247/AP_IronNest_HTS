from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_presets


# For our game to display correctly on the website, we need to define a WebWorld subclass.
class IronNestCRWebWorld(WebWorld):
    game = "IRON NEST: Heavy Turret Simulator (CR)"

    theme = "grassFlowers"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "IronNest CR setup guide",
        "English",
        "setup_en.md",
        "setup/en",
        ["CelticKuma"],
    )

    tutorials = [setup_en]

    options_presets = option_presets
