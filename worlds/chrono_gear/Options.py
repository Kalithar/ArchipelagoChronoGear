from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class GoalCondition(Choice):
    """
    Sets the condition for clearing your game.
    Steel on Steel and Zero Seconds to Midnight: Clear the chosen level
    Gear Hunt: Receive a configurable number of Golden Gears
    """

    display_name = "Goal Condition"

    option_steel_on_steel = 0
    option_zstm = 1
    option_gear_hunt = 2

    default = option_zstm

class GearHuntRequirement(Range):
    """
    Sets the required number of Golden Gears for the Gear Hunt goal condition.
    Does nothing if the goal condition is not set to Gear Hunt.
    """
    display_name = "Gear Hunt Requirement"

    range_start = 1
    range_end = 35

    default = 35


class WorldUnlockMode(Choice):
    """
    Changes how the overall worlds are unlocked.
    Automatic unlocks worlds whenever a stage in that world is unlocked.
    Item adds the worlds as items to the pool that need to be obtained before those worlds are accessible.
    Regardless of choice here, the alter timeline also requires the Chrono Gear.
    """
    display_name = "World Unlock Mode"

    option_automatic = 0
    option_item = 1

    default = option_item

class IntermissionWorldUnlocks(Toggle):
    """
    Controls where the checks for the worlds of Civilization and Chaos are.
    If enabled, the checks will be from completing the intermission (The Space Between Worlds).
    If disabled, the checks will be after completing the boss levels of Nature and Space. 
    """

    display_name = "World Unlocks on Intermission"

class StartingWorld(Choice):
    """
    Choose the world you will start in.
    This gives you both that world and its hub as starting items.
    This all assumes that I actually can do this easily
    (If someone that isn't me sees this, ping me on discord)
    """

    display_name = "Starting World"

    option_time = 0
    option_nature = 1
    option_space = 2
    option_civilization = 3
    option_chaos = 4
    option_alter = 5
    #No Darkness because it doesn't have a hub

    default = option_time

class SteelOnSteelShackleRequirement(Range):
    """
    The number of Laplus' Shackles required to access Steel on Steel
    """

    display_name = "Steel on Steel Shackle Requirement"

    range_start = 0
    range_end = 5

    default = 5

class ZStMShackleRequirement(Range):
    """
    The number of Laplus' Shackles required to access Zero Seconds to Midnight
    """

    display_name = "Zero Seconds to Midnight Shackle Requirement"

    range_start = 0
    range_end = 5

    default = 5

@dataclass
class ChronoGearOptions(PerGameCommonOptions):
    goal_condition: GoalCondition
    gear_hunt_requirement: GearHuntRequirement
    world_unlock_mode: WorldUnlockMode
    intermission_world_unlocks: IntermissionWorldUnlocks
    starting_world: StartingWorld
    steel_on_steel_shackle_requirement: SteelOnSteelShackleRequirement
    zero_seconds_to_midnight_shackle_requirement: ZStMShackleRequirement
