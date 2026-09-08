from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import IronNestWorld

LOCATION_NAME_TO_ID = {
    "Mission 1 - Completion"        :   1,
    "Mission 1 - Medal - Bronze"    :   2,
    "Mission 1 - Medal - Silver"    :   3,
    "Mission 1 - Medal - Gold"      :   4,
    "Mission 2 - Completion"        : 201,
    "Mission 2 - Medal - Bronze"    : 202,
    "Mission 2 - Medal - Silver"    : 203,
    "Mission 2 - Medal - Gold"      : 204,
    "Mission 3 - Completion"        : 301,
    "Mission 3 - Medal 1 - Bronze"  : 302,
    "Mission 3 - Medal 2 - Bronze"  : 303,
    "Mission 3 - Medal 3 - Bronze"  : 304,
    "Mission 3 - Medal 4 - Bronze"  : 305,
    "Mission 3 - Medal 1 - Silver"  : 306,
    "Mission 3 - Medal 2 - Silver"  : 307,
    "Mission 3 - Medal 3 - Silver"  : 308,
    "Mission 3 - Medal 4 - Silver"  : 309,
    "Mission 3 - Medal 1 - Gold"    : 310,
    "Mission 3 - Medal 2 - Gold"    : 311,
    "Mission 3 - Medal 3 - Gold"    : 312,
    "Mission 3 - Medal 4 - Gold"    : 313,
    "Mission 4 - Completion"        : 401,
    "Mission 4 - Medal 1 - Bronze"  : 402,
    "Mission 4 - Medal 2 - Bronze"  : 403,
    "Mission 4 - Medal 3 - Bronze"  : 404,
    "Mission 4 - Medal 4 - Bronze"  : 405,
    "Mission 4 - Medal 1 - Silver"  : 406,
    "Mission 4 - Medal 2 - Silver"  : 407,
    "Mission 4 - Medal 3 - Silver"  : 408,
    "Mission 4 - Medal 4 - Silver"  : 409,
    "Mission 4 - Medal 1 - Gold"    : 410,
    "Mission 4 - Medal 2 - Gold"    : 411,
    "Mission 4 - Medal 3 - Gold"    : 412,
    "Mission 4 - Medal 4 - Gold"    : 413,
    "Mission 5 - Completion"        : 501,
    "Mission 5 - Medal 1 - Bronze"  : 502,
    "Mission 5 - Medal 2 - Bronze"  : 503,
    "Mission 5 - Medal 3 - Bronze"  : 504,
    "Mission 5 - Medal 4 - Bronze"  : 505,
    "Mission 5 - Medal 1 - Silver"  : 506,
    "Mission 5 - Medal 2 - Silver"  : 507,
    "Mission 5 - Medal 3 - Silver"  : 508,
    "Mission 5 - Medal 4 - Silver"  : 509,
    "Mission 5 - Medal 1 - Gold"    : 510,
    "Mission 5 - Medal 2 - Gold"    : 511,
    "Mission 5 - Medal 3 - Gold"    : 512,
    "Mission 5 - Medal 4 - Gold"    : 513,
    "Mission 6 - Completion"        : 601,
    "Mission 6 - Medal 1 - Bronze"  : 602,
    "Mission 6 - Medal 2 - Bronze"  : 603,
    "Mission 6 - Medal 3 - Bronze"  : 604,
    "Mission 6 - Medal 4 - Bronze"  : 605,
    "Mission 6 - Medal 1 - Silver"  : 606,
    "Mission 6 - Medal 2 - Silver"  : 607,
    "Mission 6 - Medal 3 - Silver"  : 608,
    "Mission 6 - Medal 4 - Silver"  : 609,
    "Mission 6 - Medal 1 - Gold"    : 610,
    "Mission 6 - Medal 2 - Gold"    : 611,
    "Mission 6 - Medal 3 - Gold"    : 612,
    "Mission 6 - Medal 4 - Gold"    : 613,
    "Mission 7 - Completion"        : 701,
    "Mission 7 - Medal 1 - Bronze"  : 702,
    "Mission 7 - Medal 2 - Bronze"  : 703,
    "Mission 7 - Medal 3 - Bronze"  : 704,
    "Mission 7 - Medal 4 - Bronze"  : 705,
    "Mission 7 - Medal 1 - Silver"  : 706,
    "Mission 7 - Medal 2 - Silver"  : 707,
    "Mission 7 - Medal 3 - Silver"  : 708,
    "Mission 7 - Medal 4 - Silver"  : 709,
    "Mission 7 - Medal 1 - Gold"    : 710,
    "Mission 7 - Medal 2 - Gold"    : 711,
    "Mission 7 - Medal 3 - Gold"    : 712,
    "Mission 7 - Medal 4 - Gold"    : 713,
    "Mission 8 - Completion"        : 801,
    "Mission 8 - Medal 1 - Bronze"  : 802,
    "Mission 8 - Medal 2 - Bronze"  : 803,
    "Mission 8 - Medal 3 - Bronze"  : 804,
    "Mission 8 - Medal 4 - Bronze"  : 805,
    "Mission 8 - Medal 1 - Silver"  : 806,
    "Mission 8 - Medal 2 - Silver"  : 807,
    "Mission 8 - Medal 3 - Silver"  : 808,
    "Mission 8 - Medal 4 - Silver"  : 809,
    "Mission 8 - Medal 1 - Gold"    : 810,
    "Mission 8 - Medal 2 - Gold"    : 811,
    "Mission 8 - Medal 3 - Gold"    : 812,
    "Mission 8 - Medal 4 - Gold"    : 813,
    "Mission 9 - Completion" : 901,
    "Mission 9 - Medal 1 - Bronze" : 902,
    "Mission 9 - Medal 2 - Bronze" : 903,
    "Mission 9 - Medal 3 - Bronze" : 904,
    "Mission 9 - Medal 4 - Bronze" : 905,
    "Mission 9 - Medal 1 - Silver" : 906,
    "Mission 9 - Medal 2 - Silver" : 907,
    "Mission 9 - Medal 3 - Silver" : 908,
    "Mission 9 - Medal 4 - Silver" : 909,
    "Mission 9 - Medal 1 - Gold" : 910,
    "Mission 9 - Medal 2 - Gold" : 911,
    "Mission 9 - Medal 3 - Gold" : 912,
    "Mission 9 - Medal 4 - Gold" : 913,
    "Mission 10 - Completion" : 1001,
    "Mission 10 - Medal 1 - Bronze" : 1002,
    "Mission 10 - Medal 2 - Bronze" : 1003,
    "Mission 10 - Medal 3 - Bronze" : 1004,
    "Mission 10 - Medal 4 - Bronze" : 1005,
    "Mission 10 - Medal 1 - Silver" : 1006,
    "Mission 10 - Medal 2 - Silver" : 1007,
    "Mission 10 - Medal 3 - Silver" : 1008,
    "Mission 10 - Medal 4 - Silver" : 1009,
    "Mission 10 - Medal 1 - Gold" : 1010,
    "Mission 10 - Medal 2 - Gold" : 1011,
    "Mission 10 - Medal 3 - Gold" : 1012,
    "Mission 10 - Medal 4 - Gold" : 1013,
    "Mission 11 - Completion" : 1101,
    "Mission 11 - Medal 1 - Bronze" : 1102,
    "Mission 11 - Medal 2 - Bronze" : 1103,
    "Mission 11 - Medal 3 - Bronze" : 1104,
    "Mission 11 - Medal 4 - Bronze" : 1105,
    "Mission 11 - Medal 1 - Silver" : 1106,
    "Mission 11 - Medal 2 - Silver" : 1107,
    "Mission 11 - Medal 3 - Silver" : 1108,
    "Mission 11 - Medal 4 - Silver" : 1109,
    "Mission 11 - Medal 1 - Gold" : 1110,
    "Mission 11 - Medal 2 - Gold" : 1111,
    "Mission 11 - Medal 3 - Gold" : 1120,
    "Mission 11 - Medal 4 - Gold" : 1120,
    "Mission 12 - Completion" : 1201,
    "Mission 12 - Medal 1 - Bronze" : 1202,
    "Mission 12 - Medal 2 - Bronze" : 1203,
    "Mission 12 - Medal 3 - Bronze" : 1204,
    "Mission 12 - Medal 4 - Bronze" : 1205,
    "Mission 12 - Medal 1 - Silver" : 1206,
    "Mission 12 - Medal 2 - Silver" : 1207,
    "Mission 12 - Medal 3 - Silver" : 1208,
    "Mission 12 - Medal 4 - Silver" : 1209,
    "Mission 12 - Medal 1 - Gold" : 1210,
    "Mission 12 - Medal 2 - Gold" : 1211,
    "Mission 12 - Medal 3 - Gold" : 1212,
    "Mission 12 - Medal 4 - Gold" : 1213,
    "Mission 13 - Completion" : 1301,
    "Mission 13 - Medal 1 - Bronze" : 1302,
    "Mission 13 - Medal 2 - Bronze" : 1303,
    "Mission 13 - Medal 3 - Bronze" : 1304,
    "Mission 13 - Medal 4 - Bronze" : 1305,
    "Mission 13 - Medal 1 - Silver" : 1306,
    "Mission 13 - Medal 2 - Silver" : 1307,
    "Mission 13 - Medal 3 - Silver" : 1308,
    "Mission 13 - Medal 4 - Silver" : 1309,
    "Mission 13 - Medal 1 - Gold" : 1310,
    "Mission 13 - Medal 2 - Gold" : 1311,
    "Mission 13 - Medal 3 - Gold" : 1312,
    "Mission 13 - Medal 4 - Gold" : 1313,
    "Mission 14 - Completion" : 1401,
    "Mission 14 - Medal 1 - Bronze" : 1402,
    "Mission 14 - Medal 2 - Bronze" : 1403,
    "Mission 14 - Medal 3 - Bronze" : 1404,
    "Mission 14 - Medal 4 - Bronze" : 1405,
    "Mission 14 - Medal 1 - Silver" : 1406,
    "Mission 14 - Medal 2 - Silver" : 1407,
    "Mission 14 - Medal 3 - Silver" : 1408,
    "Mission 14 - Medal 4 - Silver" : 1409,
    "Mission 14 - Medal 1 - Gold" : 1410,
    "Mission 14 - Medal 2 - Gold" : 1411,
    "Mission 14 - Medal 3 - Gold" : 1412,
    "Mission 14 - Medal 4 - Gold" : 1413,
    "Mission 15 - Ending 1" : 1501,
    "Mission 15 - Ending 2" : 1502,
    "Mission 15 - Ending 3" : 1503,
    "Mission 15 - Ending 4" : 1504,
}

