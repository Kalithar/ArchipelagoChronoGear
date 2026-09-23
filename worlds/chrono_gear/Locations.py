from __future__ import annotations

from typing import TYPE_CHECKING, Dict, NamedTuple

from BaseClasses import ItemClassification, Location

if TYPE_CHECKING:
    from . import ChronoGearWorld

class ChronoGearLocationData(NamedTuple):
    region: str
    id: int

class ChronoGearLocation(Location): 
    name = "Chrono Gear"

def get_location_by_region(region: str) -> Dict[str, ChronoGearLocationData]:
    return {name: data for name, data in location_table.items() if data.region == region}

location_table: Dict[str, ChronoGearLocationData] = {
    #Starting Items

    "Start Game - First CD": ChronoGearLocationData("World Map", 100201),
    "Start Game - Second CD": ChronoGearLocationData("World Map", 100202),
    "Start Game - Third CD": ChronoGearLocationData("World Map", 100203),
    
    #"Start Game - Storming the Sanctum Unlock": ChronoGearLocationData("World Map", 110000),
    
    #World of Time

    "World of Time - Unlock The Battle of Bell Town": ChronoGearLocationData("World of Time", 121000),
    
    # Eternity Sanctum
    "Eternity Sanctum - Golden Gear from Council Meeting": ChronoGearLocationData("Eternity Sanctum", 100100),
    "Eternity Sanctum - Golden Gear from Secret Sanctum": ChronoGearLocationData("Eternity Sanctum", 101100),
    "Eternity Sanctum - Thread of Time near shop": ChronoGearLocationData("Eternity Sanctum", 100301),
    "Eternity Sanctum - Thread of Time on far right": ChronoGearLocationData("Eternity Sanctum", 100331),
    "Eternity Sanctum - Right CD after Steel on Steel": ChronoGearLocationData("Eternity Sanctum", 100282),
    "Eternity Sanctum - Left CD after Steel on Steel": ChronoGearLocationData("Eternity Sanctum", 100288),
    "Eternity Sanctum - Right CD after Zero Seconds to Midnight": ChronoGearLocationData("Eternity Sanctum", 100283),
    "Eternity Sanctum - Left CD after Zero Seconds to Midnight": ChronoGearLocationData("Eternity Sanctum", 100284),
    "Eternity Sanctum - CD near bookcase": ChronoGearLocationData("Eternity Sanctum", 100286),

    # Eternity Sanctum Shop
    "Eternity Sanctum Shop Page 1 - Purchase first CD": ChronoGearLocationData("Eternity Sanctum Shop Page 1", 1000),
    "Eternity Sanctum Shop Page 1 - Purchase second CD": ChronoGearLocationData("Eternity Sanctum Shop Page 1", 1001),
    "Eternity Sanctum Shop Page 1 - Purchase third CD": ChronoGearLocationData("Eternity Sanctum Shop Page 1", 1002),
    "Eternity Sanctum Shop Page 1 - Purchase fourth CD": ChronoGearLocationData("Eternity Sanctum Shop Page 1", 1003),
    "Eternity Sanctum Shop Page 1 - Purchase border art": ChronoGearLocationData("Eternity Sanctum Shop Page 1", 1004),

    "Eternity Sanctum Shop Page 2 - Purchase first CD": ChronoGearLocationData("Eternity Sanctum Shop Page 2", 1100),
    "Eternity Sanctum Shop Page 2 - Purchase second CD": ChronoGearLocationData("Eternity Sanctum Shop Page 2", 1101),
    "Eternity Sanctum Shop Page 2 - Purchase third CD": ChronoGearLocationData("Eternity Sanctum Shop Page 2", 1102),
    "Eternity Sanctum Shop Page 2 - Purchase first border art": ChronoGearLocationData("Eternity Sanctum Shop Page 2", 1103),
    "Eternity Sanctum Shop Page 2 - Purchase second border art": ChronoGearLocationData("Eternity Sanctum Shop Page 2", 1104),

    "Eternity Sanctum Shop Page 3 - Purchase border art": ChronoGearLocationData("Eternity Sanctum Shop Page 3", 1200),
    "Eternity Sanctum Shop Page 3 - Purchase first CD": ChronoGearLocationData("Eternity Sanctum Shop Page 3", 1201),
    "Eternity Sanctum Shop Page 3 - Purchase second CD": ChronoGearLocationData("Eternity Sanctum Shop Page 3", 1202),
    "Eternity Sanctum Shop Page 3 - Purchase third CD": ChronoGearLocationData("Eternity Sanctum Shop Page 3", 1203),
    "Eternity Sanctum Shop Page 3 - Purchase fourth CD": ChronoGearLocationData("Eternity Sanctum Shop Page 3", 1204),
    "Eternity Sanctum Shop Page 3 - Purchase fifth CD": ChronoGearLocationData("Eternity Sanctum Shop Page 3", 1205),
    "Eternity Sanctum Shop Page 3 - Purchase sixth CD": ChronoGearLocationData("Eternity Sanctum Shop Page 3", 1206),
    "Eternity Sanctum Shop Page 3 - Purchase seventh CD": ChronoGearLocationData("Eternity Sanctum Shop Page 3", 1207),
    "Eternity Sanctum Shop Page 3 - Purchase eighth CD": ChronoGearLocationData("Eternity Sanctum Shop Page 3", 1208),
    "Eternity Sanctum Shop Page 3 - Purchase ninth CD": ChronoGearLocationData("Eternity Sanctum Shop Page 3", 1209),
    "Eternity Sanctum Shop Page 3 - Purchase tenth CD": ChronoGearLocationData("Eternity Sanctum Shop Page 3", 1210),
    "Eternity Sanctum Shop Page 3 - Purchase eleventh CD": ChronoGearLocationData("Eternity Sanctum Shop Page 3", 1211),
    "Eternity Sanctum Shop Page 3 - Purchase twelfth CD": ChronoGearLocationData("Eternity Sanctum Shop Page 3", 1212),

    #Doorway to Nowhere

    "Storming the Sanctum - Unlock The Top of Bell Tower": ChronoGearLocationData("Storming the Sanctum", 120000),
    "Storming the Sanctum - Unlock Eternity Sanctum": ChronoGearLocationData("Storming the Sanctum", 10),
    "Storming the Sanctum - Golden Gear": ChronoGearLocationData("Storming the Sanctum", 110100),
    "Storming the Sanctum - CD before first checkpoint": ChronoGearLocationData("Storming the Sanctum", 110208),
    "Storming the Sanctum - CD below giant moving platform": ChronoGearLocationData("Storming the Sanctum", 110207),

    "World Map - Unlock Case Closed": ChronoGearLocationData("World Map", 111000),
    "Case Closed - Unlock Defending the Sanctum": ChronoGearLocationData("Case Closed", 112000),

    "Defending the Sanctum - Alter Timeline Unlock": ChronoGearLocationData("Defending the Sanctum", 7),
    "Defending the Sanctum - Unlock Solitude": ChronoGearLocationData("Defending the Sanctum", 710000),
    "Defending the Sanctum - Golden Gear": ChronoGearLocationData("Defending the Sanctum", 112100),
    "Defending the Sanctum - CD above first pendulum": ChronoGearLocationData("Defending the Sanctum", 112263),
    "Defending the Sanctum - Thread of Time before Dark Impact": ChronoGearLocationData("Defending the Sanctum", 112328),
    "Defending the Sanctum - Thread of Time above last pendulum": ChronoGearLocationData("Defending the Sanctum", 112341),

    #Bell Town

    "The Top of Bell Tower - Unlock The PolPol Express": ChronoGearLocationData("The Top of Bell Tower", 130000),
    "The Top of Bell Tower - Unlock The Gravity of Time": ChronoGearLocationData("The Top of Bell Tower", 140000),
    "The Top of Bell Tower - Unlock The Shattered Keep": ChronoGearLocationData("The Top of Bell Tower", 150000),
    "The Top of Bell Tower - Golden Gear": ChronoGearLocationData("The Top of Bell Tower", 120100),
    "The Top of Bell Tower - CD above elevator to Underworks": ChronoGearLocationData("The Top of Bell Tower", 120204),
    "The Top of Bell Tower - CD in Underworks": ChronoGearLocationData("The Top of Bell Tower", 120213),
    "The Top of Bell Tower - CD past Kroniephone and moving platform": ChronoGearLocationData("The Top of Bell Tower", 120212),
    "The Top of Bell Tower - Thread of Time above rolling platforms": ChronoGearLocationData("The Top of Bell Tower", 120370),

    "The Battle of Bell Town - Golden Gear": ChronoGearLocationData("The Battle of Bell Town", 121100),
    "The Battle of Bell Town - Unlock Call to Nature": ChronoGearLocationData("The Battle of Bell Town", 210000),
    "The Battle of Bell Town - Unlock The Great Space Bake": ChronoGearLocationData("The Battle of Bell Town", 310000),

    #Carnival Railway

    "The PolPol Express - Golden Gear": ChronoGearLocationData("The PolPol Express", 130100),
    "The PolPol Express - CD from freeing Kronies": ChronoGearLocationData("The PolPol Express", 130215),
    "The PolPol Express - CD before final room": ChronoGearLocationData("The PolPol Express", 130214),
    "The PolPol Express - Thread of Time from puzzle room right of warp gate": ChronoGearLocationData("The PolPol Express", 130369),
    "The PolPol Express - Thread of Time at top of large acrobatics room": ChronoGearLocationData("The PolPol Express", 130371),

    #The Sands of Time

    "The Gravity of Time - Golden Gear": ChronoGearLocationData("The Gravity of Time", 140100),
    "The Gravity of Time - CD above first warp gate exit": ChronoGearLocationData("The Gravity of Time", 140216),
    "The Gravity of Time - CD at top of second section": ChronoGearLocationData("The Gravity of Time", 140206),
    "The Gravity of Time - Thread of Time at end of second section": ChronoGearLocationData("The Gravity of Time", 140304),

    #Jewel Cyclone

    "The Shattered Keep - Golden Gear": ChronoGearLocationData("The Shattered Keep", 150100),
    "The Shattered Keep - CD above third checkpoint": ChronoGearLocationData("The Shattered Keep", 150209),
    "The Shattered Keep - CD after first checkpoint": ChronoGearLocationData("The Shattered Keep", 150217),
    "The Shattered Keep - Thread of Time on top path backtrack before boss": ChronoGearLocationData("The Shattered Keep", 150305),

    #World of Nature

    "World of Nature - Unlock Rebuilding the Lost City": ChronoGearLocationData("World of Nature", 240000),

    # Magic Resort

    "Magic Resort - Golden Gear": ChronoGearLocationData("Magic Resort", 200100),
    "Magic Resort - Thread of Time for catching Trout": ChronoGearLocationData("Magic Resort", 200360),
    "Magic Resort - Thread of Time for catching Salmon": ChronoGearLocationData("Magic Resort", 200361),
    "Magic Resort - Thread of Time for catching Carp": ChronoGearLocationData("Magic Resort", 200362),
    "Magic Resort - Thread of Time for catching Eel": ChronoGearLocationData("Magic Resort", 200363),
    "Magic Resort - Thread of Time for catching Dace": ChronoGearLocationData("Magic Resort", 200364),
    "Magic Resort - Thread of Time for catching Pike": ChronoGearLocationData("Magic Resort", 200365),
    "Magic Resort - Thread of Time for catching Bream": ChronoGearLocationData("Magic Resort", 200366),

    "Magic Resort Shop - Purchase top border art": ChronoGearLocationData("Magic Resort Shop", 2000),
    "Magic Resort Shop - Purchase top CD": ChronoGearLocationData("Magic Resort Shop", 2001),
    "Magic Resort Shop - Purchase bottom CD": ChronoGearLocationData("Magic Resort Shop", 2002),
    "Magic Resort Shop - Purchase bottom border art": ChronoGearLocationData("Magic Resort Shop", 2003),

    #The World Tree

    "Call to Nature - Unlock The Floating Islands": ChronoGearLocationData("Call to Nature", 220000),
    "Call to Nature - Unlock Riding the Waves": ChronoGearLocationData("Call to Nature", 230000),
    "Call to Nature - Unlock Magic Resort": ChronoGearLocationData("Call to Nature", 20),
    "Call to Nature - Golden Gear": ChronoGearLocationData("Call to Nature", 210100),
    "Call to Nature - CD in first side room": ChronoGearLocationData("Call to Nature", 210232),
    "Call to Nature - CD in summer hidden room": ChronoGearLocationData("Call to Nature", 210233),
    "Call to Nature - Thread of Time at top of tree trunk": ChronoGearLocationData("Call to Nature", 210306),

    "Autumn Harvest - Golden Gear": ChronoGearLocationData("Autumn Harvest", 211100),
    "Autumn Harvest - CD in autumn side room halfway up tree": ChronoGearLocationData("Autumn Harvest", 211234),
    "Autumn Harvest - CD in winter pointed to by haste notes": ChronoGearLocationData("Autumn Harvest", 211235),
    "Autumn Harvest - Thread of Time in autumn hidden room": ChronoGearLocationData("Autumn Harvest", 211307),
    "Autumn Harvest - Thread of Time above second winter warp trunk": ChronoGearLocationData("Autumn Harvest", 211343),

    #Doesn't directly unlock a level, but involved in Chaos and Civ unlock, as well as intermission
    "Wrath of Nature - Golden Gear": ChronoGearLocationData("Wrath of Nature", 212100),
    "Wrath of Nature - CD before first checkpoint": ChronoGearLocationData("Wrath of Nature", 212242),
    "Wrath of Nature - Thread of Time before first water sphere": ChronoGearLocationData("Wrath of Nature", 212327),

    #Sky Tops

    "The Floating Islands - Golden Gear": ChronoGearLocationData("The Floating Islands", 220100),
    "The Floating Islands - CD in cave with flower": ChronoGearLocationData("The Floating Islands", 220238),
    "The Floating Islands - Thread of Time before second checkpoint after second warp gate": ChronoGearLocationData("The Floating Islands", 220325),
    "The Floating Islands - Thread of Time before Golden Gear": ChronoGearLocationData("The Floating Islands", 220340),

    #Tidal Camp

    "Riding the Waves - Golden Gear": ChronoGearLocationData("Riding the Waves", 230100),
    "Riding the Waves - CD above crabs in last bumper section": ChronoGearLocationData("Riding the Waves", 230239),
    "Riding the Waves - Thread of Time underwater after first checkpoint": ChronoGearLocationData("Riding the Waves", 230308),
    "Riding the Waves - Thread of Time above third checkpoint": ChronoGearLocationData("Riding the Waves", 230309),

    "Chloe's Beach Race - Unlock Wrath of Nature": ChronoGearLocationData("Chloe's Beach Race", 212000),
    "Chloe's Beach Race - Golden Gear": ChronoGearLocationData("Chloe's Beach Race", 231100),

    #Depths of Atlatins

    "Rebuilding the Lost City - Unlock Chloe's Beach Race": ChronoGearLocationData("Rebuilding the Lost City", 231000),
    "Rebuilding the Lost City - Golden Gear": ChronoGearLocationData("Rebuilding the Lost City", 240100),
    "Rebuilding the Lost City - CD on side path at beginning of ruins": ChronoGearLocationData("Rebuilding the Lost City", 240241),
    "Rebuilding the Lost City - Thread of Time behind lower eel after first checkpoint": ChronoGearLocationData("Rebuilding the Lost City", 240310),
    "Rebuilding the Lost City - Thread of Time locked by optional switch in second ruins section": ChronoGearLocationData("Rebuilding the Lost City", 240311),

    #World of Space

    #Space Hub

    "Starship ID - Golden Gear": ChronoGearLocationData("Starship ID", 300100),
    "Starship ID - Thread of Time on top of ship": ChronoGearLocationData("Starship ID", 300342),
    "Starship ID - CD in generator room": ChronoGearLocationData("Starship ID", 300223),

    "Starship ID Shop Page 1 - Purchase CD": ChronoGearLocationData("Starship ID Shop Page 1", 3000),
    "Starship ID Shop Page 1 - Purchase first border art": ChronoGearLocationData("Starship ID Shop Page 1", 3001),
    "Starship ID Shop Page 1 - Purchase second border art": ChronoGearLocationData("Starship ID Shop Page 1", 3002),
    "Starship ID Shop Page 1 - Purchase third border art": ChronoGearLocationData("Starship ID Shop Page 1", 3003),

    "Starship ID Shop Page 2 - Purchase first CD": ChronoGearLocationData("Starship ID Shop Page 2", 3100),
    "Starship ID Shop Page 2 - Purchase second CD": ChronoGearLocationData("Starship ID Shop Page 2", 3101),
    "Starship ID Shop Page 2 - Purchase first border art": ChronoGearLocationData("Starship ID Shop Page 2", 3102),
    "Starship ID Shop Page 2 - Purchase second border art": ChronoGearLocationData("Starship ID Shop Page 2", 3103),

    #Galaxy Gourmet

    "The Great Space Bake - Unlock Starship ID": ChronoGearLocationData("The Great Space Bake", 30),
    "The Great Space Bake - Unlock The Houshou Pirates": ChronoGearLocationData("The Great Space Bake", 320000),
    "The Great Space Bake - Golden Gear": ChronoGearLocationData("The Great Space Bake", 310100),
    "The Great Space Bake - CD left of warp gate after first checkpoint": ChronoGearLocationData("The Great Space Bake", 310221),
    "The Great Space Bake - Thread of Time under island after second checkpoint": ChronoGearLocationData("The Great Space Bake", 310326),

    #Battleship Aquamarine

    "The Houshou Pirates - Unlock Luknight of Darkness": ChronoGearLocationData("The Houshou Pirates", 330000),
    "The Houshou Pirates - Golden Gear": ChronoGearLocationData("The Houshou Pirates", 320100),
    "The Houshou Pirates - CD below first cannons": ChronoGearLocationData("The Houshou Pirates", 320224),
    "The Houshou Pirates - CD before vertical cannons": ChronoGearLocationData("The Houshou Pirates", 320226),
    "The Houshou Pirates - CD guarded by Root Beer Walker": ChronoGearLocationData("The Houshou Pirates", 320225),

    #Hoshinova Castle

    "Luknight of Darkness - Unlock Ganmo's Grand Finale": ChronoGearLocationData("Luknight of Darkness", 331000),
    "Luknight of Darkness - Golden Gear": ChronoGearLocationData("Luknight of Darkness", 330100),
    "Luknight of Darkness - CD left of second checkpoint": ChronoGearLocationData("Luknight of Darkness", 330229),
    "Luknight of Darkness - CD from defeating Armored Rangoon": ChronoGearLocationData("Luknight of Darkness", 330230),
    "Luknight of Darkness - Thread of Time in underground section": ChronoGearLocationData("Luknight of Darkness", 330350),
    "Luknight of Darkness - Thread of Time on right split path": ChronoGearLocationData("Luknight of Darkness", 330351),

    #Doesn't directly unlock a level, but involved in Chaos and Civ unlock, as well as intermission
    "Ganmo's Grand Finale - Golden Gear": ChronoGearLocationData("Ganmo's Grand Finale", 331100),

    # Civilization Hub

    "Town Square - Golden Gear": ChronoGearLocationData("Town Square", 400100),
    "Town Square - Thread of Time from powerwashing": ChronoGearLocationData("Town Square", 400302),
    "Town Square - Thread of Time on top of house": ChronoGearLocationData("Town Square", 400303),
    "Town Square - CD in powerwashing room": ChronoGearLocationData("Town Square", 400248),
    "Town Square - CD from fixing Roboco": ChronoGearLocationData("Town Square", 400254),

    "Town Square Shop - Purchase first border art": ChronoGearLocationData("Town Square Shop", 4000),
    "Town Square Shop - Purchase first CD": ChronoGearLocationData("Town Square Shop", 4001),
    "Town Square Shop - Purchase second border art": ChronoGearLocationData("Town Square Shop", 4002),
    "Town Square Shop - Purchase second CD": ChronoGearLocationData("Town Square Shop", 4003),
    "Town Square Shop - Purchase third border art": ChronoGearLocationData("Town Square Shop", 4004),
    "Town Square Shop - Purchase third CD": ChronoGearLocationData("Town Square Shop", 4005),
    "Town Square Shop - Purchase fourth CD": ChronoGearLocationData("Town Square Shop", 4006),

    #Castle Road

    "The Road to Civilization - Unlock Town Square": ChronoGearLocationData("The Road to Civilization", 40),
    "The Road to Civilization - Unlock Path of Memories": ChronoGearLocationData("The Road to Civilization", 420000),
    "The Road to Civilization - Golden Gear": ChronoGearLocationData("The Road to Civilization", 410100),
    "The Road to Civilization - CD at top of tall tower with Mumei glider": ChronoGearLocationData("The Road to Civilization", 410249),
    "The Road to Civilization - Thread of Time left of first warp gate exit": ChronoGearLocationData("The Road to Civilization", 410312),
    "The Road to Civilization - Thread of Time underwater before tall tower with Mumei glider": ChronoGearLocationData("The Road to Civilization", 410373),

    #Involved in Case Closed unlock
    "Roboco Strikes Back - Golden Gear": ChronoGearLocationData("Roboco Strikes Back", 411100),

    #The Maze

    "Path of Memories - Unlock A Head Start": ChronoGearLocationData("Path of Memories", 430000),
    "Path of Memories - Golden Gear": ChronoGearLocationData("Path of Memories", 420100),
    "Path of Memories - CD in left section above WhoMan": ChronoGearLocationData("Path of Memories", 420251),
    "Path of Memories - Thread of Time in top rotating wall section": ChronoGearLocationData("Path of Memories", 420317),
    "Path of Memories - Thread of Time underwater in bottom right section": ChronoGearLocationData("Path of Memories", 420318),
    "Path of Memories - Thread of Time in top middle section near WhoMan": ChronoGearLocationData("Path of Memories", 420374),

    #Cursed Lands

    "A Head Start - Unlock The War Mind": ChronoGearLocationData("A Head Start", 440000),
    "A Head Start - Golden Gear": ChronoGearLocationData("A Head Start", 430100),
    "A Head Start - CD left of pit before fourth checkpoint": ChronoGearLocationData("A Head Start", 430252),
    "A Head Start - Thread of Time blocked by flame blocks after Chesseract": ChronoGearLocationData("A Head Start", 430313),

    #Magitech Forge

    "The War Mind - Unlock Roboco Strikes Back": ChronoGearLocationData("The War Mind", 411000),
    "The War Mind - Golden Gear": ChronoGearLocationData("The War Mind", 440100),
    "The War Mind - CD in upper room with Bounce Crates after first warp gate": ChronoGearLocationData("The War Mind", 440253),
    "The War Mind - Thread of Time underneath crates by Dark Impact": ChronoGearLocationData("The War Mind", 440314),
    "The War Mind - Thread of Time guarded by 4 Goblin Roses": ChronoGearLocationData("The War Mind", 440315),
    "The War Mind - Thread of Time above first checkpoint": ChronoGearLocationData("The War Mind", 440339),

    # Chaos Hub

    "The Funzone - CD on rollercoaster": ChronoGearLocationData("The Funzone", 500257),

    "The Funzone Shop - Purchase first CD": ChronoGearLocationData("The Funzone Shop", 5000),
    "The Funzone Shop - Purchase second CD": ChronoGearLocationData("The Funzone Shop", 5001),
    "The Funzone Shop - Purchase third CD": ChronoGearLocationData("The Funzone Shop", 5002),
    "The Funzone Shop - Purchase fourth CD": ChronoGearLocationData("The Funzone Shop", 5003),
    "The Funzone Shop - Purchase fifth CD": ChronoGearLocationData("The Funzone Shop", 5004),
    "The Funzone Shop - Purchase sixth CD": ChronoGearLocationData("The Funzone Shop", 5005),
    "The Funzone Shop - Purchase first border art": ChronoGearLocationData("The Funzone Shop", 5006),
    "The Funzone Shop - Purchase second border art": ChronoGearLocationData("The Funzone Shop", 5007),
    "The Funzone Shop - Purchase third border art": ChronoGearLocationData("The Funzone Shop", 5008),

    #Highway of Dreams

    "Caravan of Darkness - Unlock The Funzone": ChronoGearLocationData("Caravan of Darkness", 50),
    "Caravan of Darkness - Unlock Overclocking the Arcade": ChronoGearLocationData("Caravan of Darkness", 520000),
    "Caravan of Darkness - Golden Gear": ChronoGearLocationData("Caravan of Darkness", 510100),
    "Caravan of Darkness - CD above warp gate into upside down section": ChronoGearLocationData("Caravan of Darkness", 510256),
    "Caravan of Darkness - Thread of Time underneath crane in long descent": ChronoGearLocationData("Caravan of Darkness", 510316),
    "Caravan of Darkness - Thread of Time above rails over pit": ChronoGearLocationData("Caravan of Darkness", 510330),

    #Ducky God Arcade

    "Overclocking the Arcade - Unlock Song of Light and Darkness": ChronoGearLocationData("Overclocking the Arcade", 530000),
    "Overclocking the Arcade - Golden Gear": ChronoGearLocationData("Overclocking the Arcade", 520100),
    "Overclocking the Arcade - CD through arcade screen before fourth checkpoint": ChronoGearLocationData("Overclocking the Arcade", 520259),
    "Overclocking the Arcade - Thread of Time though arcade screen before Golden Gear": ChronoGearLocationData("Overclocking the Arcade", 520332),

    #Symphonic Gallery

    "Song of Light and Darkness - Unlock The KFP Games": ChronoGearLocationData("Song of Light and Darkness", 540000),
    "Song of Light and Darkness - Golden Gear": ChronoGearLocationData("Song of Light and Darkness", 530100),
    "Song of Light and Darkness - CD in top right split path": ChronoGearLocationData("Song of Light and Darkness", 530260),
    "Song of Light and Darkness - Thread of Time in bottom right path": ChronoGearLocationData("Song of Light and Darkness", 530319),
    "Song of Light and Darkness - Thread of Time above Hydra Block in final climb": ChronoGearLocationData("Song of Light and Darkness", 530334),

    #KFP Stadium

    "The KFP Games - Unlock Another Time Traveler?": ChronoGearLocationData("The KFP Games", 541000),
    "The KFP Games - Golden Gear": ChronoGearLocationData("The KFP Games", 540100),
    "The KFP Games - CD at top of backtrack in second stage": ChronoGearLocationData("The KFP Games", 540262),
    "The KFP Games - CD while backtracking in fourth stage": ChronoGearLocationData("The KFP Games", 540261),
    "The KFP Games - Thread of Time before flame in second stage": ChronoGearLocationData("The KFP Games", 540320),

    #Another Time Traveler?
    #No item checks, but has an event check to contribute to Case Closed unlock

    #Alter Timeline

    "Solitude - Unlock The Bunker": ChronoGearLocationData("Solitude", 70),
    "Solitude - Unlock Entropy": ChronoGearLocationData("Solitude", 720000),
    "Solitude - Laplus' Shackle": ChronoGearLocationData("Solitude", 710100),

    "Entropy - Unlock The Ancient Ones": ChronoGearLocationData("Entropy", 711000),
    "Entropy - Laplus' Shackle": ChronoGearLocationData("Entropy", 720100),

    "The Ancient Ones - Unlock Gloom": ChronoGearLocationData("The Ancient Ones", 730000),

    "Gloom - Unlock Despair": ChronoGearLocationData("Gloom", 740000),
    "Gloom - Laplus' Shackle": ChronoGearLocationData("Gloom", 730100),

    "Despair - Unlock Hope": ChronoGearLocationData("Despair", 750000),
    "Despair - Laplus' Shackle": ChronoGearLocationData("Despair", 740100), #Not an actual check the game gives you

    "Hope - Unlock The Way Home": ChronoGearLocationData("Hope", 751000),
    "Hope - Laplus' Shackle": ChronoGearLocationData("Hope", 750100),

    
    "The Way Home - Unlock Her Time is Now": ChronoGearLocationData("The Way Home", 620000), 
    "The Way Home - Chrono Gear": ChronoGearLocationData("The Way Home", 751400),

    #World of Darkness

    "Intermission - Unlock The Space Between Worlds": ChronoGearLocationData("The Space Between Worlds", 610000),
    #Where these actually end up depend on settings, but they're in the intermission in vanilla

    "Intermission - Unlock Caravan of Darkness": ChronoGearLocationData("Intermission", 510000),
    "Intermission - Unlock The Road to Civilization": ChronoGearLocationData("Intermission", 410000),

    "Her Time is Now - Unlock The Final Ascent": ChronoGearLocationData("Her Time is Now", 630000),
    "Her Time is Now - Golden Gear": ChronoGearLocationData("Her Time is Now", 620100),
    "Her Time is Now - CD at end of first ground section": ChronoGearLocationData("Her Time is Now", 620275),
    "Her Time is Now - Thread of Time above Defense Core": ChronoGearLocationData("Her Time is Now", 620322),
    "Her Time is Now - Thread of Time on pillar before gate": ChronoGearLocationData("Her Time is Now", 620323),
    "Her Time is Now - Thread of Time left of first moving lasers": ChronoGearLocationData("Her Time is Now", 620324),
    "Her Time is Now - Thread of Time right of first moving lasers": ChronoGearLocationData("Her Time is Now", 620321),

    "The Final Ascent - Unlock Steel on Steel": ChronoGearLocationData("The Final Ascent", 631000),
    "The Final Ascent - Golden Gear": ChronoGearLocationData("The Final Ascent", 630100),
    "The Final Ascent - CD in ruined room near lobby": ChronoGearLocationData("The Final Ascent", 630276),
    "The Final Ascent - CD covered by shadow barrier": ChronoGearLocationData("The Final Ascent", 630277),
    "The Final Ascent - CD in large room with Arc Sentinels": ChronoGearLocationData("The Final Ascent", 630278),
    "The Final Ascent - CD behind key locked door": ChronoGearLocationData("The Final Ascent", 630279),
    "The Final Ascent - CD above ruined portal": ChronoGearLocationData("The Final Ascent", 630280),
    "The Final Ascent - CD at top of frozen time section with Shadow Armor": ChronoGearLocationData("The Final Ascent", 630281),

    "Steel on Steel - Unlock Zero Seconds to Midnight": ChronoGearLocationData("Steel on Steel", 632000),

}

