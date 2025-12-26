from typing import TYPE_CHECKING

from BaseClasses import Region, ItemClassification
from worlds.chrono_gear.Locations import location_table, event_location_table, ChronoGearLocation
from worlds.generic.Rules import set_rule
from . import Items

if TYPE_CHECKING:
    from . import ChronoGearWorld


def make_and_fill_regions(world: ChronoGearWorld):
    create_and_connect_regions(world)
    add_locations(world)

def create_and_connect_regions(world: ChronoGearWorld):
    world_map = Region("World Map", world.player, world.multiworld)
    world.multiworld.regions += world_map
    
    #World of Time
    world_of_time = Region("World of Time", world.player, world.multiworld)
    storming = Region("Storming the Sanctum", world.player, world.multiworld)
    time_hub = Region("Eternity Sanctum", world.player, world.multiworld)
    time_shop_1 = Region("Eternity Sanctum Shop Page 1", world.player, world.multiworld)
    time_shop_2 = Region("Eternity Sanctum Shop Page 2", world.player, world.multiworld)
    time_shop_3 = Region("Eternity Sanctum Shop Page 3", world.player, world.multiworld)
    case_closed = Region("Case Closed", world.player, world.multiworld)
    bell_tower = Region("The Top of Bell Tower", world.player, world.multiworld)
    defending = Region("Defending the Sanctum", world.player, world.multiworld)
    bell_battle = Region("The Battle of Bell Town", world.player, world.multiworld)
    polpol_express = Region("The PolPol Express", world.player, world.multiworld)
    gravity = Region("The Gravity of Time", world.player, world.multiworld)
    shattered = Region("The Shattered Keep", world.player, world.multiworld)

    time_regions = [world_of_time, storming, time_hub, time_shop_1, time_shop_2, time_shop_3, case_closed, 
                    defending, bell_battle, bell_tower, polpol_express, gravity, shattered]

    #World of Nature
    world_of_nature = Region("World of Nature", world.player, world.multiworld)
    nature_hub = Region("Magic Resort", world.player, world.multiworld)
    nature_shop = Region("Magic Resort Shop", world.player, world.multiworld)
    call_to_nature = Region("Call to Nature", world.player, world.multiworld)
    autumn_harvest = Region("Autumn Harvest", world.player, world.multiworld)
    wrath_of_nature = Region("Wrath of Nature", world.player, world.multiworld)
    floating_islands = Region("The Floating Islands", world.player, world.multiworld)
    riding_the_waves = Region("Riding the Waves", world.player, world.multiworld)
    chloe_race = Region("Chloe's Beach Race", world.player, world.multiworld)
    lost_city = Region("Rebuilding the Lost City", world.player, world.multiworld)

    nature_regions = [world_of_nature, nature_hub, nature_shop, call_to_nature, autumn_harvest, 
                      wrath_of_nature, floating_islands, riding_the_waves, chloe_race, lost_city]

    #World of Space
    world_of_space = Region("World of Space", world.player, world.multiworld)
    space_hub = Region("Starship ID", world.player, world.multiworld)
    space_shop_1 = Region("Starship ID Shop Page 1", world.player, world.multiworld)
    space_shop_2 = Region("Starship ID Shop Page 2", world.player, world.multiworld)
    space_bake = Region("The Great Space Bake", world.player, world.multiworld)
    houshou_pirates = Region("The Houshou Pirates", world.player, world.multiworld)
    lunkight_darkness = Region("Luknight of Darkness", world.player, world.multiworld)
    ganmo_finale = Region("Ganmo's Grand Finale", world.player, world.multiworld)

    space_regions = [world_of_space, space_hub, space_shop_1, space_shop_2, space_bake, houshou_pirates, lunkight_darkness, ganmo_finale]

    #World of Civilization
    world_of_civ = Region("World of Civilization", world.player, world.multiworld)
    civ_hub = Region("Town Square", world.player, world.multiworld)
    civ_shop = Region("Town Square Shop", world.player, world.multiworld)
    road_to_civ = Region("The Road to Civilization", world.player, world.multiworld)
    roboco_strikes = Region("Roboco Strikes Back", world.player, world.multiworld)
    path_memories = Region("Path of Memories", world.player, world.multiworld)
    head_start = Region("A Head Start", world.player, world.multiworld)
    war_mind = Region("The War Mind", world.player, world.multiworld)

    civ_regions = [world_of_civ, civ_hub, civ_shop, road_to_civ, roboco_strikes, path_memories, head_start, war_mind]

    #World of Chaos

    world_of_chaos = Region("World of Chaos", world.player, world.multiworld)
    chaos_hub = Region("The Funzone", world.player, world.multiworld)
    chaos_shop = Region("The Funzone Shop", world.player, world.multiworld)
    caravan = Region("Caravan of Darkness", world.player, world.multiworld)
    overclocking = Region("Overclocking the Arcade", world.player, world.multiworld)
    song_light_dark = Region("Song of Light and Darkness", world.player, world.multiworld)
    kfp_games = Region("The KFP Games", world.player, world.multiworld)
    time_traveler = Region("Another Time Traveler?", world.player, world.multiworld)

    chaos_regions = [world_of_chaos, chaos_hub, chaos_shop, caravan, overclocking, song_light_dark, kfp_games, time_traveler]

    #Alter Timeline
    world_alter = Region("Alter Timeline", world.player, world.multiworld)
    solitude = Region("Solitude", world.player, world.multiworld)
    bunker = Region("The Bunker", world.player, world.multiworld)
    entropy = Region("Entropy", world.player, world.multiworld)
    ancient = Region("The Ancient Ones", world.player, world.multiworld)
    gloom = Region("Gloom", world.player, world.multiworld)
    despair = Region("Despair", world.player, world.multiworld)
    hope = Region("Hope", world.player, world.multiworld)
    way_home = Region("The Way Home", world.player, world.multiworld)

    alter_regions = [world_alter, solitude, bunker, entropy, ancient, gloom, despair, hope, way_home]

    #World of Darkness
    world_darkness = Region("World of Darkness", world.player, world.multiworld)
    space_between = Region("The Space Between Worlds", world.player, world.multiworld)
    time_is_now = Region("Her Time is Now", world.player, world.multiworld)
    final_ascent = Region("The Final Ascent", world.player, world.multiworld)
    steel_steel = Region("Steel on Steel", world.player, world.multiworld)
    zstm = Region("Zero Seconds to Midnight", world.player, world.multiworld)

    darkness_regions = [world_darkness, space_between, time_is_now, final_ascent, steel_steel, zstm]

    world.multiworld.regions += time_regions
    world.multiworld.regions += nature_regions
    world.multiworld.regions += space_regions
    world.multiworld.regions += civ_regions
    world.multiworld.regions += chaos_regions
    world.multiworld.regions += alter_regions
    world.multiworld.regions += darkness_regions

    #Connect regions
    #World Map
    
    if(world.options.world_unlock_mode == 1):
        world_map.connect(world_of_time, "World Map to World of Time", lambda state: state.has("World of Time", world.player))
        world_map.connect(world_of_nature, "World Map to World of Nature", lambda state: state.has("World of Nature", world.player))
        world_map.connect(world_of_space, "World Map to World of Space", lambda state: state.has("World of Space", world.player))
        world_map.connect(world_of_civ, "World Map to World of Civilization", lambda state: state.has("World of Civilization", world.player))
        world_map.connect(world_of_chaos, "World Map to World of Chaos", lambda state: state.has("World of Chaos", world.player))
        world_map.connect(world_alter, "World Map to Alter Timeline", lambda state: state.has("Alter Timeline", world.player))
        world_map.connect(world_darkness, "World Map to World of Darkness", lambda state: state.has("World of Darkness", world.player))
    else:
        world_map.connect(world_of_time, "World Map to World of Time")
        world_map.connect(world_of_nature, "World Map to World of Nature")
        world_map.connect(world_of_space, "World Map to World of Space")
        world_map.connect(world_of_civ, "World Map to World of Civilization")
        world_map.connect(world_of_chaos, "World Map to World of Chaos")
        world_map.connect(world_alter, "World Map to Alter Timeline")
        world_map.connect(world_darkness, "World Map to World of Darkness")

    #World of Time
    time_regions.remove(world_of_time)
    for region in time_regions:
        if region == time_shop_1:
            time_hub.connect(region, "Eternity Sanctum to Time Shop Page 1", lambda state: state.has("Thread of Time - Time Page 1", world.player, 5))
        elif region == time_shop_2:
            time_hub.connect(region, "Eternity Sanctum to Time Shop Page 2", lambda state: state.has_all_counts({"Thread of Time - Time Page 2": 5, "Golden Gear": 7}, world.player)) 
        elif region == time_shop_3:
            time_hub.connect(region, "Eternity Sanctum to Time Shop Page 3", lambda state: state.has_all_counts({"Thread of Time - Time Page 3": 13, "Golden Gear": 32}, world.player))
        else:
            world_of_time.connect(region, "World of Time to " + region.name, lambda state: state.has(region.name, world.player))
    
    #World of Nature
    nature_regions.remove(world_of_nature)
    for region in nature_regions:
        if region == nature_shop:
            nature_hub.connect(region, "Magic Resort to Nature Shop", lambda state: state.has("Thread of Time - Nature", world.player, 4))
        else:
            world_of_nature.connect(region, "World of Nature to " + region.name, lambda state: state.has(region.name, world.player))
    
    #World of Space
    space_regions.remove(world_of_space)
    for region in space_regions:
        if region == space_shop_1:
            space_hub.connect(region, "Starship ID to Space Shop Page 1", lambda state: state.has("Thread of Time - Space Page 1", world.player, 4))
        elif region == space_shop_2:
            space_hub.connect(region, "Starship ID to Space Shop Page 2", lambda state: state.has_all_counts({"Thread of Time - Space Page 2": 4, "Golden Gear": 17}, world.player))
        else:
            world_of_space.connect(region, "World of Space to " + region.name, lambda state: state.has(region.name, world.player))
    
    #World of Civ
    civ_regions.remove(world_of_civ)
    for region in civ_regions:
        if region == civ_shop:
            civ_hub.connect(region, "Town Square to Civilization Shop", lambda state: state.has("Thread of Time - Civilization", world.player, 7))
        else:
            world_of_civ.connect(region, "World of Civilization to " + region.name, lambda state: state.has(region.name, world.player))
    
    #World of Chaos
    chaos_regions.remove(world_of_chaos)
    for region in chaos_regions:
        if region == chaos_shop:
            chaos_hub.connect(region, "The Funzone to Chaos Shop", lambda state: state.has("Thread of Time - Chaos", world.player, 9))
        else:
            world_of_chaos.connect(region, "World of Chaos to " + region.name, lambda state: state.has(region.name, world.player))
    
    #Alter Timeline
    alter_regions.remove(world_alter)
    for region in alter_regions:
        world_alter.connect(region, "Alter Timeline to " + region.name, lambda state: state.has(region.name, world.player))

    #World of Darkness
    world_darkness.remove(world_darkness)
    for region in darkness_regions:
        if region == final_ascent:
            world_darkness.connect(region, "World of Darkness to The Final Ascent", lambda state: state.has_all([region.name, "Chrono Gear"], world.player))
        elif region == steel_steel:
            world_darkness.connect(region, "World of Darkness to Steel on Steel", lambda state: state.has_all_counts({region.name: 1, "Laplus' Shackle": world.options.steel_on_steel_shackle_requirement, "Chrono Gear": 1}, world.player))
        elif region == zstm:
            world_darkness.connect(region, "World of Darkness to Zero Seconds to Midnight", lambda state: state.has_all_counts({region.name: 1, "Laplus' Shackle": world.options.zero_seconds_to_midnight_shackle_requirement, "Chrono Gear": 1}, world.player))
        else:
            world_darkness.connect(region, "World of Darkness to " + region.name, lambda state: state.has(region.name, world.player))


