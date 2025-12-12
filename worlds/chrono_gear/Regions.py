from BaseClasses import Region, Location, LocationProgressType
from typing import TYPE_CHECKING
from .Locations import (
    ChronoGearLocation,
    location_table_time_hub,
    location_table_time_shop_page_1,
    location_table_time_shop_page_2,
    location_table_time_shop_page_3,
    location_table_storming_the_sanctum,
    location_table_case_closed,
    location_table_defending_the_sanctum,
    location_table_top_of_bell_tower,
    location_table_battle_of_bell_town,
    location_table_polpol_express,
    location_table_gravity_of_time,
    location_table_shattered_keep,
    location_table_nature_hub,
    location_table_nature_shop,
    location_table_call_to_nature,
    location_table_autumn_harvest,
    location_table_wrath_of_nature,
    location_table_the_floating_islands,
    location_table_riding_the_waves,
    location_table_chloes_beach_race,
    location_table_rebuilding_the_lost_city,
    location_table_space_hub,
    location_table_space_shop_page_1,
    location_table_space_shop_page_2,
    location_table_the_great_space_bake,
    location_table_the_houshou_pirates,
    location_table_luknight_of_darkness,
    location_table_ganmos_grand_finale,
    location_table_civ_hub,
    location_table_civ_shop,
    location_table_the_road_to_civilization,
    location_table_roboco_strikes_back,
    location_table_path_of_memories,
    location_table_a_head_start,
    location_table_the_war_mind,
    location_table_chaos_hub,
    location_table_chaos_shop,
    location_table_caravan_of_darkness,
    location_table_overclocking_the_arcade,
    location_table_song_of_light_and_darkness,
    location_table_the_kfp_games,
    location_table_another_time_travler,
    location_table_solitude,
    location_table_entropy,
    location_table_the_ancient_ones,
    location_table_gloom,
    location_table_despair,
    location_table_hope,
    location_table_the_way_home,
    location_table_intermission,
    location_table_her_time_is_now,
    location_table_the_final_ascent,
    location_table_steel_on_steel,
    location_table_zero_seconds_to_midnight,
)

#Thing about type checking
if TYPE_CHECKING:
    from . import ChronoGearWorld

def create_and_connect_regions(world: ChronoGearWorld) -> None:
    create_time_regions(world)
    create_nature_regions(world)
    create_space_regions(world)
    create_civ_regions(world)
    create_chaos_regions(world)
    create_alter_regions(world)
    creates_darkness_regions(world)

    connect_time_regions(world)
    connect_nature_regions(world)
    connect_space_regions(world)
    connect_civ_regions(world)
    connect_chaos_regions(world)
    connect_alter_regions(world)
    connect_darkness_regions(world)

def create_time_regions(world: ChronoGearWorld) -> None:
    time_hub = Region("Eternity Sanctum", world.player, world.multiworld)
    time_shop_1 = Region("Eternity Sanctum Shop Page 1", world.player, world.multiworld)
    time_shop_2 = Region("Eternity Sanctum Shop Page 2", world.player, world.multiworld)
    time_shop_3 = Region("Eternity Sanctum Shop Page 3", world.player, world.multiworld)
    storming_the_sanctum = Region("Storming the Sanctum", world.player, world.multiworld)
    defending_the_sanctum = Region("Defending the Sanctum", world.player, world.multiworld)
    case_closed = Region("Case Closed", world.player, world.multiworld)
    top_of_bell_tower = Region("The Top of Bell Tower", world.player, world.multiworld)
    battle_of_bell_town = Region("The Battle of Bell Town", world.player, world.multiworld)
    polpol_express = Region("The PolPol Express", world.player, world.multiworld)
    gravity_of_time = Region("The Gravity of Time", world.player, world.multiworld)
    shattered_keep = Region("The Shattered Keep", world.player, world.multiworld)

    time_hub.add_locations(location_table_time_hub, ChronoGearLocation)
    time_shop_1.add_locations(location_table_time_shop_page_1, ChronoGearLocation)
    time_shop_2.add_locations(location_table_time_shop_page_2, ChronoGearLocation)
    time_shop_3.add_locations(location_table_time_shop_page_3, ChronoGearLocation)
    storming_the_sanctum.add_locations(location_table_storming_the_sanctum, ChronoGearLocation)
    defending_the_sanctum.add_locations(location_table_defending_the_sanctum, ChronoGearLocation)
    case_closed.add_locations(location_table_case_closed, ChronoGearLocation)
    top_of_bell_tower.add_locations(location_table_top_of_bell_tower, ChronoGearLocation)
    battle_of_bell_town.add_locations(location_table_battle_of_bell_town, ChronoGearLocation)
    polpol_express.add_locations(location_table_polpol_express, ChronoGearLocation)
    gravity_of_time.add_locations(location_table_gravity_of_time, ChronoGearLocation)
    shattered_keep.add_locations(location_table_shattered_keep, ChronoGearLocation)

    regions = [time_hub, time_shop_1, time_shop_2, time_shop_3, storming_the_sanctum, defending_the_sanctum, 
               case_closed, top_of_bell_tower, battle_of_bell_town, polpol_express, gravity_of_time, shattered_keep]
    
    world.multiworld.regions += regions