event_location_table: Dict[str, ChronoGearLocationData] = {
    "Zero Seconds to Midnight - Clear Level": ChronoGearLocationData("Zero Seconds to Midnight", None),
    "Another Time Traveler? - Clear Level": ChronoGearLocationData("Another Time Traveler?", None),
}

world_unlock_location_table: Dict[str, ChronoGearLocationData] = {
    #"Start Game - Unlock World of Time": ChronoGearLocationData("World Map", 1),
    "The Battle of Bell Town - Unlock World of Nature": ChronoGearLocationData("The Battle of Bell Town", 2),
    "The Battle of Bell Town - Unlock World of Space": ChronoGearLocationData("The Battle of Bell Town", 3),
    "The Way Home - Unlock World of Darkness": ChronoGearLocationData("The Way Home", 6),
    "Intermission - Unlock World of Chaos": ChronoGearLocationData("Intermission", 5),
    "Intermission - Unlock World of Civilization": ChronoGearLocationData("Intermission", 4),
}

stage_score_location_table: Dict[str, ChronoGearLocationData] = {
    "Storming the Sanctum - 100 Notes Score": ChronoGearLocationData("Storming the Sanctum", 110500),
    "Storming the Sanctum - 100 Time Score": ChronoGearLocationData("Storming the Sanctum", 110501),
    "Storming the Sanctum - 100 Damage Taken Score": ChronoGearLocationData("Storming the Sanctum", 110502),
    
    "Case Closed - 100 Time Score": ChronoGearLocationData("Case Closed", 111501),
    "Case Closed - 100 Damage Taken Score": ChronoGearLocationData("Case Closed", 111502),

    "Defending the Sanctum - 100 Notes Score": ChronoGearLocationData("Defending the Sanctum", 112500),
    "Defending the Sanctum - 100 Time Score": ChronoGearLocationData("Defending the Sanctum", 112501),
    "Defending the Sanctum - 100 Damage Taken Score": ChronoGearLocationData("Defending the Sanctum", 112502),
    
    "The Top of Bell Tower - 100 Notes Score": ChronoGearLocationData("The Top of Bell Tower", 120500),
    "The Top of Bell Tower - 100 Time Score": ChronoGearLocationData("The Top of Bell Tower", 120501),
    "The Top of Bell Tower - 100 Damage Taken Score": ChronoGearLocationData("The Top of Bell Tower", 120502),

    "The Battle of Bell Town - 100 Time Score": ChronoGearLocationData("The Battle of Bell Town", 121501),
    "The Battle of Bell Town - 100 Damage Taken Score": ChronoGearLocationData("The Battle of Bell Town", 121502),

    "The PolPol Express - 100 Notes Score": ChronoGearLocationData("The PolPol Express", 130500),
    "The PolPol Express - 100 Time Score": ChronoGearLocationData("The PolPol Express", 130501),
    "The PolPol Express - 100 Damage Taken Score": ChronoGearLocationData("The PolPol Express", 130502),

    "The Gravity of Time - 100 Notes Score": ChronoGearLocationData("The Gravity of Time", 140500),
    "The Gravity of Time - 100 Time Score": ChronoGearLocationData("The Gravity of Time", 140501),
    "The Gravity of Time - 100 Damage Taken Score": ChronoGearLocationData("The Gravity of Time", 140502),

    "The Shattered Keep - 100 Notes Score": ChronoGearLocationData("The Shattered Keep", 150500),
    "The Shattered Keep - 100 Time Score": ChronoGearLocationData("The Shattered Keep", 150501),
    "The Shattered Keep - 100 Damage Taken Score": ChronoGearLocationData("The Shattered Keep", 150502),

    "Call to Nature - 100 Notes Score": ChronoGearLocationData("Call to Nature", 210500),
    "Call to Nature - 100 Time Score": ChronoGearLocationData("Call to Nature", 210501),
    "Call to Nature - 100 Damage Taken Score": ChronoGearLocationData("Call to Nature", 210502),

    "Autumn Harvest - 100 Notes Score": ChronoGearLocationData("Autumn Harvest", 211500),
    "Autumn Harvest - 100 Time Score": ChronoGearLocationData("Autumn Harvest", 211501),
    "Autumn Harvest - 100 Damage Taken Score": ChronoGearLocationData("Autumn Harvest", 211502),

    "Wrath of Nature - 100 Time Score": ChronoGearLocationData("Wrath of Nature", 212501),
    "Wrath of Nature - 100 Damage Taken Score": ChronoGearLocationData("Wrath of Nature", 212502),

    "The Floating Islands - 100 Notes Score": ChronoGearLocationData("The Floating Islands", 220500),
    "The Floating Islands - 100 Time Score": ChronoGearLocationData("The Floating Islands", 220501),
    "The Floating Islands - 100 Damage Taken Score": ChronoGearLocationData("The Floating Islands", 220502),

    "Riding the Waves - 100 Notes Score": ChronoGearLocationData("Riding the Waves", 230500),
    "Riding the Waves - 100 Time Score": ChronoGearLocationData("Riding the Waves", 230501),
    "Riding the Waves - 100 Damage Taken Score": ChronoGearLocationData("Riding the Waves", 230502),

    "Chloe's Beach Race - 100 Time Score": ChronoGearLocationData("Chloe's Beach Race", 231501),
    "Chloe's Beach Race - 100 Damage Taken Score": ChronoGearLocationData("Chloe's Beach Race", 231502),

    "Rebuilding the Lost City - 100 Notes Score": ChronoGearLocationData("Rebuilding the Lost City", 240500),
    "Rebuilding the Lost City - 100 Time Score": ChronoGearLocationData("Rebuilding the Lost City", 240501),
    "Rebuilding the Lost City - 100 Damage Taken Score": ChronoGearLocationData("Rebuilding the Lost City", 240502),

    "The Great Space Bake - 100 Notes Score": ChronoGearLocationData("The Great Space Bake", 310500),
    "The Great Space Bake - 100 Time Score": ChronoGearLocationData("The Great Space Bake", 310501),
    "The Great Space Bake - 100 Damage Taken Score": ChronoGearLocationData("The Great Space Bake", 310502),

    "The Houshou Pirates - 100 Notes Score": ChronoGearLocationData("The Houshou Pirates", 320500),
    "The Houshou Pirates - 100 Time Score": ChronoGearLocationData("The Houshou Pirates", 320501),
    "The Houshou Pirates - 100 Damage Taken Score": ChronoGearLocationData("The Houshou Pirates", 320502),

    "Luknight of Darkness - 100 Notes Score": ChronoGearLocationData("Luknight of Darkness", 330500),
    "Luknight of Darkness - 100 Time Score": ChronoGearLocationData("Luknight of Darkness", 330501),
    "Luknight of Darkness - 100 Damage Taken Score": ChronoGearLocationData("Luknight of Darkness", 330502),

    "Ganmo's Grand Finale - 100 Notes Score": ChronoGearLocationData("Ganmo's Grand Finale", 331500),
    "Ganmo's Grand Finale - 100 Time Score": ChronoGearLocationData("Ganmo's Grand Finale", 331501),
    "Ganmo's Grand Finale - 100 Damage Taken Score": ChronoGearLocationData("Ganmo's Grand Finale", 331502),

    "The Road to Civilization - 100 Notes Score": ChronoGearLocationData("The Road to Civilization", 410500),
    "The Road to Civilization - 100 Time Score": ChronoGearLocationData("The Road to Civilization", 410501),
    "The Road to Civilization - 100 Damage Taken Score": ChronoGearLocationData("The Road to Civilization", 410502),

    "Roboco Strikes Back - 100 Notes Score": ChronoGearLocationData("Roboco Strikes Back", 411500),
    "Roboco Strikes Back - 100 Time Score": ChronoGearLocationData("Roboco Strikes Back", 411501),
    "Roboco Strikes Back - 100 Damage Taken Score": ChronoGearLocationData("Roboco Strikes Back", 411502),

    "Path of Memories - 100 Notes Score": ChronoGearLocationData("Path of Memories", 420500),
    "Path of Memories - 100 Time Score": ChronoGearLocationData("Path of Memories", 420501),
    "Path of Memories - 100 Damage Taken Score": ChronoGearLocationData("Path of Memories", 420502),

    "A Head Start - 100 Notes Score": ChronoGearLocationData("A Head Start", 430500),
    "A Head Start - 100 Time Score": ChronoGearLocationData("A Head Start", 430501),
    "A Head Start - 100 Damage Taken Score": ChronoGearLocationData("A Head Start", 430502),

    "The War Mind - 100 Notes Score": ChronoGearLocationData("The War Mind", 440500),
    "The War Mind - 100 Time Score": ChronoGearLocationData("The War Mind", 440501),
    "The War Mind - 100 Damage Taken Score": ChronoGearLocationData("The War Mind", 440502),

    "Caravan of Darkness - 100 Notes Score": ChronoGearLocationData("Caravan of Darkness", 510500),
    "Caravan of Darkness - 100 Time Score": ChronoGearLocationData("Caravan of Darkness", 510501),
    "Caravan of Darkness - 100 Damage Taken Score": ChronoGearLocationData("Caravan of Darkness", 510502),

    "Overclocking the Arcade - 100 Notes Score": ChronoGearLocationData("Overclocking the Arcade", 520500),
    "Overclocking the Arcade - 100 Time Score": ChronoGearLocationData("Overclocking the Arcade", 520501),
    "Overclocking the Arcade - 100 Damage Taken Score": ChronoGearLocationData("Overclocking the Arcade", 520502),

    "Song of Light and Darkness - 100 Notes Score": ChronoGearLocationData("Song of Light and Darkness", 530500),
    "Song of Light and Darkness - 100 Time Score": ChronoGearLocationData("Song of Light and Darkness", 530501),
    "Song of Light and Darkness - 100 Damage Taken Score": ChronoGearLocationData("Song of Light and Darkness", 530502),

    "The KFP Games - 100 Notes Score": ChronoGearLocationData("The KFP Games", 540500),
    "The KFP Games - 100 Time Score": ChronoGearLocationData("The KFP Games", 540501),
    "The KFP Games - 100 Damage Taken Score": ChronoGearLocationData("The KFP Games", 540502),

    "Another Time Traveler? - 100 Time Score": ChronoGearLocationData("Another Time Traveler?", 541501),
    "Another Time Traveler? - 100 Damage Taken Score": ChronoGearLocationData("Another Time Traveler?", 541502),

    "Solitude - 100 Notes Score": ChronoGearLocationData("Solitude", 710500),
    "Solitude - 100 Time Score": ChronoGearLocationData("Solitude", 710501),
    "Solitude - 100 Damage Taken Score": ChronoGearLocationData("Solitude", 710502),

    "Entropy - 100 Notes Score": ChronoGearLocationData("Entropy", 720500),
    "Entropy - 100 Time Score": ChronoGearLocationData("Entropy", 720501),
    "Entropy - 100 Damage Taken Score": ChronoGearLocationData("Entropy", 720502),

    "The Ancient Ones - 100 Time Score": ChronoGearLocationData("The Ancient Ones", 711501),
    "The Ancient Ones - 100 Damage Taken Score": ChronoGearLocationData("The Ancient Ones", 711502),

    "Gloom - 100 Notes Score": ChronoGearLocationData("Gloom", 730500),
    "Gloom - 100 Time Score": ChronoGearLocationData("Gloom", 730501),
    "Gloom - 100 Damage Taken Score": ChronoGearLocationData("Gloom", 730502),

    "Despair - 100 Notes Score": ChronoGearLocationData("Despair", 740500),
    "Despair - 100 Time Score": ChronoGearLocationData("Despair", 740501),
    "Despair - 100 Damage Taken Score": ChronoGearLocationData("Despair", 740502),

    "Hope - 100 Time Score": ChronoGearLocationData("Hope", 750501),
    "Hope - 100 Damage Taken Score": ChronoGearLocationData("Hope", 750502),

    "The Way Home - 100 Time Score": ChronoGearLocationData("The Way Home", 751501),
    "The Way Home - 100 Damage Taken Score": ChronoGearLocationData("The Way Home", 751502),

    "The Space Between Worlds - 100 Time Score": ChronoGearLocationData("The Space Between Worlds", 610501),
    "The Space Between Worlds - 100 Damage Taken Score": ChronoGearLocationData("The Space Between Worlds", 610502),

    "Her Time is Now - 100 Notes Score": ChronoGearLocationData("Her Time is Now", 620500),
    "Her Time is Now - 100 Time Score": ChronoGearLocationData("Her Time is Now", 620501),
    "Her Time is Now - 100 Damage Taken Score": ChronoGearLocationData("Her Time is Now", 620502),

    "The Final Ascent - 100 Notes Score": ChronoGearLocationData("The Final Ascent", 630500),
    "The Final Ascent - 100 Time Score": ChronoGearLocationData("The Final Ascent", 630501),
    "The Final Ascent - 100 Damage Taken Score": ChronoGearLocationData("The Final Ascent", 630502),

    "Steel on Steel - 100 Time Score": ChronoGearLocationData("Steel on Steel", 632501),
    "Steel on Steel - 100 Damage Taken Score": ChronoGearLocationData("Steel on Steel", 632502),

    "Zero Seconds to Midnight - 100 Time Score": ChronoGearLocationData("Zero Seconds to Midnight", 633501),
    "Zero Seconds to Midnight - 100 Damage Taken Score": ChronoGearLocationData("Zero Seconds to Midnight", 633502),
}

