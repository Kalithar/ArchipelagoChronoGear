class LocationData():
    name: str
    id: int

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

location_table_ : list[LocationData] = [

]

LocationData(" - Level Completion", 000)
LocationData(" - Golden Gear", 100)
LocationData(" - CD", 2)
LocationData(" - Thread of Time", 3)
LocationData(" - Purchase ", )

#Starting Items
#haven't handled these on the client yet, holding off for now

#Time Hub
location_table_time_hub : list[LocationData] = [
    LocationData("Eternity Sanctum - Golden Gear from Council Meeting", 100100),
    LocationData("Eternity Sanctum - Golden Gear from Secret Sanctum", 101100),
    LocationData("Eternity Sanctum - Thread of Time near shop", 100301),
    LocationData("Eternity Sanctum - Thread of Time on far right", 100331),
    LocationData("Eternity Sanctum - CD after Steel on Steel", 100282),
    LocationData("Eternity Sanctum - Right CD after Zero Seconds to Midnight", 100283),
    LocationData("Eternity Sanctum - Left CD after Zero Seconds to Midnight", 100284),
    LocationData("Eternity Sanctum - CD near bookcase", 100286)
]

location_table_time_shop_page_1: list[LocationData] = [
    LocationData("Eternity Sanctum Shop Page 1 - Purchase first CD", 1000),
    LocationData("Eternity Sanctum Shop Page 1 - Purchase second CD", 1001),
    LocationData("Eternity Sanctum Shop Page 1 - Purchase third CD", 1002),
    LocationData("Eternity Sanctum Shop Page 1 - Purchase fourth CD", 1003),
    LocationData("Eternity Sanctum Shop Page 1 - Purchase border art", 1004)
]

location_table_time_shop_page_2: list[LocationData] = [
    LocationData("Eternity Sanctum Shop Page 2 - Purchase first CD", 1101),
    LocationData("Eternity Sanctum Shop Page 2 - Purchase second CD", 1102),
    LocationData("Eternity Sanctum Shop Page 2 - Purchase third CD", 1103),
    LocationData("Eternity Sanctum Shop Page 2 - Purchase first border art", 1104),
    LocationData("Eternity Sanctum Shop Page 2 - Purchase second border art", 1105)
]

location_table_time_shop_page_2: list[LocationData] = [
    LocationData("Eternity Sanctum Shop Page 3 - Purchase border art", 1201),
    LocationData("Eternity Sanctum Shop Page 3 - Purchase first CD", 1202),
    LocationData("Eternity Sanctum Shop Page 3 - Purchase second CD", 1203),
    LocationData("Eternity Sanctum Shop Page 3 - Purchase third CD", 1204),
    LocationData("Eternity Sanctum Shop Page 3 - Purchase fourth CD", 1205),
    LocationData("Eternity Sanctum Shop Page 3 - Purchase fifth CD", 1206),
    LocationData("Eternity Sanctum Shop Page 3 - Purchase sixth CD", 1207),
    LocationData("Eternity Sanctum Shop Page 3 - Purchase seventh CD", 1208),
    LocationData("Eternity Sanctum Shop Page 3 - Purchase eighth CD", 1209),
    LocationData("Eternity Sanctum Shop Page 3 - Purchase ninth CD", 1210),
    LocationData("Eternity Sanctum Shop Page 3 - Purchase tenth CD", 1211),
    LocationData("Eternity Sanctum Shop Page 3 - Purchase eleventh CD", 1212),
    LocationData("Eternity Sanctum Shop Page 3 - Purchase twelfth CD", 1213)
]

#Doorway to Nowhere
location_table_storming_the_sanctum : list[LocationData] = [
    LocationData("Storming the Sanctum - Level Completion", 110000),
    LocationData("Storming the Sanctum - Golden Gear", 110100),
    LocationData("Storming the Sanctum - CD before first checkpoint", 110208),
    LocationData("Storming the Sanctum - CD below giant moving platform", 110207)
]

location_table_case_closed : list[LocationData] = [
    LocationData("Case Closed - Level Completion", 111000)
]

