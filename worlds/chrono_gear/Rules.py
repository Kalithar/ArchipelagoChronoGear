from __future__ import annotations

from typing import TYPE_CHECKING, Dict

from rule_builder.rules import Has, CanReachLocation, CanReachRegion, HasAllCounts
from worlds.chrono_gear.Locations import location_table, event_location_table, world_unlock_location_table, ChronoGearLocation, ChronoGearLocationData

if TYPE_CHECKING:
    from . import ChronoGearWorld

def setAllRules(world:ChronoGearWorld) -> None:
    setLocationRules(world)
    setOptionRules(world)
    setCompletionCondition(world)

def setLocationRules(world: ChronoGearWorld) -> None:
    locations: Dict[str, ChronoGearLocationData] = location_table
    if world.options.world_unlock_mode == 1:
        locations = locations | world_unlock_location_table
    for name, data in locations.items():
        if data.region == "Intermission":
            if world.options.intermission_world_unlocks == False:
                world.set_rule(world.get_location(name), 
                        CanReachLocation("Ganmo's Grand Finale - Golden Gear") & 
                        CanReachLocation("Wrath of Nature - Golden Gear"))
        else:
            if data.id == 111000: #Unlock Case Closed
                world.set_rule(world.get_location(name), 
                        CanReachLocation("Roboco Strikes Back - Golden Gear") & 
                        CanReachLocation("Another Time Traveler? - Clear Level"))
            elif data.id == 121000: #Unlock The Battle of Bell Town
                world.set_rule(world.get_location(name), 
                        CanReachLocation("The PolPol Express - Golden Gear") & 
                        CanReachLocation("The Gravity of Time - Golden Gear") &
                        CanReachLocation("The Shattered Keep - Golden Gear"))
            elif data.id == 240000: #Unlock Rebuilding the Lost City
                world.set_rule(world.get_location(name), 
                        CanReachLocation("Riding the Waves - Golden Gear") & 
                        CanReachLocation("The Floating Islands - Golden Gear"))
            elif data.id == 610000: #Unlock The Space Between Worlds
                world.set_rule(world.get_location(name),
                        CanReachLocation("Ganmo's Grand Finale - Golden Gear") & 
                        CanReachLocation("Wrath of Nature - Golden Gear"))
            elif data.id == 100100: #Council Meeting Golden Gear
                world.set_rule(world.get_location(name),
                        CanReachLocation("The Battle of Bell Town - Golden Gear"))
            elif data.id == 101100: #Secret Chamber Golden Gear
                world.set_rule(world.get_location(name),
                        Has("Golden Gear", 33) &
                        HasAllCounts({"Zero Seconds to Midnight": 1, "Laplus' Shackle": world.options.zero_seconds_to_midnight_shackle_requirement.value}))
            elif data.id == 100282 or data.id == 100288: #Steel on Steel CDs
                world.set_rule(world.get_location(name),
                        CanReachLocation("Steel on Steel - Unlock Zero Seconds to Midnight"))
            elif data.id == 100283: #ZStM CD 1
                world.set_rule(world.get_location(name),
                        CanReachLocation("Zero Seconds to Midnight - Clear Level"))
            elif data.id == 100284: #ZStM CD 2
                world.set_rule(world.get_location(name),
                        CanReachLocation("Zero Seconds to Midnight - Clear Level"))
            elif data.id == 300100: #The Ancient Weapon Golden Gear
                world.set_rule(world.get_location(name),
                        CanReachLocation("The Gravity of Time - Golden Gear") &
                        CanReachLocation("The Houshou Pirates - Golden Gear"))
            elif data.id == 400254: #Roboco CD
                world.set_rule(world.get_location(name),
                        CanReachLocation("Roboco Strikes Back - Golden Gear") &
                        CanReachLocation("Another Time Traveler? - Clear Level") &
                        CanReachRegion("Magic Resort"))
            elif data.id == 620000: #Complete A Way Home
                world.set_rule(world.get_location(name),
                               Has("Chrono Gear", 1))