total_stage_score_location_table: Dict[str, ChronoGearLocationData] = {
    "Storming the Sanctum - 300 Total Score": ChronoGearLocationData("Storming the Sanctum", 110503),
    "Case Closed - 300 Total Score": ChronoGearLocationData("Case Closed", 111503),
    "Defending the Sanctum - 300 Total Score": ChronoGearLocationData("Defending the Sanctum", 112503),
    "The Top of Bell Tower - 300 Total Score": ChronoGearLocationData("The Top of Bell Tower", 120503),
    "The Battle of Bell Town - 300 Total Score": ChronoGearLocationData("The Battle of Bell Town", 121503),
    "The PolPol Express - 300 Total Score": ChronoGearLocationData("The PolPol Express", 130503),
    "The Gravity of Time - 300 Total Score": ChronoGearLocationData("The Gravity of Time", 140503),
    "The Shattered Keep - 300 Total Score": ChronoGearLocationData("The Shattered Keep", 150503),
    "Call to Nature - 300 Total Score": ChronoGearLocationData("Call to Nature", 210503),
    "Autumn Harvest - 300 Total Score": ChronoGearLocationData("Autumn Harvest", 211503),
    "Wrath of Nature - 300 Total Score": ChronoGearLocationData("Wrath of Nature", 212503),
    "The Floating Islands - 300 Total Score": ChronoGearLocationData("The Floating Islands", 220503),
    "Riding the Waves - 300 Total Score": ChronoGearLocationData("Riding the Waves", 230503),
    "Chloe's Beach Race - 300 Total Score": ChronoGearLocationData("Chloe's Beach Race", 231503),
    "Rebuilding the Lost City - 300 Total Score": ChronoGearLocationData("Rebuilding the Lost City", 240503),
    "The Great Space Bake - 300 Total Score": ChronoGearLocationData("The Great Space Bake", 310503),
    "The Houshou Pirates - 300 Total Score": ChronoGearLocationData("The Houshou Pirates", 320503),
    "Luknight of Darkness - 300 Total Score": ChronoGearLocationData("Luknight of Darkness", 330503),
    "Ganmo's Grand Finale - 300 Total Score": ChronoGearLocationData("Ganmo's Grand Finale", 331503),
    "The Road to Civilization - 300 Total Score": ChronoGearLocationData("The Road to Civilization", 410503),
    "Roboco Strikes Back - 300 Total Score": ChronoGearLocationData("Roboco Strikes Back", 411503),
    "Path of Memories - 300 Total Score": ChronoGearLocationData("Path of Memories", 420503),
    "A Head Start - 300 Total Score": ChronoGearLocationData("A Head Start", 430503),
    "The War Mind - 300 Total Score": ChronoGearLocationData("The War Mind", 440503),
    "Caravan of Darkness - 300 Total Score": ChronoGearLocationData("Caravan of Darkness", 510503),
    "Overclocking the Arcade - 300 Total Score": ChronoGearLocationData("Overclocking the Arcade", 520503),
    "Song of Light and Darkness - 300 Total Score": ChronoGearLocationData("Song of Light and Darkness", 530503),
    "The KFP Games - 300 Total Score": ChronoGearLocationData("The KFP Games", 540503),
    "Another Time Traveler? - 300 Total Score": ChronoGearLocationData("Another Time Traveler?", 541503),
    "Solitude - 300 Total Score": ChronoGearLocationData("Solitude", 710503),
    "Entropy - 300 Total Score": ChronoGearLocationData("Entropy", 720503),
    "The Ancient Ones - 300 Total Score": ChronoGearLocationData("The Ancient Ones", 711503),
    "Gloom - 300 Total Score": ChronoGearLocationData("Gloom", 730503),
    "Despair - 300 Total Score": ChronoGearLocationData("Despair", 740503),
    "Hope - 300 Total Score": ChronoGearLocationData("Hope", 750503),
    "The Way Home - 300 Total Score": ChronoGearLocationData("The Way Home", 751503),
    "The Space Between Worlds - 300 Total Score": ChronoGearLocationData("The Space Between Worlds", 610503),
    "Her Time is Now - 300 Total Score": ChronoGearLocationData("Her Time is Now", 620503),
    "The Final Ascent - 300 Total Score": ChronoGearLocationData("The Final Ascent", 630503),
    "Steel on Steel - 300 Total Score": ChronoGearLocationData("Steel on Steel", 632503),
    "Zero Seconds to Midnight - 300 Total Score": ChronoGearLocationData("Zero Seconds to Midnight", 633503),
}