class IronNestLocation(Location):
    game = "IRON NEST: Heavy Turret Simulator"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: IronNestWorld) -> None:
    create_regular_locations(world)
    #create_events(world)


def create_regular_locations(world: IronNestWorld) -> None:
    mission_1 = world.get_region("Mission 1")
    mission_2 = world.get_region("Mission 2")
    mission_3 = world.get_region("Mission 3")
    mission_4 = world.get_region("Mission 4")
    mission_5 = world.get_region("Mission 5")
    mission_6 = world.get_region("Mission 6")
    mission_7 = world.get_region("Mission 7")
    mission_8 = world.get_region("Mission 8")
    mission_9 = world.get_region("Mission 9")
    mission_10 = world.get_region("Mission 10")
    mission_11 = world.get_region("Mission 11")
    mission_12 = world.get_region("Mission 12")
    mission_13 = world.get_region("Mission 13")
    mission_14 = world.get_region("Mission 14")
    mission_15 = world.get_region("Mission 15")

    mission_1_locations = get_location_names_with_ids([
        "Mission 1 - Medal - Bronze",
        "Mission 1 - Medal - Silver",
        "Mission 1 - Medal - Gold",
    ])
    mission_1.add_locations(mission_1_locations, IronNestLocation)

    mission_2_locations = get_location_names_with_ids([
        "Mission 2 - Medal - Bronze",
        "Mission 2 - Medal - Silver",
        "Mission 2 - Medal - Gold",
    ])
    mission_2.add_locations(mission_2_locations, IronNestLocation)

    mission_3_locations = get_location_names_with_ids([
        "Mission 3 - Medal 1 - Bronze",
        "Mission 3 - Medal 2 - Bronze",
        "Mission 3 - Medal 3 - Bronze",
        "Mission 3 - Medal 4 - Bronze",
        "Mission 3 - Medal 1 - Silver",
        "Mission 3 - Medal 2 - Silver",
        "Mission 3 - Medal 3 - Silver",
        "Mission 3 - Medal 4 - Silver",
        "Mission 3 - Medal 1 - Gold",
        "Mission 3 - Medal 2 - Gold",
        "Mission 3 - Medal 3 - Gold",
        "Mission 3 - Medal 4 - Gold",
    ])
    mission_3.add_locations(mission_3_locations, IronNestLocation)

    mission_4_locations = get_location_names_with_ids([
        "Mission 4 - Medal 1 - Bronze",
        "Mission 4 - Medal 2 - Bronze",
        "Mission 4 - Medal 3 - Bronze",
        "Mission 4 - Medal 4 - Bronze",
        "Mission 4 - Medal 1 - Silver",
        "Mission 4 - Medal 2 - Silver",
        "Mission 4 - Medal 3 - Silver",
        "Mission 4 - Medal 4 - Silver",
        "Mission 4 - Medal 1 - Gold",
        "Mission 4 - Medal 2 - Gold",
        "Mission 4 - Medal 3 - Gold",
        "Mission 4 - Medal 4 - Gold",
    ])
    mission_4.add_locations(mission_4_locations, IronNestLocation)

    mission_5_locations = get_location_names_with_ids([
        "Mission 5 - Medal 1 - Bronze",
        "Mission 5 - Medal 2 - Bronze",
        "Mission 5 - Medal 3 - Bronze",
        "Mission 5 - Medal 4 - Bronze",
        "Mission 5 - Medal 1 - Silver",
        "Mission 5 - Medal 2 - Silver",
        "Mission 5 - Medal 3 - Silver",
        "Mission 5 - Medal 4 - Silver",
        "Mission 5 - Medal 1 - Gold",
        "Mission 5 - Medal 2 - Gold",
        "Mission 5 - Medal 3 - Gold",
        "Mission 5 - Medal 4 - Gold",
    ])
    mission_5.add_locations(mission_5_locations, IronNestLocation)

    mission_6_locations = get_location_names_with_ids([
        "Mission 6 - Medal 1 - Bronze",
        "Mission 6 - Medal 2 - Bronze",
        "Mission 6 - Medal 3 - Bronze",
        "Mission 6 - Medal 4 - Bronze",
        "Mission 6 - Medal 1 - Silver",
        "Mission 6 - Medal 2 - Silver",
        "Mission 6 - Medal 3 - Silver",
        "Mission 6 - Medal 4 - Silver",
        "Mission 6 - Medal 1 - Gold",
        "Mission 6 - Medal 2 - Gold",
        "Mission 6 - Medal 3 - Gold",
        "Mission 6 - Medal 4 - Gold",
    ])
    mission_6.add_locations(mission_6_locations, IronNestLocation)

    mission_7_locations = get_location_names_with_ids([
        "Mission 7 - Medal 1 - Bronze",
        "Mission 7 - Medal 2 - Bronze",
        "Mission 7 - Medal 3 - Bronze",
        "Mission 7 - Medal 4 - Bronze",
        "Mission 7 - Medal 1 - Silver",
        "Mission 7 - Medal 2 - Silver",
        "Mission 7 - Medal 3 - Silver",
        "Mission 7 - Medal 4 - Silver",
        "Mission 7 - Medal 1 - Gold",
        "Mission 7 - Medal 2 - Gold",
        "Mission 7 - Medal 3 - Gold",
        "Mission 7 - Medal 4 - Gold",
    ])
    mission_7.add_locations(mission_7_locations, IronNestLocation)

    mission_8_locations = get_location_names_with_ids([
        "Mission 8 - Medal 1 - Bronze",
        "Mission 8 - Medal 2 - Bronze",
        "Mission 8 - Medal 3 - Bronze",
        "Mission 8 - Medal 4 - Bronze",
        "Mission 8 - Medal 1 - Silver",
        "Mission 8 - Medal 2 - Silver",
        "Mission 8 - Medal 3 - Silver",
        "Mission 8 - Medal 4 - Silver",
        "Mission 8 - Medal 1 - Gold",
        "Mission 8 - Medal 2 - Gold",
        "Mission 8 - Medal 3 - Gold",
        "Mission 8 - Medal 4 - Gold",
    ])
    mission_8.add_locations(mission_8_locations, IronNestLocation)

    mission_9_locations = get_location_names_with_ids([
        "Mission 9 - Medal 1 - Bronze",
        "Mission 9 - Medal 2 - Bronze",
        "Mission 9 - Medal 3 - Bronze",
        "Mission 9 - Medal 4 - Bronze",
        "Mission 9 - Medal 1 - Silver",
        "Mission 9 - Medal 2 - Silver",
        "Mission 9 - Medal 3 - Silver",
        "Mission 9 - Medal 4 - Silver",
        "Mission 9 - Medal 1 - Gold",
        "Mission 9 - Medal 2 - Gold",
        "Mission 9 - Medal 3 - Gold",
        "Mission 9 - Medal 4 - Gold",
    ])
    mission_9.add_locations(mission_9_locations, IronNestLocation)

    mission_10_locations = get_location_names_with_ids([
        "Mission 10 - Medal 1 - Bronze",
        "Mission 10 - Medal 2 - Bronze",
        "Mission 10 - Medal 3 - Bronze",
        "Mission 10 - Medal 4 - Bronze",
        "Mission 10 - Medal 1 - Silver",
        "Mission 10 - Medal 2 - Silver",
        "Mission 10 - Medal 3 - Silver",
        "Mission 10 - Medal 4 - Silver",
        "Mission 10 - Medal 1 - Gold",
        "Mission 10 - Medal 2 - Gold",
        "Mission 10 - Medal 3 - Gold",
        "Mission 10 - Medal 4 - Gold",
    ])
    mission_10.add_locations(mission_10_locations, IronNestLocation)

    mission_11_locations = get_location_names_with_ids([
        "Mission 11 - Medal 1 - Bronze",
        "Mission 11 - Medal 2 - Bronze",
        "Mission 11 - Medal 3 - Bronze",
        "Mission 11 - Medal 4 - Bronze",
        "Mission 11 - Medal 1 - Silver",
        "Mission 11 - Medal 2 - Silver",
        "Mission 11 - Medal 3 - Silver",
        "Mission 11 - Medal 4 - Silver",
        "Mission 11 - Medal 1 - Gold",
        "Mission 11 - Medal 2 - Gold",
        "Mission 11 - Medal 3 - Gold",
        "Mission 11 - Medal 4 - Gold",
    ])
    mission_11.add_locations(mission_11_locations, IronNestLocation)

    mission_12_locations = get_location_names_with_ids([
        "Mission 12 - Medal 1 - Bronze",
        "Mission 12 - Medal 2 - Bronze",
        "Mission 12 - Medal 3 - Bronze",
        "Mission 12 - Medal 4 - Bronze",
        "Mission 12 - Medal 1 - Silver",
        "Mission 12 - Medal 2 - Silver",
        "Mission 12 - Medal 3 - Silver",
        "Mission 12 - Medal 4 - Silver",
        "Mission 12 - Medal 1 - Gold",
        "Mission 12 - Medal 2 - Gold",
        "Mission 12 - Medal 3 - Gold",
        "Mission 12 - Medal 4 - Gold",
    ])
    mission_12.add_locations(mission_12_locations, IronNestLocation)

    mission_13_locations = get_location_names_with_ids([
        "Mission 13 - Medal 1 - Bronze",
        "Mission 13 - Medal 2 - Bronze",
        "Mission 13 - Medal 3 - Bronze",
        "Mission 13 - Medal 4 - Bronze",
        "Mission 13 - Medal 1 - Silver",
        "Mission 13 - Medal 2 - Silver",
        "Mission 13 - Medal 3 - Silver",
        "Mission 13 - Medal 4 - Silver",
        "Mission 13 - Medal 1 - Gold",
        "Mission 13 - Medal 2 - Gold",
        "Mission 13 - Medal 3 - Gold",
        "Mission 13 - Medal 4 - Gold",
    ])
    mission_13.add_locations(mission_13_locations, IronNestLocation)

    mission_14_locations = get_location_names_with_ids([
        "Mission 14 - Medal 1 - Bronze",
        "Mission 14 - Medal 2 - Bronze",
        "Mission 14 - Medal 3 - Bronze",
        "Mission 14 - Medal 4 - Bronze",
        "Mission 14 - Medal 1 - Silver",
        "Mission 14 - Medal 2 - Silver",
        "Mission 14 - Medal 3 - Silver",
        "Mission 14 - Medal 4 - Silver",
        "Mission 14 - Medal 1 - Gold",
        "Mission 14 - Medal 2 - Gold",
        "Mission 14 - Medal 3 - Gold",
        "Mission 14 - Medal 4 - Gold",
    ])
    mission_14.add_locations(mission_14_locations, IronNestLocation)

    mission_15_locations = get_location_names_with_ids([
        "Mission 15 - Ending 1",
        "Mission 15 - Ending 2",
        "Mission 15 - Ending 3",
        "Mission 15 - Ending 4",
    ])
    mission_15.add_locations(mission_15_locations, IronNestLocation)

#def create_events(world: IronNestWorld) -> None:
