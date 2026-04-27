from collections.abc import Mapping
from typing import Any
from BaseClasses import Item, ItemClassification, MultiWorld, Tutorial
from worlds.AutoWorld import WebWorld, World

from . import Options as cg_options
from . import Items, Locations, Regions, Rules

class ChronoGearWebWorld(WebWorld):
    game = "Chrono Gear"
    theme = "ocean"
    setup_en = Tutorial(
        "Setup Guide",
        "A guide to setting up the Chrono Gear Archipelago Multiworld Randomizer",
        "English",
        "setup_en.md",
        "setup/en",
        ["Kalithar"],
    )

    tutorials = [setup_en]

    #Option groups and presets if I make them

class ChronoGearWorld(World):
    """Archipelago implementation for Chrono Gear: Warden of Time."""

    game = "Chrono Gear"
    web = ChronoGearWebWorld()

    options_dataclass = cg_options.ChronoGearOptions
    options: cg_options.ChronoGearOptions

    location_name_to_id = {name: data.id for name, data in Locations.get_locations_for_mapping().items()}
    item_name_to_id = {name: data.id for name, data in Items.get_items_for_mapping().items()}

    origin_region_name = "World Map"

    def create_regions(self) -> None:
        Regions.make_and_fill_regions(self)

    def set_rules(self) -> None:
        Rules.setAllRules(self)
    
    def create_items(self) -> None:
        Items.generate_all_items(self)

    def create_item(self, name: str) -> Item:
        return Items.generate_item(self, name)
    
    def get_filler_item_name(self) -> str:
        return Items.get_filler_name(self)
    
    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "goal_condition", "gear_hunt_requirement", "world_unlock_mode", "intermission_world_unlocks",
            "steel_on_steel_shackle_requirement", "zero_seconds_to_midnight_shackle_requirement", "early_chrono_gear"
        )