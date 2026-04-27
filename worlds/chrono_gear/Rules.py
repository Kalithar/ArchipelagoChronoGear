from __future__ import annotations

from typing import TYPE_CHECKING, Dict

from rule_builder.rules import Has, CanReachLocation, CanReachRegion
from worlds.chrono_gear.Locations import location_table, event_location_table, world_unlock_location_table, ChronoGearLocation, ChronoGearLocationData

if TYPE_CHECKING:
    from . import ChronoGearWorld

def setAllRules(world:ChronoGearWorld) -> None:
    setLocationRules(world)
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
                        Has("Golden Gear", 34))
            elif data.id == 100282: #Steel on Steel CD
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
                        CanReachLocation("The Gravity of Time - Golden Gear"))
            elif data.id == 400254: #Roboco CD
                world.set_rule(world.get_location(name),
                        CanReachLocation("Roboco Strikes Back - Golden Gear") &
                        CanReachLocation("Another Time Traveler? - Clear Level") &
                        CanReachRegion("Magic Resort"))
    

def setCompletionCondition(world: ChronoGearWorld) -> None:
    if world.options.goal_condition == 0:
        world.get_region("Steel on Steel").add_event("Clear Steel on Steel", "Victory")
        world.set_completion_rule(Has("Victory"))
    elif world.options.goal_condition == 1:
        world.get_region("Zero Seconds to Midnight").add_event("Clear Zero Seconds to Midnight", "Victory")
        world.set_completion_rule(Has("Victory"))
    else:
        world.set_completion_rule(Has("Golden Gear", world.options.gear_hunt_requirement))