location_table_defending_the_sanctum : list[LocationData] = [
    LocationData("Defending the Sanctum - Level Completion", 112000),
    LocationData("Defending the Sanctum - Golden Gear", 112100),
    LocationData("Defending the Sanctum - CD above first pendulum", 112263),
    LocationData("Defending the Sanctum - Thread of Time before Dark Impact", 112328),
    LocationData("Defending the Sanctum - Thread of Time above last pendulum", 112341)
]

#Bell Town
location_table_top_of_bell_tower : list[LocationData] = [
    LocationData("The Top of Bell Tower - Level Completion", 120000),
    LocationData("The Top of Bell Tower - Golden Gear", 120100),
    LocationData("The Top of Bell Tower - CD above elevator to Underworks", 120204),
    LocationData("The Top of Bell Tower - CD in Underworks", 120213),
    LocationData("The Top of Bell Tower - CD past Kroniephone and moving platform", 120212),
    LocationData("The Top of Bell Tower - Thread of Time above rolling platforms", 120370)
]

location_table_battle_of_bell_town : list[LocationData] = [
    LocationData("The Battle of Bell Town - Level Completion", 121000),
    LocationData("The Battle of Bell Town - Golden Gear", 121100)
]

#Carnival Railway
location_table_polpol_express : list[LocationData] = [
    LocationData("The PolPol Express - Level Completion", 130000),
    LocationData("The PolPol Express - Golden Gear", 130100),
    LocationData("The PolPol Express - CD from freeing Kronies", 130215),
    LocationData("The PolPol Express - CD before final room", 130214),
    LocationData("The PolPol Express - Thread of Time from puzzle room right of warp gate", 130369),
    LocationData("The PolPol Express - Thread of Time at top of large acrobatics room", 130371)
]

#Sands of Time
location_table_gravity_of_time : list[LocationData] = [
    LocationData("The Gravity of Time - Level Completion", 140000),
    LocationData("The Gravity of Time - Golden Gear", 140100),
    LocationData("The Gravity of Time - CD above first warp gate exit", 140216),
    LocationData("The Gravity of Time - CD at top of second section", 140206),
    LocationData("The Gravity of Time - Thread of Time at end of second section", 140304)
]

#Jewel Cyclone
location_table_shattered_keep : list[LocationData] = [
    LocationData("The Shattered Keep - Level Completion", 150000),
    LocationData("The Shattered Keep - Golden Gear", 150100),
    LocationData("The Shattered Keep - CD above third checkpoint", 150209),
    LocationData("The Shattered Keep - CD after first checkpoint", 150217),
    LocationData("The Shattered Keep - Thread of Time on top path backtrack before boss", 150305)
]

#Nature Hub
location_table_nature_hub : list[LocationData] = [
    LocationData("Magic Resort - Golden Gear", 200100),
    LocationData("Magic Resort - Thread of Time for catching Trout", 2003),
    LocationData("Magic Resort - Thread of Time for catching Salmon", 2003),
    LocationData("Magic Resort - Thread of Time for catching Carp", 2003),
    LocationData("Magic Resort - Thread of Time for catching Eel", 2003),
    LocationData("Magic Resort - Thread of Time for catching Dace", 2003),
    LocationData("Magic Resort - Thread of Time for catching Pike", 2003),
    LocationData("Magic Resort - Thread of Time for catching Bream", 2003)
]

location_table_nature_shop : list[LocationData] = [
    LocationData("Magic Resort Shop - Purchase top border art", 1105),
    LocationData("Magic Resort Shop - Purchase top CD", 1105),
    LocationData("Magic Resort Shop - Purchase bottom CD", 1105),
    LocationData("Magic Resort Shop - Purchase bottom border art", 1105)
]

#The World Tree
location_table_call_to_nature : list[LocationData] = [
    LocationData("Call to Nature - Level Completion", 210000),
    LocationData("Call to Nature - Golden Gear", 210100),
    LocationData("Call to Nature - CD", 210232),
    LocationData("Call to Nature - CD", 213233),
    LocationData("Call to Nature - Thread of Time", 2103)
]

