from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import ChronoGearWorld

class ChronoGearLocation():
    name: str
    id: int
    game: str

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.game = "Chrono Gear"

#Starting Items
#haven't handled these on the client yet, holding off for now

#Time Hub
location_table_time_hub : list[ChronoGearLocation] = [
    ChronoGearLocation("Eternity Sanctum - Golden Gear from Council Meeting", 100100),
    ChronoGearLocation("Eternity Sanctum - Golden Gear from Secret Sanctum", 101100),
    ChronoGearLocation("Eternity Sanctum - Thread of Time near shop", 100301),
    ChronoGearLocation("Eternity Sanctum - Thread of Time on far right", 100331),
    ChronoGearLocation("Eternity Sanctum - CD after Steel on Steel", 100282),
    ChronoGearLocation("Eternity Sanctum - Right CD after Zero Seconds to Midnight", 100283),
    ChronoGearLocation("Eternity Sanctum - Left CD after Zero Seconds to Midnight", 100284),
    ChronoGearLocation("Eternity Sanctum - CD near bookcase", 100286)
]

location_table_time_shop_page_1: list[ChronoGearLocation] = [
    ChronoGearLocation("Eternity Sanctum Shop Page 1 - Purchase first CD", 1000),
    ChronoGearLocation("Eternity Sanctum Shop Page 1 - Purchase second CD", 1001),
    ChronoGearLocation("Eternity Sanctum Shop Page 1 - Purchase third CD", 1002),
    ChronoGearLocation("Eternity Sanctum Shop Page 1 - Purchase fourth CD", 1003),
    ChronoGearLocation("Eternity Sanctum Shop Page 1 - Purchase border art", 1004)
]

location_table_time_shop_page_2: list[ChronoGearLocation] = [
    ChronoGearLocation("Eternity Sanctum Shop Page 2 - Purchase first CD", 1100),
    ChronoGearLocation("Eternity Sanctum Shop Page 2 - Purchase second CD", 1101),
    ChronoGearLocation("Eternity Sanctum Shop Page 2 - Purchase third CD", 1102),
    ChronoGearLocation("Eternity Sanctum Shop Page 2 - Purchase first border art", 1103),
    ChronoGearLocation("Eternity Sanctum Shop Page 2 - Purchase second border art", 1104)
]

location_table_time_shop_page_3: list[ChronoGearLocation] = [
    ChronoGearLocation("Eternity Sanctum Shop Page 3 - Purchase border art", 1200),
    ChronoGearLocation("Eternity Sanctum Shop Page 3 - Purchase first CD", 1201),
    ChronoGearLocation("Eternity Sanctum Shop Page 3 - Purchase second CD", 1202),
    ChronoGearLocation("Eternity Sanctum Shop Page 3 - Purchase third CD", 1203),
    ChronoGearLocation("Eternity Sanctum Shop Page 3 - Purchase fourth CD", 1204),
    ChronoGearLocation("Eternity Sanctum Shop Page 3 - Purchase fifth CD", 1205),
    ChronoGearLocation("Eternity Sanctum Shop Page 3 - Purchase sixth CD", 1206),
    ChronoGearLocation("Eternity Sanctum Shop Page 3 - Purchase seventh CD", 1207),
    ChronoGearLocation("Eternity Sanctum Shop Page 3 - Purchase eighth CD", 1208),
    ChronoGearLocation("Eternity Sanctum Shop Page 3 - Purchase ninth CD", 1209),
    ChronoGearLocation("Eternity Sanctum Shop Page 3 - Purchase tenth CD", 1210),
    ChronoGearLocation("Eternity Sanctum Shop Page 3 - Purchase eleventh CD", 1211),
    ChronoGearLocation("Eternity Sanctum Shop Page 3 - Purchase twelfth CD", 1212)
]

#Doorway to Nowhere
location_table_storming_the_sanctum : list[ChronoGearLocation] = [
    ChronoGearLocation("Storming the Sanctum - Level Completion", 110000),
    ChronoGearLocation("Storming the Sanctum - Golden Gear", 110100),
    ChronoGearLocation("Storming the Sanctum - CD before first checkpoint", 110208),
    ChronoGearLocation("Storming the Sanctum - CD below giant moving platform", 110207)
]

location_table_case_closed : list[ChronoGearLocation] = [
    ChronoGearLocation("Case Closed - Level Completion", 111000)
]

location_table_defending_the_sanctum : list[ChronoGearLocation] = [
    ChronoGearLocation("Defending the Sanctum - Level Completion", 112000),
    ChronoGearLocation("Defending the Sanctum - Golden Gear", 112100),
    ChronoGearLocation("Defending the Sanctum - CD above first pendulum", 112263),
    ChronoGearLocation("Defending the Sanctum - Thread of Time before Dark Impact", 112328),
    ChronoGearLocation("Defending the Sanctum - Thread of Time above last pendulum", 112341)
]

#Bell Town
location_table_top_of_bell_tower : list[ChronoGearLocation] = [
    ChronoGearLocation("The Top of Bell Tower - Level Completion", 120000),
    ChronoGearLocation("The Top of Bell Tower - Golden Gear", 120100),
    ChronoGearLocation("The Top of Bell Tower - CD above elevator to Underworks", 120204),
    ChronoGearLocation("The Top of Bell Tower - CD in Underworks", 120213),
    ChronoGearLocation("The Top of Bell Tower - CD past Kroniephone and moving platform", 120212),
    ChronoGearLocation("The Top of Bell Tower - Thread of Time above rolling platforms", 120370)
]

location_table_battle_of_bell_town : list[ChronoGearLocation] = [
    ChronoGearLocation("The Battle of Bell Town - Level Completion", 121000),
    ChronoGearLocation("The Battle of Bell Town - Golden Gear", 121100)
]

#Carnival Railway
location_table_polpol_express : list[ChronoGearLocation] = [
    ChronoGearLocation("The PolPol Express - Level Completion", 130000),
    ChronoGearLocation("The PolPol Express - Golden Gear", 130100),
    ChronoGearLocation("The PolPol Express - CD from freeing Kronies", 130215),
    ChronoGearLocation("The PolPol Express - CD before final room", 130214),
    ChronoGearLocation("The PolPol Express - Thread of Time from puzzle room right of warp gate", 130369),
    ChronoGearLocation("The PolPol Express - Thread of Time at top of large acrobatics room", 130371)
]

#Sands of Time
location_table_gravity_of_time : list[ChronoGearLocation] = [
    ChronoGearLocation("The Gravity of Time - Level Completion", 140000),
    ChronoGearLocation("The Gravity of Time - Golden Gear", 140100),
    ChronoGearLocation("The Gravity of Time - CD above first warp gate exit", 140216),
    ChronoGearLocation("The Gravity of Time - CD at top of second section", 140206),
    ChronoGearLocation("The Gravity of Time - Thread of Time at end of second section", 140304)
]

#Jewel Cyclone
location_table_shattered_keep : list[ChronoGearLocation] = [
    ChronoGearLocation("The Shattered Keep - Level Completion", 150000),
    ChronoGearLocation("The Shattered Keep - Golden Gear", 150100),
    ChronoGearLocation("The Shattered Keep - CD above third checkpoint", 150209),
    ChronoGearLocation("The Shattered Keep - CD after first checkpoint", 150217),
    ChronoGearLocation("The Shattered Keep - Thread of Time on top path backtrack before boss", 150305)
]

#Nature Hub
location_table_nature_hub : list[ChronoGearLocation] = [
    ChronoGearLocation("Magic Resort - Golden Gear", 200100),
    ChronoGearLocation("Magic Resort - Thread of Time for catching Trout", 200360),
    ChronoGearLocation("Magic Resort - Thread of Time for catching Salmon", 200361),
    ChronoGearLocation("Magic Resort - Thread of Time for catching Carp", 200362),
    ChronoGearLocation("Magic Resort - Thread of Time for catching Eel", 200363),
    ChronoGearLocation("Magic Resort - Thread of Time for catching Dace", 200364),
    ChronoGearLocation("Magic Resort - Thread of Time for catching Pike", 200365),
    ChronoGearLocation("Magic Resort - Thread of Time for catching Bream", 200366)
]

location_table_nature_shop : list[ChronoGearLocation] = [
    ChronoGearLocation("Magic Resort Shop - Purchase top border art", 2000),
    ChronoGearLocation("Magic Resort Shop - Purchase top CD", 2001),
    ChronoGearLocation("Magic Resort Shop - Purchase bottom CD", 2002),
    ChronoGearLocation("Magic Resort Shop - Purchase bottom border art", 2003)
]

#The World Tree
location_table_call_to_nature : list[ChronoGearLocation] = [
    ChronoGearLocation("Call to Nature - Level Completion", 210000),
    ChronoGearLocation("Call to Nature - Golden Gear", 210100),
    ChronoGearLocation("Call to Nature - CD in first side room", 210232),
    ChronoGearLocation("Call to Nature - CD in summer hidden room", 213233),
    ChronoGearLocation("Call to Nature - Thread of Time at top of tree trunk", 210306)
]

location_table_autumn_harvest : list[ChronoGearLocation] = [
    ChronoGearLocation("Autumn Harvest - Level Completion", 211000),
    ChronoGearLocation("Autumn Harvest - Golden Gear", 211100),
    ChronoGearLocation("Autumn Harvest - CD in autumn side room halfway up tree", 211234),
    ChronoGearLocation("Autumn Harvest - CD in winter pointed to by haste notes", 211235),
    ChronoGearLocation("Autumn Harvest - Thread of Time in autumn hidden room", 211307),
    ChronoGearLocation("Autumn Harvest - Thread of Time above second winter warp trunk", 211343)
]

location_table_wrath_of_nature : list[ChronoGearLocation] = [
    ChronoGearLocation("Wrath of Nature - Level Completion", 212000),
    ChronoGearLocation("Wrath of Nature - Golden Gear", 212100),
    ChronoGearLocation("Wrath of Nature - CD before first checkpoint", 212242),
    ChronoGearLocation("Wrath of Nature - Thread of Time before first water sphere", 212327)
]

#Sky Tops
location_table_the_floating_islands : list[ChronoGearLocation] = [
    ChronoGearLocation("The Floating Islands - Level Completion", 220000),
    ChronoGearLocation("The Floating Islands - Golden Gear", 220100),
    ChronoGearLocation("The Floating Islands - CD in cave with flower", 220238),
    ChronoGearLocation("The Floating Islands - Thread of Time before second checkpoint after second warp gate", 220325),
    ChronoGearLocation("The Floating Islands - Thread of Time before Golden Gear", 220340)
]

#Tidal Camp
location_table_riding_the_waves : list[ChronoGearLocation] = [
    ChronoGearLocation("Riding the Waves - Level Completion", 230000),
    ChronoGearLocation("Riding the Waves - Golden Gear", 230100),
    ChronoGearLocation("Riding the Waves - CD above crabs in last bumper section", 230239),
    ChronoGearLocation("Riding the Waves - Thread of Time underwater after first checkpoint", 230308),
    ChronoGearLocation("Riding the Waves - Thread of Time above third checkpoint", 230309)
]

location_table_chloes_beach_race : list[ChronoGearLocation] = [
    ChronoGearLocation("Chloe's Beach Race - Level Completion", 231000),
    ChronoGearLocation("Chloe's Beach Race - Golden Gear", 231100)
]

#Depths of Atlantis
location_table_rebuilding_the_lost_city : list[ChronoGearLocation] = [
    ChronoGearLocation("Rebuilding the Lost City - Level Completion", 240000),
    ChronoGearLocation("Rebuilding the Lost City - Golden Gear", 240100),
    ChronoGearLocation("Rebuilding the Lost City - CD on side path at beginning of ruins", 240241),
    ChronoGearLocation("Rebuilding the Lost City - Thread of Time behind lower eel after first checkpoint", 240310),
    ChronoGearLocation("Rebuilding the Lost City - Thread of Time locked by optional switch in second ruins section", 240311)
]

#Space Hub
location_table_space_hub : list[ChronoGearLocation] = [
    ChronoGearLocation("Starship - Golden Gear", 300100),
    ChronoGearLocation("Starship - Thread of Time on top of ship", 300342),
    ChronoGearLocation("Starship - CD in generator room", 300223)
]

location_table_space_shop_page_1 : list[ChronoGearLocation] = [
    ChronoGearLocation("Starship ID Shop Page 1 - Purchase CD", 3000),
    ChronoGearLocation("Starship ID Shop Page 1 - Purchase first border art", 3001),
    ChronoGearLocation("Starship ID Shop Page 1 - Purchase second border art", 3002),
    ChronoGearLocation("Starship ID Shop Page 1 - Purchase third border art", 3003)
]

location_table_space_shop_page_2 : list[ChronoGearLocation] = [
    ChronoGearLocation("Starship ID Shop Page 2 - Purchase first CD", 3100),
    ChronoGearLocation("Starship ID Shop Page 2 - Purchase second CD", 3101),
    ChronoGearLocation("Starship ID Shop Page 2 - Purchase first border art", 3102),
    ChronoGearLocation("Starship ID Shop Page 2 - Purchase second border art", 3103)
]

#Galaxy Gourmet
location_table_the_great_space_bake : list[ChronoGearLocation] = [
    ChronoGearLocation("The Great Space Bake - Level Completion", 310000),
    ChronoGearLocation("The Great Space Bake - Golden Gear", 310100),
    ChronoGearLocation("The Great Space Bake - CD left of warp gate after first checkpoint", 310221),
    ChronoGearLocation("The Great Space Bake - Thread of Time under island after second checkpoint", 310326)
]

#Battleship Aquamarine
location_table_the_houshou_pirates : list[ChronoGearLocation] = [
    ChronoGearLocation("The Houshou Pirates - Level Completion", 320000),
    ChronoGearLocation("The Houshou Pirates - Golden Gear", 320100),
    ChronoGearLocation("The Houshou Pirates - CD below first cannons", 320224),
    ChronoGearLocation("The Houshou Pirates - CD before vertical cannons", 320226),
    ChronoGearLocation("The Houshou Pirates - CD guarded by Root Beer Walker", 320225)
]

#Hoshinova Castle
location_table_luknight_of_darkness : list[ChronoGearLocation] = [
    ChronoGearLocation("Luknight of Darkness - Level Completion", 330000),
    ChronoGearLocation("Luknight of Darkness - Golden Gear", 330100),
    ChronoGearLocation("Luknight of Darkness - CD left of second checkpoint", 330229),
    ChronoGearLocation("Luknight of Darkness - CD from defeating Armored Rangoon", 330230),
    ChronoGearLocation("Luknight of Darkness - Thread of Time in underground section", 330350),
    ChronoGearLocation("Luknight of Darkness - Thread of Time on right split path", 330351)
]

location_table_ganmos_grand_finale : list[ChronoGearLocation] = [
    ChronoGearLocation("Ganmo's Grand Finale - Level Completion", 331000),
    ChronoGearLocation("Ganmo's Grand Finale - Golden Gear", 331100)
]

#Civilization Hub
location_table_civ_hub : list[ChronoGearLocation] = [
    ChronoGearLocation("Town Square - Golden Gear", 400100),
    ChronoGearLocation("Town Square - Thread of Time from powerwashing", 400302),
    ChronoGearLocation("Town Square - Thread of Time on top of house", 400303),
    ChronoGearLocation("Town Square - CD in powerwashing room", 400248),
    ChronoGearLocation("Town Square - CD from fixing Roboco", 400254)
]

location_table_civ_shop : list[ChronoGearLocation] = [
    ChronoGearLocation("Town Square Shop - Purchase first border art", 4000),
    ChronoGearLocation("Town Square Shop - Purchase first CD", 4001),
    ChronoGearLocation("Town Square Shop - Purchase second border art", 4002),
    ChronoGearLocation("Town Square Shop - Purchase second CD", 4003),
    ChronoGearLocation("Town Square Shop - Purchase third border art", 4004),
    ChronoGearLocation("Town Square Shop - Purchase third CD", 4005),
    ChronoGearLocation("Town Square Shop - Purchase fourth CD", 4006)
]

#Castle Road
location_table_the_road_to_civilization : list[ChronoGearLocation] = [
    ChronoGearLocation("The Road to Civilization - Level Completion", 410000),
    ChronoGearLocation("The Road to Civilization - Golden Gear", 410100),
    ChronoGearLocation("The Road to Civilization - CD at top of tall tower with Mumei glider", 410249),
    ChronoGearLocation("The Road to Civilization - Thread of Time left of first warp gate exit", 410312),
    ChronoGearLocation("The Road to Civilization - Thread of Time underwater before tall tower with Mumei glider", 410373)
]

