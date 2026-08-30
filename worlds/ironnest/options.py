from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class BasicToggle(Toggle):
    """
    A basic Toggle option
    """

    display_name = "Basic Toggle"

@dataclass
class IronNestOptions(PerGameCommonOptions):
    basic_toggle: BasicToggle

option_presets = {
    "boring": {
        "basic_toggle": False,
    },
}