def add_locations(world: ChronoGearWorld):
    for name, data in location_table:
        region = world.get_region(data.region)
        if region.name == "Intermission":
            if world.options.intermission_world_unlocks == False:
                world.get_region("World Map").add_locations({name, data.id}, ChronoGearLocation)
                set_rule(world.get_location(name), 
                         lambda state: state.can_reach_location("Ganmo's Grand Finale - Golden Gear", world.player) and 
                                       state.can_reach_location("Wrath of Nature - Golden Gear", world.player))
            else:
                world.get_region("The Space Between Worlds").add_locations({name, data.id}, ChronoGearLocation)
        elif name == "World Map - Unlock Case Closed":
            region.add_locations({name, data.id}, ChronoGearLocation)
            set_rule(world.get_location(name), 
                     lambda state: state.can_reach_location("Roboco Strikes Back - Golden Gear", world.player) and 
                                   state.can_reach_location("Another Time Traveler? - Clear Level", world.player))
        elif name == "World of Time - Unlock The Battle of Bell Town":
            region.add_locations({name, data.id}, ChronoGearLocation)
            set_rule(world.get_location(name), 
                     lambda state: state.can_reach_location("The PolPol Express - Golden Gear", world.player) and 
                                   state.can_reach_location("The Gravity of Time - Golden Gear", world.player) and
                                   state.can_reach_location("The Shattered Keep - Golden Gear", world.player))
        elif name == "World of Nature - Unlock Rebuilding the Lost City":
            region.add_locations({name, data.id}, ChronoGearLocation)
            set_rule(world.get_location(name), 
                     lambda state: state.can_reach_location("Riding the Waves - Golden Gear", world.player) and 
                                   state.can_reach_location("The Floating Islands - Golden Gear", world.player))
        elif name == "World Map - Unlock The Space Between Worlds":
            region.add_locations({name, data.id}, ChronoGearLocation)
            set_rule(world.get_location(name),
                     lambda state: state.can_reach_location("Ganmo's Grand Finale - Golden Gear", world.player) and 
                                       state.can_reach_location("Wrath of Nature - Golden Gear", world.player))
        else:
            region.add_locations({name, data.id}, ChronoGearLocation)

    for name, data in event_location_table:
        region = world.get_region(data.region)
        region.add_locations({name, data.id}, ChronoGearLocation)
        world.get_location(name).place_locked_item(Items.CGItem(None, name, ItemClassification.progression))


    
    