level_collectible_location_table: Dict[str, ChronoGearLocationData] = {
    "Autumn Harvest - Acorn in entrance to tree": ChronoGearLocationData("Autumn Harvest", 211600),
    "Autumn Harvest - Acorn in extra room near beginning": ChronoGearLocationData("Autumn Harvest", 211601),
    "Autumn Harvest - Acorn directly above beginning": ChronoGearLocationData("Autumn Harvest", 211602),
    "Autumn Harvest - Acorn in hidden room with CD": ChronoGearLocationData("Autumn Harvest", 211603),
    "Autumn Harvest - Acorn above tree entrance": ChronoGearLocationData("Autumn Harvest", 211604),
    "Autumn Harvest - Acorn at bottom of outside left path": ChronoGearLocationData("Autumn Harvest", 211605),
    "Autumn Harvest - Acorn at top right of tree": ChronoGearLocationData("Autumn Harvest", 211606),
    "Autumn Harvest - Acorn under entrance to small hidden room": ChronoGearLocationData("Autumn Harvest", 211607),
    "Autumn Harvest - Acorn at middle of outside left path": ChronoGearLocationData("Autumn Harvest", 211608),
    "Autumn Harvest - Acorn right of entrance to CD hidden room": ChronoGearLocationData("Autumn Harvest", 211609),
    "Autumn Harvest - Lower acorn at upper left of tree": ChronoGearLocationData("Autumn Harvest", 211610),
    "Autumn Harvest - Upper acorn at upper left of tree": ChronoGearLocationData("Autumn Harvest", 211611),
    "Autumn Harvest - Acorn next to top checkpoint": ChronoGearLocationData("Autumn Harvest", 211612),
    "Autumn Harvest - Acorn left of top checkpoint": ChronoGearLocationData("Autumn Harvest", 211613),

    "Path of Memories - Chest in boat platform section": ChronoGearLocationData("Path of Memories", 420600),
    "Path of Memories - Chest in spinning platform room with Thread": ChronoGearLocationData("Path of Memories", 420601),
    "Path of Memories - Chest left of beginning": ChronoGearLocationData("Path of Memories", 420602),
    "Path of Memories - Chest left of entrance to chest room": ChronoGearLocationData("Path of Memories", 420603),
    "Path of Memories - Chest in spike room blocked by bubble wall": ChronoGearLocationData("Path of Memories", 420604),
    "Path of Memories - Chest above vertical minecarts right of entrance": ChronoGearLocationData("Path of Memories", 420605),
    "Path of Memories - Chest past minecarts left of entrance": ChronoGearLocationData("Path of Memories", 420606),
    "Path of Memories - Chest up right of entrance": ChronoGearLocationData("Path of Memories", 420607),
    "Path of Memories - Chest with part in chest room": ChronoGearLocationData("Path of Memories", 420608),
    "Path of Memories - Chest left of vertical minecarts near water": ChronoGearLocationData("Path of Memories", 420609),
    "Path of Memories - Chest in underwater passage": ChronoGearLocationData("Path of Memories", 420610),
    "Path of Memories - Chest left of horizontal minecarts near water": ChronoGearLocationData("Path of Memories", 420611),
    "Path of Memories - Chest in left side climb out of water": ChronoGearLocationData("Path of Memories", 420612),
    "Path of Memories - Chest up left of group of three Sun Strikers": ChronoGearLocationData("Path of Memories", 420613),
    "Path of Memories - Maze part from upper WhoMan": ChronoGearLocationData("Path of Memories", 420614),
    "Path of Memories - Maze part from lower WhoMan": ChronoGearLocationData("Path of Memories", 420615),
    "Path of Memories - Interactable chest in chest room": ChronoGearLocationData("Path of Memories", 420616),
    "Path of Memories - Bottom left chest in first chest room": ChronoGearLocationData("Path of Memories", 420617),
    "Path of Memories - Bottom right chest in first chest room": ChronoGearLocationData("Path of Memories", 420618),
    "Path of Memories - Bottom right chest in second chest room": ChronoGearLocationData("Path of Memories", 420619),
    "Path of Memories - Top right chest in second chest room": ChronoGearLocationData("Path of Memories", 420620),
    "Path of Memories - Bottom left chest in second chest room": ChronoGearLocationData("Path of Memories", 420621),

    "The Final Ascent - Key at top of elevator": ChronoGearLocationData("The Final Ascent", 630611),
    "The Final Ascent - Key guarded by Dark Impact": ChronoGearLocationData("The Final Ascent", 630617),
    "The Final Ascent - Key above Bow Platforms": ChronoGearLocationData("The Final Ascent", 630620),
}

sidequest_location_table: Dict[str, ChronoGearLocationData] = {
    "The Gravity of Time - Anya's Keris": ChronoGearLocationData("The Gravity of Time", 140700),
    "Magic Resort - Fishing Rod": ChronoGearLocationData("Magic Resort", 200700),
}

def get_locations_for_mapping() -> Dict[str, ChronoGearLocationData]:
    return location_table | world_unlock_location_table | total_stage_score_location_table | stage_score_location_table | level_collectible_location_table | sidequest_location_table