location_table_autumn_harvest : list[LocationData] = [
    LocationData("Autumn Harvest - Level Completion", 211000),
    LocationData("Autumn Harvest - Golden Gear", 211100),
    LocationData("Autumn Harvest - CD", 211234),
    LocationData("Autumn Harvest - CD", 211235),
    LocationData("Autumn Harvest - Thread of Time", 2113),
    LocationData("Autumn Harvest - Thread of Time", 2113)
]

location_table_wrath_of_nature : list[LocationData] = [
    LocationData("Wrath of Nature - Level Completion", 212000),
    LocationData("Wrath of Nature - Golden Gear", 212100),
    LocationData("Wrath of Nature - CD", 212242),
    LocationData("Wrath of Nature - Thread of Time", 2123)
]

#Sky Tops
location_table_the_floating_islands : list[LocationData] = [
    LocationData("The Floating Islands - Level Completion", 220000),
    LocationData("The Floating Islands - Golden Gear", 220100),
    LocationData("The Floating Islands - CD", 220238),
    LocationData("The Floating Islands - Thread of Time", 2203),
    LocationData("The Floating Islands - Thread of Time", 2203)
]

#Tidal Camp
location_table_riding_the_waves : list[LocationData] = [
    LocationData("Riding the Waves - Level Completion", 230000),
    LocationData("Riding the Waves - Golden Gear", 230100),
    LocationData("Riding the Waves - CD", 230239),
    LocationData("Riding the Waves - Thread of Time", 2303),
    LocationData("Riding the Waves - Thread of Time", 2303)
]

location_table_chloes_beach_race : list[LocationData] = [
    LocationData("Chloe's Beach Race - Level Completion", 231000),
    LocationData("Chloe's Beach Race - Golden Gear", 231100)
]

#Depths of Atlantis
location_table_rebuilding_the_lost_city : list[LocationData] = [
    LocationData("Rebuilding the Lost City - Level Completion", 240000),
    LocationData("Rebuilding the Lost City - Golden Gear", 240100),
    LocationData("Rebuilding the Lost City - CD", 240241),
    LocationData("Rebuilding the Lost City - Thread of Time", 2403),
    LocationData("Rebuilding the Lost City - Thread of Time", 2403)
]

#Space Hub
location_table_space_hub : list[LocationData] = [
    LocationData("Starship - Golden Gear", 300100),
    LocationData("Starship - Thread of Time", 3003),
    LocationData("Starship - CD", 300223)
]

location_table_space_shop_page_1 : list[LocationData] = [
    LocationData("Starship ID Shop Page 1 - Purchase CD", 3005),
    LocationData("Starship ID Shop Page 1 - Purchase first border art", 3005),
    LocationData("Starship ID Shop Page 1 - Purchase second border art", 3005),
    LocationData("Starship ID Shop Page 1 - Purchase third border art", 3005)
]

location_table_space_shop_page_2 : list[LocationData] = [
    LocationData("Starship ID Shop Page 2 - Purchase first CD", 3005),
    LocationData("Starship ID Shop Page 2 - Purchase second CD", 3005),
    LocationData("Starship ID Shop Page 2 - Purchase first border art", 3005),
    LocationData("Starship ID Shop Page 2 - Purchase second border art", 3005)
]

#Galaxy Gourmet
location_table_the_great_space_bake : list[LocationData] = [
    LocationData("The Great Space Bake - Level Completion", 310000),
    LocationData("The Great Space Bake - Golden Gear", 310100),
    LocationData("The Great Space Bake - CD", 310221),
    LocationData("The Great Space Bake - Thread of Time", 3103)
]

#Battleship Aquamarine
location_table_the_houshou_pirates : list[LocationData] = [
    LocationData("The Houshou Pirates - Level Completion", 320000),
    LocationData("The Houshou Pirates - Golden Gear", 320100),
    LocationData("The Houshou Pirates - CD", 320224),
    LocationData("The Houshou Pirates - CD", 320226),
    LocationData("The Houshou Pirates - CD", 320225)
]

#Hoshinova Castle
location_table_luknight_of_darkness : list[LocationData] = [
    LocationData("Luknight of Darkness - Level Completion", 330000),
    LocationData("Luknight of Darkness - Golden Gear", 330100),
    LocationData("Luknight of Darkness - CD", 330229),
    LocationData("Luknight of Darkness - CD", 330230),
    LocationData("Luknight of Darkness - Thread of Time", 3303),
    LocationData("Luknight of Darkness - Thread of Time", 3303)
]

location_table_ganmos_grand_finale : list[LocationData] = [
    LocationData("Ganmo's Grand Finale - Level Completion", 331000),
    LocationData("Ganmo's Grand Finale - Golden Gear", 331100)
]

#Civilization Hub
location_table_civ_hub : list[LocationData] = [
    LocationData("Town Square - Golden Gear", 400100),
    LocationData("Town Square - Thread of Time", 4003),
    LocationData("Town Square - Thread of Time", 4003),
    LocationData("Town Square - CD", 400248),
    LocationData("Town Square - CD", 400254)
]

location_table_civ_shop : list[LocationData] = [
    LocationData("Town Square Shop - Purchase first border art", 4005),
    LocationData("Town Square Shop - Purchase first CD", 4005),
    LocationData("Town Square Shop - Purchase second border art", 4005),
    LocationData("Town Square Shop - Purchase second CD", 4005),
    LocationData("Town Square Shop - Purchase third border art", 4005),
    LocationData("Town Square Shop - Purchase third CD", 4005),
    LocationData("Town Square Shop - Purchase fourth CD", 4005)
]

#Castle Road
location_table_the_road_to_civilization : list[LocationData] = [
    LocationData("The Road to Civilization - Level Completion", 410000),
    LocationData("The Road to Civilization - Golden Gear", 410100),
    LocationData("The Road to Civilization - CD", 410249),
    LocationData("The Road to Civilization - Thread of Time", 4103),
    LocationData("The Road to Civilization - Thread of Time", 4103)
]

location_table_roboco_strikes_back : list[LocationData] = [
    LocationData("Roboco Strikes Back - Level Completion", 411000),
    LocationData("A Head Start - Golden Gear", 411100)
]

#The Maze
location_table_path_of_memories : list[LocationData] = [
    LocationData("Path of Memories - Level Completion", 420000),
    LocationData("Path of Memories - Golden Gear", 420100),
    LocationData("Path of Memories - CD", 420251),
    LocationData("Path of Memories - Thread of Time", 4203),
    LocationData("Path of Memories - Thread of Time", 4203),
    LocationData("Path of Memories - Thread of Time", 4203)
]

#Cursed Lands
location_table_a_head_start : list[LocationData] = [
    LocationData("A Head Start - Level Completion", 430000),
    LocationData("A Head Start - Golden Gear", 430100),
    LocationData("A Head Start - CD", 430252),
    LocationData("A Head Start - Thread of Time", 4303)
]

#Magitech Forge
location_table_the_war_mind : list[LocationData] = [
    LocationData("The War Mind - Level Completion", 440000),
    LocationData("The War Mind - Golden Gear", 440100),
    LocationData("The War Mind - CD", 440253),
    LocationData("The War Mind - Thread of Time", 4403),
    LocationData("The War Mind - Thread of Time", 4403),
    LocationData("The War Mind - Thread of Time", 4403)
]

#Chaos Hub
location_table_chaos_hub : list[LocationData] = [
    LocationData("The Fun Zone - CD", 500254)
]

location_table_chaos_shop : list[LocationData] = [
    LocationData("Town Square - Purchase first CD", 5005),
    LocationData("Town Square - Purchase second CD", 5005),
    LocationData("Town Square - Purchase third CD", 5005),
    LocationData("Town Square - Purchase fourth CD", 5005),
    LocationData("Town Square - Purchase fifth CD", 5005),
    LocationData("Town Square - Purchase sixth CD", 5005),
    LocationData("Town Square - Purchase first border art", 5005),
    LocationData("Town Square - Purchase second border art", 5005),
    LocationData("Town Square - Purchase third border art", 5005)
]

