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
    LocationData("The Shattered Keep - Thread of Time on top path backtracking before boss", 150305)
]