location_table_roboco_strikes_back : list[ChronoGearLocation] = [
    ChronoGearLocation("Roboco Strikes Back - Level Completion", 411000),
    ChronoGearLocation("A Head Start - Golden Gear", 411100)
]

#The Maze
location_table_path_of_memories : list[ChronoGearLocation] = [
    ChronoGearLocation("Path of Memories - Level Completion", 420000),
    ChronoGearLocation("Path of Memories - Golden Gear", 420100),
    ChronoGearLocation("Path of Memories - CD in left section above WhoMan", 420251),
    ChronoGearLocation("Path of Memories - Thread of Time in top rotating wall section", 420317),
    ChronoGearLocation("Path of Memories - Thread of Time underwater in bottom right section", 420318),
    ChronoGearLocation("Path of Memories - Thread of Time in top middle section near WhoMan", 4203)
]

#Cursed Lands
location_table_a_head_start : list[ChronoGearLocation] = [
    ChronoGearLocation("A Head Start - Level Completion", 430000),
    ChronoGearLocation("A Head Start - Golden Gear", 430100),
    ChronoGearLocation("A Head Start - CD left of pit before fourth checkpoint", 430252),
    ChronoGearLocation("A Head Start - Thread of Time blocked by flame blocks after Chesseract", 430313)
]

#Magitech Forge
location_table_the_war_mind : list[ChronoGearLocation] = [
    ChronoGearLocation("The War Mind - Level Completion", 440000),
    ChronoGearLocation("The War Mind - Golden Gear", 440100),
    ChronoGearLocation("The War Mind - CD in upper room with Bounce Crates after first warp gate", 440253),
    ChronoGearLocation("The War Mind - Thread of Time underneath crates by Dark Impact", 440314),
    ChronoGearLocation("The War Mind - Thread of Time guarded by 4 Goblin Roses", 440315),
    ChronoGearLocation("The War Mind - Thread of Time above first checkpoint", 440339)
]

#Chaos Hub
location_table_chaos_hub : list[ChronoGearLocation] = [
    ChronoGearLocation("The Fun Zone - CD on rollercoaster", 500257)
]

location_table_chaos_shop : list[ChronoGearLocation] = [
    ChronoGearLocation("Town Square - Purchase first CD", 5000),
    ChronoGearLocation("Town Square - Purchase second CD", 5001),
    ChronoGearLocation("Town Square - Purchase third CD", 5002),
    ChronoGearLocation("Town Square - Purchase fourth CD", 5003),
    ChronoGearLocation("Town Square - Purchase fifth CD", 5004),
    ChronoGearLocation("Town Square - Purchase sixth CD", 5005),
    ChronoGearLocation("Town Square - Purchase first border art", 5006),
    ChronoGearLocation("Town Square - Purchase second border art", 5007),
    ChronoGearLocation("Town Square - Purchase third border art", 5008)
]

#Highway of Dreams
location_table_caravan_of_darkness : list[ChronoGearLocation] = [
    ChronoGearLocation("Caravan of Darkness - Level Completion", 510000),
    ChronoGearLocation("Caravan of Darkness - Golden Gear", 510100),
    ChronoGearLocation("Caravan of Darkness - CD above warp gate into upside down section", 510256),
    ChronoGearLocation("Caravan of Darkness - Thread of Time underneath crane in long descent", 510316),
    ChronoGearLocation("Caravan of Darkness - Thread of Time above rails over pit", 510330)
]

#Ducky God Arcade
location_table_overclocking_the_arcade : list[ChronoGearLocation] = [
    ChronoGearLocation("Overclocking the Arcade - Level Completion", 520000),
    ChronoGearLocation("Overclocking the Arcade - Golden Gear", 520100),
    ChronoGearLocation("Overclocking the Arcade - CD through arcade screen before fourth checkpoint", 520259),
    ChronoGearLocation("Overclocking the Arcade - Thread of Time though arcade screen before Golden Gear", 520332)
]

#Symphonic Gallery
location_table_song_of_light_and_darkness : list[ChronoGearLocation] = [
    ChronoGearLocation("Song of Light and Darkness - Level Completion", 530000),
    ChronoGearLocation("Song of Light and Darkness - Golden Gear", 530100),
    ChronoGearLocation("Song of Light and Darkness - CD in top right split path", 530260),
    ChronoGearLocation("Song of Light and Darkness - Thread of Time in time stop before warp gate", 530319),
    ChronoGearLocation("Song of Light and Darkness - Thread of Time above Hydra Block in final climb", 530334)
]

#KFP Stadium
location_table_the_kfp_games : list[ChronoGearLocation] = [
    ChronoGearLocation("The KFP Games - Level Completion", 530000),
    ChronoGearLocation("The KFP Games - Golden Gear", 530100),
    ChronoGearLocation("The KFP Games - CD at top of backtrack in second stage", 530262),
    ChronoGearLocation("The KFP Games - CD while backtracking in fourth stage", 530261),
    ChronoGearLocation("The KFP Games - Thread of Time before flame in second stage", 530320)
]

location_table_another_time_travler : list[ChronoGearLocation] = [
    ChronoGearLocation("Another Time Traveler? - Level Completion", 531000)
]

#Alter Timeline
location_table_solitude : list[ChronoGearLocation] = [
    ChronoGearLocation("Solitude - Level Completion", 710000),
    ChronoGearLocation("Solitude - Laplus' Shackle", 710100)
]

location_table_entropy : list[ChronoGearLocation] = [
    ChronoGearLocation("Entropy - Level Completion", 720000),
    ChronoGearLocation("Entropy - Laplus' Shackle", 720100)
]

location_table_the_ancient_ones : list[ChronoGearLocation] = [
    ChronoGearLocation("The Ancient Ones - Level Completion", 711000),
]

location_table_gloom : list[ChronoGearLocation] = [
    ChronoGearLocation("Gloom - Level Completion", 730000),
    ChronoGearLocation("Gloom - Laplus' Shackle", 730100)
]

location_table_despair : list[ChronoGearLocation] = [
    ChronoGearLocation("Despair - Level Completion", 740000),
    ChronoGearLocation("Despair - Laplus' Shackle", 740100)
]

location_table_hope : list[ChronoGearLocation] = [
    ChronoGearLocation("Hope - Level Completion", 750000),
    ChronoGearLocation("Hope - Laplus' Shackle", 750100)
]

location_table_the_way_home : list[ChronoGearLocation] = [
    ChronoGearLocation("The Way Home - Level Completion", 751000),
    ChronoGearLocation("The Way Home - Chrono Gear", 751400)
]

#World of Darkness
location_table_intermission : list[ChronoGearLocation] = [
    ChronoGearLocation("The Space Between Worlds - Level Completion", 610000)
]

location_table_her_time_is_now : list[ChronoGearLocation] = [
    ChronoGearLocation("Her Time is Now - Level Completion", 620000),
    ChronoGearLocation("Her Time is Now - Golden Gear", 620100),
    ChronoGearLocation("Her Time is Now - CD at end of first ground section", 620275),
    ChronoGearLocation("Her Time is Now - Thread of Time above Defense Core", 620322),
    ChronoGearLocation("Her Time is Now - Thread of Time on pillar before gate", 620323),
    ChronoGearLocation("Her Time is Now - Thread of Time left of first moving lasers", 620324),
    ChronoGearLocation("Her Time is Now - Thread of Time right of first moving lasers", 620321)
]

location_table_the_final_ascent : list[ChronoGearLocation] = [
    ChronoGearLocation("The Final Ascent - Level Completion", 630000),
    ChronoGearLocation("The Final Ascent - Golden Gear", 630100),
    ChronoGearLocation("The Final Ascent - CD in ruined room near lobby", 630276),
    ChronoGearLocation("The Final Ascent - CD covered by shadow barrier", 630277),
    ChronoGearLocation("The Final Ascent - CD in large room with Arc Sentinels", 630278),
    ChronoGearLocation("The Final Ascent - CD behind key locked door", 630279),
    ChronoGearLocation("The Final Ascent - CD above ruined portal", 630280),
    ChronoGearLocation("The Final Ascent - CD at top of frozen time section with Shadow Armor", 630281)
]

location_table_steel_on_steel : list[ChronoGearLocation] = [
    ChronoGearLocation("Steel on Steel - Level Completion", 631000)
]

location_table_zero_seconds_to_midnight : list[ChronoGearLocation] = [
    ChronoGearLocation("Zero Seconds to Midnight - Level Completion", 632000)
]