#Highway of Dreams
location_table_caravan_of_darkness : list[LocationData] = [
    LocationData("Carvan of Darkness - Level Completion", 510000),
    LocationData("Carvan of Darkness - Golden Gear", 510100),
    LocationData("Carvan of Darkness - CD", 510256),
    LocationData("Carvan of Darkness - Thread of Time", 5103),
    LocationData("Carvan of Darkness - Thread of Time", 5103)
]

#Ducky God Arcade
location_table_overclocking_the_arcade : list[LocationData] = [
    LocationData("Overclocking the Arcade - Level Completion", 520000),
    LocationData("Overclocking the Arcade - Golden Gear", 520100),
    LocationData("Overclocking the Arcade - CD", 520259),
    LocationData("Overclocking the Arcade - Thread of Time", 5203)
]

#Symphonic Gallery
location_table_song_of_light_and_darkness : list[LocationData] = [
    LocationData("Song of Light and Darkness - Level Completion", 530000),
    LocationData("Song of Light and Darkness - Golden Gear", 530100),
    LocationData("Song of Light and Darkness - CD", 530260),
    LocationData("Song of Light and Darkness - Thread of Time", 5303),
    LocationData("Song of Light and Darkness - Thread of Time", 5303)
]

#KFP Stadium
location_table_the_kfp_games : list[LocationData] = [
    LocationData("The KFP Games - Level Completion", 530000),
    LocationData("The KFP Games - Golden Gear", 530100),
    LocationData("The KFP Games - CD", 530260),
    LocationData("The KFP Games - CD", 530260),
    LocationData("The KFP Games - Thread of Time", 5303)
]

location_table_another_time_travler : list[LocationData] = [
    LocationData("Another Time Traveler? - Level Completion", 531000)
]

#Alter Timeline
location_table_solitude : list[LocationData] = [
    LocationData("Solitude - Level Completion", 710000),
    LocationData("Solitude - Laplus' Shackle", 710100)
]

location_table_entropy : list[LocationData] = [
    LocationData("Entropy - Level Completion", 720000),
    LocationData("Entropy - Laplus' Shackle", 720100)
]

location_table_the_ancient_ones : list[LocationData] = [
    LocationData("The Ancient Ones - Level Completion", 711000),
]

location_table_gloom : list[LocationData] = [
    LocationData("Gloom - Level Completion", 730000),
    LocationData("Gloom - Laplus' Shackle", 730100)
]

location_table_despair : list[LocationData] = [
    LocationData("Despair - Level Completion", 740000),
    LocationData("Despair - Laplus' Shackle", 740100)
]

location_table_hope : list[LocationData] = [
    LocationData("Hope - Level Completion", 750000),
    LocationData("Hope - Laplus' Shackle", 750100)
]

location_table_the_way_home : list[LocationData] = [
    LocationData("The Way Home - Level Completion", 751000),
    LocationData("The Way Home - Chrono Gear")
]

#World of Darkness
location_table_intermission : list[LocationData] = [
    LocationData("The Space Between Worlds - Level Completion")
]

location_table_her_time_is_now : list[LocationData] = [
    LocationData("Her Time is Now - Level Completion", 620000),
    LocationData("Her Time is Now - Golden Gear", 620100),
    LocationData("Her Time is Now - CD", 620275),
    LocationData("Her Time is Now - Thread of Time", 6203),
    LocationData("Her Time is Now - Thread of Time", 6203),
    LocationData("Her Time is Now - Thread of Time", 6203),
    LocationData("Her Time is Now - Thread of Time", 6203)
]

location_table_the_final_ascent : list[LocationData] = [
    LocationData("The Final Ascent - Level Completion", 630000),
    LocationData("The Final Ascent - Golden Gear", 630100),
    LocationData("The Final Ascent - CD", 630276),
    LocationData("The Final Ascent - CD", 630277),
    LocationData("The Final Ascent - CD", 630278),
    LocationData("The Final Ascent - CD", 630279),
    LocationData("The Final Ascent - CD", 630280),
    LocationData("The Final Ascent - CD", 630281)
]

location_table_steel_on_steel : list[LocationData] = [
    LocationData("Her Time is Now - Level Completion", 631000)
]

location_table_zero_seconds_to_midnight : list[LocationData] = [
    LocationData("Zero Seconds to Midnight - Level Completion", 632000)
]