def create_nature_regions(world: ChronoGearWorld) -> None:
    nature_hub = Region("Magic Resort", world.player, world.multiworld)
    nature_shop = Region("Magic Resort Shop", world.player, world.multiworld)
    call_to_nature = Region("Call to Nature", world.player, world.multiworld)
    autumn_harvest = Region("Autumn Harvest", world.player, world.multiworld)
    wrath_of_nature = Region("Wrath of Nature", world.player, world.multiworld)
    floating_islands = Region("The Floating Islands", world.player, world.multiworld)
    riding_the_waves = Region("Riding the Waves", world.player, world.multiworld)
    beach_race = Region("Chloe's Beach Race", world.player, world.multiworld)
    rebuilding_atlantis = Region("Rebuilding the Lost City", world.player, world.multiworld)

    nature_hub.add_locations(location_table_nature_hub, ChronoGearLocation)
    nature_shop.add_locations(location_table_nature_shop, ChronoGearLocation)
    call_to_nature.add_locations(location_table_call_to_nature, ChronoGearLocation)
    autumn_harvest.add_locations(autumn_harvest, ChronoGearLocation)
    wrath_of_nature.add_locations(location_table_wrath_of_nature, ChronoGearLocation)
    floating_islands.add_locations(location_table_the_floating_islands, ChronoGearLocation)
    riding_the_waves.add_locations(location_table_riding_the_waves, ChronoGearLocation)
    beach_race.add_locations(location_table_chloes_beach_race, ChronoGearLocation)
    rebuilding_atlantis.add_locations(location_table_rebuilding_the_lost_city, ChronoGearLocation)

    regions = [nature_hub, nature_shop, call_to_nature, autumn_harvest, wrath_of_nature, floating_islands, 
               riding_the_waves, beach_race, rebuilding_atlantis]
    
    world.multiworld.regions += regions

def create_space_regions(world: ChronoGearWorld) -> None:
    space_hub = Region("Spaceship ID", world.player, world.multiworld)
    space_shop_1 = Region("Spaceship ID Shop Page 1", world.player, world.multiworld)
    space_shop_2 = Region("Spaceship ID Shop Page 2", world.player, world.multiworld)
    space_bake = Region("The Great Space Bake", world.player, world.multiworld)
    houshou_pirates = Region("The Houshou Pirates", world.player, world.multiworld)
    luknight_of_darkness = Region("Luknight of Darkness", world.player, world.multiworld)
    ganmo_grand_finale = Region("Ganmo's Grand Finale", world.player, world.multiworld)

    space_hub.add_locations(location_table_space_hub, ChronoGearLocation)
    space_shop_1.add_locations(location_table_space_shop_page_1, ChronoGearLocation)
    space_shop_2.add_locations(location_table_space_shop_page_2, ChronoGearLocation)
    space_bake.add_locations(location_table_the_great_space_bake, ChronoGearLocation)
    houshou_pirates.add_locations(location_table_the_houshou_pirates, ChronoGearLocation)
    luknight_of_darkness.add_locations(location_table_luknight_of_darkness, ChronoGearLocation)
    ganmo_grand_finale.add_locations(location_table_ganmos_grand_finale, ChronoGearLocation)

    regions = [space_hub, space_shop_1, space_shop_2, space_bake, houshou_pirates, luknight_of_darkness, ganmo_grand_finale]

    world.multiworld.regions += regions

