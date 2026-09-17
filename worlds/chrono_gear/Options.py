from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class GoalCondition(Choice):
    """
    Set the level required to beat the game.
    """

    display_name = "Goal Condition"

    option_steel_on_steel = 0
    option_zstm = 1
    option_gear_hunt = 2

    default = option_zstm

class GearHuntRequirement(Range):
    """
    Adds an optional Golden Gear requirement to beat the game.
    The goal level must be cleared while holding this many Golden Gears.
    """
    display_name = "Gear Hunt Requirement"

    range_start = 0
    range_end = 35

    default = 0

class SteelOnSteelShackleRequirement(Range):
    """
    The number of Laplus' Shackles required to access Steel on Steel.
    """

    display_name = "Steel on Steel Shackle Requirement"

    range_start = 0
    range_end = 5

    default = 5

class ZStMShackleRequirement(Range):
    """
    The number of Laplus' Shackles required to access Zero Seconds to Midnight.
    """

    display_name = "Zero Seconds to Midnight Shackle Requirement"

    range_start = 0
    range_end = 5

    default = 5

class WorldUnlockMode(Choice):
    """
    Changes how the overall worlds are unlocked.
    Automatic unlocks worlds whenever a stage in that world is unlocked.
    Item adds the worlds as items to the pool that need to be obtained before those worlds are accessible.
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
    Does nothing if World Unlock Mode is set to automatic.
    """

    display_name = "World Unlocks on Intermission"

class StageIndividualScoreLocations(Toggle):
    """
    Adds locations to getting 100 score for notes, time, and damage taken to each stage.
    Levels that do not have a notes score requirement do not have that location added.
    """

    display_name = "Individual Score Locations"

class StageTotalScoreLocations(Toggle):
    """
    Adds locations for getting 300 total score in each stage.
    """

    display_name = "Total Score Locations"

#class StartingWorld(Choice):
#    """
#    Choose the world you will start in.
#    This gives you both that world and its hub as starting items.
#    This all assumes that I actually can do this easily
#    (If someone that isn't me sees this, ping me on discord)
#    """
#
#    display_name = "Starting World"
#
#    option_time = 0
#    option_nature = 1
#    option_space = 2
#   option_civilization = 3
#    option_chaos = 4
#    option_alter = 5
#    option_random = 6
    #No Darkness because it doesn't have a hub
#
#    default = option_time

class EarlyChronoGear(Toggle):
    """
    Controls whether the Chrono Gear is usable in levels before you would normally obtain it.
    If disabled, the Chrono Gear is only usable in the levels it is normally usable in (A Way Home and later).
    If enabled, it is usable in all levels once acquired.
    """

    display_name = "Early Chrono Gear"

    default = True



@dataclass
class ChronoGearOptions(PerGameCommonOptions):
    goal_condition: GoalCondition
    gear_hunt_requirement: GearHuntRequirement
    world_unlock_mode: WorldUnlockMode
    intermission_world_unlocks: IntermissionWorldUnlocks
    individual_score_locations: StageIndividualScoreLocations
    total_score_locations: StageTotalScoreLocations
    #starting_world: StartingWorld
    steel_on_steel_shackle_requirement: SteelOnSteelShackleRequirement
    zero_seconds_to_midnight_shackle_requirement: ZStMShackleRequirement
    early_chrono_gear: EarlyChronoGear
