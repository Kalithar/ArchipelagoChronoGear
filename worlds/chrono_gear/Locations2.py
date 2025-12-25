#This is a staging file as I refactor how I'm making my locations. Goal is to make it extensible and hopefully not break my brain as much

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
    "Start Game - World of Time Unlock": ChronoGearLocationData("World Map", 1),
    "Start Game - Storming the Sanctum Unlock": ChronoGearLocationData("World Map", 110000),
    
    #World of Time

    "Unlock The Battle of Bell Town": ChronoGearLocationData("World of Time", 121000),
    
    # Eternity Sanctum
    "Eternity Sanctum - Golden Gear from Council Meeting": ChronoGearLocationData("Eternity Sanctum", 100100),
    "Eternity Sanctum - Golden Gear from Secret Sanctum": ChronoGearLocationData("Eternity Sanctum", 101100),
    "Eternity Sanctum - Thread of Time near shop": ChronoGearLocationData("Eternity Sanctum", 100301),
    "Eternity Sanctum - Thread of Time on far right": ChronoGearLocationData("Eternity Sanctum", 100331),
    "Eternity Sanctum - CD after Steel on Steel": ChronoGearLocationData("Eternity Sanctum", 100282),
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

    "Case Closed - Unlock Defending the Sanctum": ChronoGearLocationData("Case Closed", 111000),

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

    "Unlock Rebuilding the Lost City": ChronoGearLocationData("World of Nature", 240000),

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
    "Call to Nature - Unlock Magic Resort": ChronoGearLocationData("Call to Nature", 200000),
    "Call to Nature - Golden Gear": ChronoGearLocationData("Call to Nature", 210100),
    "Call to Nature - CD in first side room": ChronoGearLocationData("Call to Nature", 210232),
    "Call to Nature - CD in summer hidden room": ChronoGearLocationData("Call to Nature", 213233),
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

    "The Great Space Bake - Unlock Starship ID": ChronoGearLocationData("The Great Space Bake", 300000),
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

    "The Road to Civilization - Unlock Town Square": ChronoGearLocationData("The Road to Civilization", 400000),
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

    "Caravan of Darkness - Unlock The Funzone": ChronoGearLocationData("Caravan of Darkness", 500000),
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

    "Song of Light and Darkness - Unlock The KFP Games": ChronoGearLocationData("Song of Light and Darkness", 530000),
    "Song of Light and Darkness - Golden Gear": ChronoGearLocationData("Song of Light and Darkness", 530100),
    "Song of Light and Darkness - CD in top right split path": ChronoGearLocationData("Song of Light and Darkness", 530260),
    "Song of Light and Darkness - Thread of Time in time stop before warp gate": ChronoGearLocationData("Song of Light and Darkness", 530319),
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

    "Solitude - Unlock The Bunker": ChronoGearLocationData("Solitude", 700000),
    "Solitude - Unlock Entropy": ChronoGearLocationData("Solitude", 720000),
    "Solitude - Laplus' Shackle": ChronoGearLocationData("Solitude", 710100),

    "Entropy - Unlock The Ancient Ones": ChronoGearLocationData("Entropy", 711000),
    "Entropy - Laplus' Shackle": ChronoGearLocationData("Entropy", 720100),

    "The Ancient Ones - Unlock Gloom": ChronoGearLocationData("The Ancient Ones", 730000),

    "Gloom - Unlock Despair": ChronoGearLocationData("Gloom", 740000),
    "Gloom - Laplus' Shackle": ChronoGearLocationData("Gloom", 730100),

    "Despair - Unlock Hope": ChronoGearLocationData("Despair", 750000),
    "Despair - Laplus' Shackle": ChronoGearLocationData("Despair", 740100),

    "Hope - Unlock The Way Home": ChronoGearLocationData("Hope", 751000),
    "Hope - Laplus' Shackle": ChronoGearLocationData("Hope", 750100),

    "The Way Home - Unlock World of Darkness": ChronoGearLocationData("The Way Home", 6),
    "The Way Home - Unlock Her Time is Now": ChronoGearLocationData("The Way Home", 620000), 
    "The Way Home - Chrono Gear": ChronoGearLocationData("The Way Home", 751400),

    #World of Darkness

    "Intermission - Unlock The Space Between Worlds": ChronoGearLocationData("The Space Between Worlds", 610000),
    #Where these actually end up depend on settings, but they're in the intermission in vanilla
    "Intermission - Unlock World of Chaos": ChronoGearLocationData("Intermission", 5),
    "Intermission - Unlock World of Civilization": ChronoGearLocationData("Intermission", 4),
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
    "Wrath of Nature - Clear Level": ChronoGearLocationData("Wrath of Nature", None),
    "Ganmo's Grand Finale - Clear Level": ChronoGearLocationData("Ganmo's Grand Finale", None),
    "Another Time Traveler? - Clear Level": ChronoGearLocationData("Another Time Traveler?", None),
    "Roboco Strikes Back - Clear Level": ChronoGearLocationData("Roboco Strikes Back", None),
}