def create_civ_regions(world: ChronoGearWorld) -> None:
    civ_hub = Region("Town Square", world.player, world.multiworld)
    civ_shop = Region("Town Square Shop", world.player, world.multiworld)
    road_to_civ = Region("The Road to Civilization", world.player, world.multiworld)
    roboco_strikes_back = Region("Roboco Strikes Back", world.player, world.multiworld)
    path_of_memories = Region("Path of Memories", world.player, world.multiworld)
    cursed_lands = Region("A Head Start", world.player, world.multiworld)
    war_mind = Region("The War Mind", world.player, world.multiworld)

    civ_hub.add_locations(location_table_civ_hub, ChronoGearLocation)
    civ_shop.add_locations(location_table_civ_shop, ChronoGearLocation)
    road_to_civ.add_locations(location_table_the_road_to_civilization, ChronoGearLocation)
    roboco_strikes_back.add_locations(location_table_roboco_strikes_back, ChronoGearLocation)
    path_of_memories.add_locations(location_table_path_of_memories, ChronoGearLocation)
    cursed_lands.add_locations(location_table_a_head_start, ChronoGearLocation)
    war_mind.add_locations(location_table_the_war_mind, ChronoGearLocation)

    regions = [civ_hub, civ_shop, road_to_civ, roboco_strikes_back, path_of_memories, cursed_lands, war_mind]

    world.multiworld.regions += regions

def create_chaos_regions(world: ChronoGearWorld) -> None:
    chaos_hub = Region("The Funzone", world.player, world.multiworld)
    chaos_shop = Region("The Funzone Shop", world.player, world.multiworld)
    caravan_of_darkness = Region("Caravan of Darkness", world.player, world.multiworld)
    overclocking_arcade = Region("Overclocking the Arcade", world.player, world.multiworld)
    song_light_dark = Region("Song of Light and Darkness", world.player, world.multiworld)
    kfp_games = Region("The KFP Games", world.player, world.multiworld)
    another_time_traveler = Region("Another Time Traveler?", world.player, world.multiworld)

    chaos_hub.add_locations(location_table_chaos_hub, ChronoGearLocation)
    chaos_shop.add_locations(location_table_chaos_shop, ChronoGearLocation)
    caravan_of_darkness.add_locations(caravan_of_darkness, ChronoGearLocation)
    overclocking_arcade.add_locations(location_table_overclocking_the_arcade, ChronoGearLocation)
    song_light_dark.add_locations(location_table_song_of_light_and_darkness, ChronoGearLocation)
    kfp_games.add_locations(location_table_the_kfp_games, ChronoGearLocation)
    another_time_traveler.add_locations(location_table_another_time_travler, ChronoGearLocation)

    regions = [chaos_hub, chaos_shop, caravan_of_darkness, overclocking_arcade, song_light_dark, kfp_games, another_time_traveler]

    world.multiworld.regions += regions

def create_alter_regions(world: ChronoGearWorld) -> None:
    alter_hub = Region("The Bunker", world.player, world.multiworld)
    solitude = Region("Solitude", world.player, world.multiworld)
    entropy = Region("Entropy", world.player, world.multiworld)
    ancient_ones = Region("The Ancient Ones", world.player, world.multiworld)
    gloom = Region("Gloom", world.player, world.multiworld)
    despair = Region("Despair", world.player, world.multiworld)
    hope = Region("Hope", world.player, world.multiworld)
    the_way_home = Region("The Way Home", world.player, world.multiworld)

    solitude.add_locations(location_table_solitude, ChronoGearLocation)
    entropy.add_locations(location_table_entropy, ChronoGearLocation)
    ancient_ones.add_locations(location_table_the_ancient_ones, ChronoGearLocation)
    gloom.add_locations(location_table_gloom, ChronoGearLocation)
    despair.add_locations(location_table_despair, ChronoGearLocation)
    hope.add_locations(location_table_hope, ChronoGearLocation)
    the_way_home.add_locations(location_table_the_way_home, ChronoGearLocation)

    regions = [alter_hub, solitude, entropy, ancient_ones, gloom, despair, hope, the_way_home]

    world.multiworld.regions += regions

def creates_darkness_regions(world: ChronoGearWorld) -> None:
    intermission = Region("The Space Between Worlds", world.player, world.multiworld)
    dark_nest = Region("Her Time is Now", world.player, world.multiworld)
    final_ascent = Region("The Final Ascent", world.player, world.multiworld)
    steel_steel = Region("Steel On Steel", world.player, world.multiworld)
    zero_seconds = Region("Zero Seconds to Midnight", world.player, world.multiworld)

    intermission.add_locations(location_table_intermission, ChronoGearLocation)
    dark_nest.add_locations(location_table_her_time_is_now, ChronoGearLocation)
    final_ascent.add_locations(location_table_the_final_ascent, ChronoGearLocation)
    steel_steel.add_locations(location_table_steel_on_steel, ChronoGearLocation)
    zero_seconds.add_locations(location_table_zero_seconds_to_midnight, ChronoGearLocation)

    regions = [intermission, dark_nest, final_ascent, steel_steel, zero_seconds]

    world.multiworld.regions += regions

def connect_time_regions(world: ChronoGearWorld) -> None:
    time_hub = world.get_region("Eternity Sanctum")
    time_shop_1 = world.get_region("Eternity Sanctum Shop Page 1")
    time_shop_2 = world.get_region("Eternity Sanctum Shop Page 2")
    time_shop_3 = world.get_region("Eternity Sanctum Shop Page 3")
    storming_the_sanctum = world.get_region("Storming the Sanctum")
    defending_the_sanctum = world.get_region("Defending the Sanctum")
    case_closed = world.get_region("Case Closed")
    top_of_bell_tower = world.get_region("The Top of Bell Tower")
    battle_of_bell_town = world.get_region("The Battle of Bell Town")
    polpol_express = world.get_region("The PolPol Express")
    gravity_of_time = world.get_region("The Gravity of Time")
    shattered_keep = world.get_region("The Shattered Keep")

    time_hub.connect(time_shop_1, "Hub to Time Shop 1", lambda state: state.has("Thread of Time - Time Page 1", world.player, 5))
    time_hub.connect(time_shop_2, "Hub to Time Shop 2", lambda state: state.has_all_counts({"Thread of Time - Time Page 2": 5, "Golden Gear": 7}, world.player))
    time_hub.connect(time_shop_3, "Hub to Time Shop 3", lambda state: state.has_all_counts({"Thread of Time - Time Page 3": 13, "Golden Gear": 32}, world.player))
    time_hub.connect(storming_the_sanctum, "Hub to Storming", lambda state: state.has("Storming the Sanctum", world.player))
    time_hub.connect(defending_the_sanctum, "Hub to Defending", lambda state: state.has("Defending the Sanctum", world.player))
    time_hub.connect(case_closed, "Hub to Case Closed", lambda state: state.has("Case Closed", world.player))
    time_hub.connect(top_of_bell_tower, "Hub to Bell Tower", lambda state: state.has("The Top of Bell Tower", world.player))
    time_hub.connect(battle_of_bell_town, "Hub to Battle of Bell Town", lambda state: state.has("The Battle of Bell Town", world.player))
    time_hub.connect(polpol_express, "Hub to PolPol Express", lambda state: state.has("The PolPol Express", world.player))
    time_hub.connect(gravity_of_time, "Hub to Gravity"), lambda state: state.has("The Gravity of Time", world.player)
    time_hub.connect(shattered_keep, "Hub to Shattered Keep", lambda state: state.has("The Shattered Keep", world.player))