def setOptionRules(world: ChronoGearWorld) -> None:
    if world.options.level_collectible_locations == True:
        for id in ["Autumn Harvest - Golden Gear", "Autumn Harvest - CD in winter pointed to by haste notes", "Autumn Harvest - Thread of Time above second winter warp trunk"]:
            world.set_rule(world.get_location(id), Has("Acorn", 10))
        if world.options.individual_score_locations == True:
            for id in ["Autumn Harvest - 100 Notes Score", "Autumn Harvest - 100 Time Score", "Autumn Harvest - 100 Damage Taken Score"]:
                world.set_rule(world.get_location(id), Has("Acorn", 10))
        if world.options.total_score_locations == True:
            world.set_rule(world.get_location("Autumn Harvest - 300 Total Score"), Has("Acorn", 10))
        
        for id in ["Path of Memories - Golden Gear", "Path of Memories - Unlock A Head Start"]:
            world.set_rule(world.get_location(id), Has("Maze Part", 10))
        if world.options.individual_score_locations == True:
            for id in ["Path of Memories - 100 Notes Score", "Path of Memories - 100 Time Score", "Path of Memories - 100 Damage Taken Score"]:
                world.set_rule(world.get_location(id), Has("Maze Part", 10))
        if world.options.total_score_locations == True:
            world.set_rule(world.get_location("Path of Memories - 300 Total Score"), Has("Maze Part", 10))
        
        for id in ["The Final Ascent - Unlock Steel on Steel", "The Final Ascent - Golden Gear", "The Final Ascent - CD in large room with Arc Sentinels", 
                   "The Final Ascent - CD above ruined portal", "The Final Ascent - CD at top of frozen time section with Shadow Armor"]:
            world.set_rule(world.get_location(id), Has("Tower Key", 1))
        world.set_rule(world.get_location("The Final Ascent - CD behind key locked door"), Has("Tower Key", 3))
        if world.options.individual_score_locations == True:
            for id in ["The Final Ascent - 100 Notes Score", "The Final Ascent - 100 Time Score", "The Final Ascent - 100 Damage Taken Score"]:
                world.set_rule(world.get_location(id), Has("Tower Key", 1))
        if world.options.total_score_locations == True:
            world.set_rule(world.get_location("The Final Ascent - 300 Total Score"), Has("Tower Key", 1))

    if world.options.sidequest_locations == True:
        world.set_rule(world.get_location("Starship ID - Golden Gear"), Has("Anya's Keris", 1))
        world.set_rule(world.get_location("Town Square - CD from fixing Roboco"), Has("Roboco's Schematics", 1))
        for id in ["Magic Resort - Golden Gear", "Magic Resort - Thread of Time for catching Trout", "Magic Resort - Thread of Time for catching Salmon", "Magic Resort - Thread of Time for catching Carp", "Magic Resort - Thread of Time for catching Eel",
                    "Magic Resort - Thread of Time for catching Dace", "Magic Resort - Thread of Time for catching Pike", "Magic Resort - Thread of Time for catching Bream"]:
            world.set_rule(world.get_location(id), Has("Fishing Rod", 1))
        for id in ["Town Square - Golden Gear", "Town Square - Thread of Time from powerwashing", "Town Square - CD in powerwashing room"]:
            world.set_rule(world.get_location(id), Has("Kobo's Gun", 1))

def setCompletionCondition(world: ChronoGearWorld) -> None:
    if world.options.goal_condition == 0:
        world.get_region("Steel on Steel").add_event("Clear Steel on Steel", "Victory")
        if world.options.gear_hunt_requirement.value > 0:
            world.set_completion_rule(HasAllCounts({"Golden Gear": world.options.gear_hunt_requirement.value, "Victory": 1}))
        else:
            world.set_completion_rule(Has("Victory"))
    else:
        world.get_region("Zero Seconds to Midnight").add_event("Clear Zero Seconds to Midnight", "Victory")
        if world.options.gear_hunt_requirement.value > 0:
            world.set_completion_rule(HasAllCounts({"Golden Gear": world.options.gear_hunt_requirement.value, "Victory": 1}))
        else:
            world.set_completion_rule(Has("Victory"))