def connect_nature_regions(world: ChronoGearWorld) -> None:
    time_hub = world.get_region("Eternity Sanctum") #This will get refactored once I can change starting hub
    nature_hub = world.get_region("Magic Resort")
    nature_shop = world.get_region("Magic Resort Shop")
    call_to_nature = world.get_region("Call to Nature")
    autumn_harvest = world.get_region("Autumn Harvest")
    wrath_of_nature = world.get_region("Wrath of Nature")
    floating_islands = world.get_region("The Floating Islands")
    riding_the_waves = world.get_region("Riding the Waves")
    beach_race = world.get_region("Chloe's Beach Race")
    rebuilding_atlantis = world.get_region("Rebuilding the Lost City")

    time_hub.connect(nature_hub, "Hub to Magic Resort", lambda state: state.has("Magic Resort", world.player))
    nature_hub.connect(nature_shop, "Hub to Nature Shop", lambda state: state.has("Thread of Time - Nature", world.player, 4))
    time_hub.connect(call_to_nature, "Hub to Call to Nature", lambda state: state.has("Call to Nature", world.player))
    time_hub.connect(autumn_harvest, "Hub to Autumn Harvest", lambda state: state.has("Autumn Harvest", world.player))
    time_hub.connect(wrath_of_nature, "Hub to Wrath of Nature", lambda state: state.has("Wrath of Nature", world.player))
    time_hub.connect(floating_islands, "Hub to Floating Islands", lambda state: state.has("The Floating Islands", world.player))
    time_hub.connect(riding_the_waves, "Hub to Riding the Waves", lambda state: state.has("Riding the Waves", world.player))
    time_hub.connect(beach_race, "Hub to Chloe's Beach Race", lambda state: state.has("Chloe's Beach Race", world.player))
    time_hub.connect(rebuilding_atlantis, "Hub to Rebuilding the Lost City", lambda state: state.has("Rebuilding the Lost City", world.player))

def connect_space_regions(world: ChronoGearWorld) -> None:
    time_hub = world.get_region("Eternity Sanctum") #This will get refactored once I can change starting hub
    space_hub = world.get_region("Spaceship ID")
    space_shop_1 = world.get_region("Spaceship ID Shop Page 1")
    space_shop_2 = world.get_region("Spaceship ID Shop Page 2")
    space_bake = world.get_region("The Great Space Bake")
    houshou_pirates = world.get_region("The Houshou Pirates")
    luknight_of_darkness = world.get_region("Luknight of Darkness")
    ganmo_grand_finale = world.get_region("Ganmo's Grand Finale")

    time_hub.connect(space_hub, "Hub to Starship ID", lambda state: state.has("Starship ID", world.player))
    space_hub.connect(space_shop_1, "Hub to Space Shop Page 1", lambda state: state.has("Thread of Time - Space Page 1", world.player, 4))
    space_hub.connect(space_shop_2, "Hub to Space Shop Page 2", lambda state: state.has_all_counts({"Thread of Time - Space Page 2": 4, "Golden Gear": 17}, world.player))
    time_hub.connect(space_bake, "Hub to The Great Space Bake", lambda state: state.has("The Great Space Bake", world.player))
    time_hub.connect(houshou_pirates, "Hub to The Houshou Pirates", lambda state: state.has("The Houshou Pirates", world.player))
    time_hub.connect(luknight_of_darkness, "Hub to Luknight of Darkness", lambda state: state.has("Luknight of Darkness", world.player))
    time_hub.connect(ganmo_grand_finale, "Hub to Ganmo's Grand Finale", lambda state: state.has("Ganmo's Grand Finale", world.player))

def connect_civ_regions(world: ChronoGearWorld) -> None:
    time_hub = world.get_region("Eternity Sanctum")
    civ_hub = world.get_region("Town Square")
    civ_shop = world.get_region("Town Square Shop")
    road_to_civ = world.get_region("The Road to Civilization")
    roboco_strikes_back = world.get_region("Roboco Strikes Back")
    path_of_memories = world.get_region("Path of Memories")
    cursed_lands = world.get_region("A Head Start")
    war_mind = world.get_region("The War Mind")

    time_hub.connect(civ_hub, "Hub to Town Square", lambda state: state.has("Town Square", world.player))
    civ_hub.connect(civ_shop, "Hub to Civ Shop", lambda state: state.has("Thread of Time - Civilization", world.player, 7))
    time_hub.connect(road_to_civ, "Hub to Road to Civilization", lambda state: state.has("The Road to Civilization", world.player))
    time_hub.connect(roboco_strikes_back, "Hub to Roboco Strikes Back", lambda state: state.has("Roboco Strikes Back", world.player))
    time_hub.connect(path_of_memories, "Hub to Path of Memories", lambda state: state.has("Path of Memories", world.player))
    time_hub.connect(cursed_lands, "Hub to A Head Start", lambda state: state.has("A Head Start", world.player))
    time_hub.connect(war_mind, "Hub to The War Mind", lambda state: state.has("The War Mind", world.player))

def connect_chaos_regions(world: ChronoGearWorld) -> None:
    time_hub = world.get_region("Eternity Sanctum")
    chaos_hub = world.get_region("The Funzone")
    chaos_shop = world.get_region("The Funzone Shop")
    caravan_of_darkness = world.get_region("Caravan of Darkness")
    overclocking_arcade = world.get_region("Overclocking the Arcade")
    song_light_dark = world.get_region("Song of Light and Darkness")
    kfp_games = world.get_region("The KFP Games")
    another_time_traveler = world.get_region("Another Time Traveler?")

    time_hub.connect(chaos_hub, "Hub to The Funzone", lambda state: state.has("The Funzone", world.player))
    chaos_hub.connect(chaos_shop, "Hub to Chaos Shop", lambda state: state.has("Thread of Time - Chaos", world.player, 9))
    time_hub.connect(caravan_of_darkness, "Hub to Caravan of Darkness", lambda state: state.has("Caravan of Darkness", world.player))
    time_hub.connect(overclocking_arcade, "Hub to Overclocking the Arcade", lambda state: state.has("Overclocking the Arcade", world.player))
    time_hub.connect(song_light_dark, "Hub to Song of Light and Darkness", lambda state: state.has("Song of Light and Darkness", world.player))
    time_hub.connect(kfp_games, "Hub to The KFP Games", lambda state: state.has("The KFP Games", world.player))
    time_hub.connect(another_time_traveler, "Hub to Another Time Traveler?", lambda state: state.has("Another Time Traveler?", world.player))

def connect_alter_regions(world: ChronoGearWorld) -> None:
    time_hub = world.get_region("Eternity Sanctum")
    alter_hub = world.get_region("The Bunker")
    solitude = world.get_region("Solitude")
    entropy = world.get_region("Entropy")
    ancient_ones = world.get_region("The Ancient Ones")
    gloom = world.get_region("Gloom")
    despair = world.get_region("Despair")
    hope = world.get_region("Hope")
    the_way_home = world.get_region("The Way Home")

    time_hub.connect(alter_hub, "Hub to The Bunker", lambda state: state.has("The Bunker", world.player))
    time_hub.connect(solitude, "Hub to Solitude", lambda state: state.has("Solitude", world.player))
    time_hub.connect(entropy, "Hub to Entropy", lambda state: state.has("Entropy", world.player))
    time_hub.connect(ancient_ones, "Hub to The Ancient Ones", lambda state: state.has("The Ancient Ones", world.player))
    time_hub.connect(gloom, "Hub to Gloom", lambda state: state.has("Gloom", world.player))
    time_hub.connect(despair, "Hub to Despair", lambda state: state.has("Despair", world.player))
    time_hub.connect(hope, "Hub to Hope", lambda state: state.has("Hope", world.player))
    time_hub.connect(the_way_home, "Hub to The Way Home", lambda state: state.has("The Way Home", world.player))

def connect_darkness_regions(world: ChronoGearWorld) -> None:
    time_hub = world.get_region("Eternity Sanctum")
    intermission = world.get_region("The Space Between Worlds")
    dark_nest = world.get_region("Her Time is Now")
    final_ascent = world.get_region("The Final Ascent")
    steel_steel = world.get_region("Steel On Steel")
    zero_seconds = world.get_region("Zero Seconds to Midnight")

    time_hub.connect(intermission, "Hub to The Space Between Worlds", lambda state: state.has("The Space Between Worlds", world.player))
    time_hub.connect(dark_nest, "Hub to Her Time is Now", lambda state: state.has("Her Time is Now", world.player))
    time_hub.connect(final_ascent, "Hub to The Final Ascent", lambda state: state.has("The Final Ascent", world.player))
    time_hub.connect(steel_steel, "Hub to Steel On Steel", lambda state: state.has("Steel On Steel", world.player))
    time_hub.connect(zero_seconds, "Hub to Zero Seconds to Midnight", lambda state: state.has("Zero Seconds to Midnight", world.player))