from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import IronNestWorld

# Medals
# OE - Ordanance Efficiency
# MF - Measured Fire
# MC - Marksman's Cross
# UV - Unbroken Volley
# AS - Austere Service
# SC - Salvo Commendation
# CB - Counter-Battery Commendation
# NQ - No Quarter
# UF - Unaided Fire Distinction
# RE - Rapid Engagement

LOCATION_NAME_TO_ID = {
    # OE only
    "Mission 1: Calibration Fire - Completion"   :    1,
    "Mission 1: Calibration Fire - OE Bronze"    :    2,
    "Mission 1: Calibration Fire - OE Silver"    :    3,
    "Mission 1: Calibration Fire - OE Gold"      :    4,
    "Mission 2: Fire and Light - Completion"     :  101,
    "Mission 2: Fire and Light - OE Bronze"      :  102,
    "Mission 2: Fire and Light - OE Silver"      :  103,
    "Mission 2: Fire and Light - OE Gold"        :  104,
    # MF, MC, UV, AS                                
    "Mission 3: Liberation - Completion"         :  201,
    "Mission 3: Liberation - MF Bronze"          :  202,
    "Mission 3: Liberation - MC Bronze"          :  203,
    "Mission 3: Liberation - UV Bronze"          :  204,
    "Mission 3: Liberation - AS Bronze"          :  205,
    "Mission 3: Liberation - MF Silver"          :  206,
    "Mission 3: Liberation - MC Silver"          :  207,
    "Mission 3: Liberation - UV Silver"          :  208,
    "Mission 3: Liberation - AS Silver"          :  209,
    "Mission 3: Liberation - MF Gold"            :  210,
    "Mission 3: Liberation - MC Gold"            :  211,
    "Mission 3: Liberation - UV Gold"            :  212,
    "Mission 3: Liberation - AS Gold"            :  213,
    # SC, CB, AS, NQ                                
    "Mission 4: Counter-Battery - Completion"    :  301,
    "Mission 4: Counter-Battery - SC Bronze"     :  302,
    "Mission 4: Counter-Battery - CB Bronze"     :  303,
    "Mission 4: Counter-Battery - AS Bronze"     :  304,
    "Mission 4: Counter-Battery - NQ Bronze"     :  305,
    "Mission 4: Counter-Battery - SC Silver"     :  306,
    "Mission 4: Counter-Battery - CB Silver"     :  307,
    "Mission 4: Counter-Battery - AS Silver"     :  308,
    "Mission 4: Counter-Battery - NQ Silver"     :  309,
    "Mission 4: Counter-Battery - SC Gold"       :  310,
    "Mission 4: Counter-Battery - CB Gold"       :  311,
    "Mission 4: Counter-Battery - AS Gold"       :  312,
    "Mission 4: Counter-Battery - NQ Gold"       :  313,
    # MF, UV, OE, UF                                
    "Mission 5: Iron Road - Completion"          :  401,
    "Mission 5: Iron Road - MF Bronze"           :  402,
    "Mission 5: Iron Road - UV Bronze"           :  403,
    "Mission 5: Iron Road - OE Bronze"           :  404,
    "Mission 5: Iron Road - UF Bronze"           :  405,
    "Mission 5: Iron Road - MF Silver"           :  406,
    "Mission 5: Iron Road - UV Silver"           :  407,
    "Mission 5: Iron Road - OE Silver"           :  408,
    "Mission 5: Iron Road - UF Silver"           :  409,
    "Mission 5: Iron Road - MF Gold"             :  410,
    "Mission 5: Iron Road - UV Gold"             :  411,
    "Mission 5: Iron Road - OE Gold"             :  412,
    "Mission 5: Iron Road - UF Gold"             :  413,
    # MF, NQ, UF, AS                               
    "Mission 6: Siege of Cartagena - Completion" :  501,
    "Mission 6: Siege of Cartagena - MF Bronze"  :  502,
    "Mission 6: Siege of Cartagena - NQ Bronze"  :  503,
    "Mission 6: Siege of Cartagena - UF Bronze"  :  504,
    "Mission 6: Siege of Cartagena - AS Bronze"  :  505,
    "Mission 6: Siege of Cartagena - MF Silver"  :  506,
    "Mission 6: Siege of Cartagena - NQ Silver"  :  507,
    "Mission 6: Siege of Cartagena - UF Silver"  :  508,
    "Mission 6: Siege of Cartagena - AS Silver"  :  509,
    "Mission 6: Siege of Cartagena - MF Gold"    :  510,
    "Mission 6: Siege of Cartagena - NQ Gold"    :  511,
    "Mission 6: Siege of Cartagena - UF Gold"    :  512,
    "Mission 6: Siege of Cartagena - AS Gold"    :  513,
    # MF, UV, NQ, OE                               
    "Mission 7: The Gorge - Completion"          :  601,
    "Mission 7: The Gorge - MF Bronze"           :  602,
    "Mission 7: The Gorge - UV Bronze"           :  603,
    "Mission 7: The Gorge - NQ Bronze"           :  604,
    "Mission 7: The Gorge - OE Bronze"           :  605,
    "Mission 7: The Gorge - MF Silver"           :  606,
    "Mission 7: The Gorge - UV Silver"           :  607,
    "Mission 7: The Gorge - NQ Silver"           :  608,
    "Mission 7: The Gorge - OE Silver"           :  609,
    "Mission 7: The Gorge - MF Gold"             :  610,
    "Mission 7: The Gorge - UV Gold"             :  611,
    "Mission 7: The Gorge - NQ Gold"             :  612,
    "Mission 7: The Gorge - OE Gold"             :  613,
    # MF, NQ, UF, AS                                
    "Mission 8: Rock of Gibraltar - Completion"  :  701,
    "Mission 8: Rock of Gibraltar - MF Bronze"   :  702,
    "Mission 8: Rock of Gibraltar - NQ Bronze"   :  703,
    "Mission 8: Rock of Gibraltar - UF Bronze"   :  704,
    "Mission 8: Rock of Gibraltar - AS Bronze"   :  705,
    "Mission 8: Rock of Gibraltar - MF Silver"   :  706,
    "Mission 8: Rock of Gibraltar - NQ Silver"   :  707,
    "Mission 8: Rock of Gibraltar - UF Silver"   :  708,
    "Mission 8: Rock of Gibraltar - AS Silver"   :  709,
    "Mission 8: Rock of Gibraltar - MF Gold"     :  710,
    "Mission 8: Rock of Gibraltar - NQ Gold"     :  711,
    "Mission 8: Rock of Gibraltar - UF Gold"     :  712,
    "Mission 8: Rock of Gibraltar - AS Gold"     :  713,
    # MF, UV, NQ, AS                                
    "Mission 9: Dead Reckoning - Completion"     :  801,
    "Mission 9: Dead Reckoning - MF Bronze"      :  802,
    "Mission 9: Dead Reckoning - UV Bronze"      :  803,
    "Mission 9: Dead Reckoning - NQ Bronze"      :  804,
    "Mission 9: Dead Reckoning - AS Bronze"      :  805,
    "Mission 9: Dead Reckoning - MF Silver"      :  806,
    "Mission 9: Dead Reckoning - UV Silver"      :  807,
    "Mission 9: Dead Reckoning - NQ Silver"      :  808,
    "Mission 9: Dead Reckoning - AS Silver"      :  809,
    "Mission 9: Dead Reckoning - MF Gold"        :  810,
    "Mission 9: Dead Reckoning - UV Gold"        :  811,
    "Mission 9: Dead Reckoning - NQ Gold"        :  812,
    "Mission 9: Dead Reckoning - AS Gold"        :  813,
    # MF, NQ, OE, UF                             
    "Mission 10: Fire and Call - Completion"     :  901,
    "Mission 10: Fire and Call - MF Bronze"      :  902,
    "Mission 10: Fire and Call - NQ Bronze"      :  903,
    "Mission 10: Fire and Call - OE Bronze"      :  904,
    "Mission 10: Fire and Call - UF Bronze"      :  905,
    "Mission 10: Fire and Call - MF Silver"      :  906,
    "Mission 10: Fire and Call - NQ Silver"      :  907,
    "Mission 10: Fire and Call - OE Silver"      :  908,
    "Mission 10: Fire and Call - UF Silver"      :  909,
    "Mission 10: Fire and Call - MF Gold"        :  910,
    "Mission 10: Fire and Call - NQ Gold"        :  911,
    "Mission 10: Fire and Call - OE Gold"        :  912,
    "Mission 10: Fire and Call - UF Gold"        :  913,
    # UV, SC, MC, (UV is on this one twice)      
    "Mission 11: High Tide - Completion"         : 1001,
    "Mission 11: High Tide - UV Bronze"          : 1002,
    "Mission 11: High Tide - SC Bronze"          : 1003,
    "Mission 11: High Tide - MC Bronze"          : 1004,
    "Mission 11: High Tide - UV Silver"          : 1005,
    "Mission 11: High Tide - SC Silver"          : 1006,
    "Mission 11: High Tide - MC Silver"          : 1007,
    "Mission 11: High Tide - UV Gold"            : 1008,
    "Mission 11: High Tide - SC Gold"            : 1009,
    "Mission 11: High Tide - MC Gold"            : 1010,
    # AS, UV, NQ, UF                             
    "Mission 12: Blind Fire - Completion"        : 1101,
    "Mission 12: Blind Fire - AS Bronze"         : 1102,
    "Mission 12: Blind Fire - UV Bronze"         : 1103,
    "Mission 12: Blind Fire - NQ Bronze"         : 1104,
    "Mission 12: Blind Fire - UF Bronze"         : 1105,
    "Mission 12: Blind Fire - AS Silver"         : 1106,
    "Mission 12: Blind Fire - UV Silver"         : 1107,
    "Mission 12: Blind Fire - NQ Silver"         : 1108,
    "Mission 12: Blind Fire - UF Silver"         : 1109,
    "Mission 12: Blind Fire - AS Gold"           : 1110,
    "Mission 12: Blind Fire - UV Gold"           : 1111,
    "Mission 12: Blind Fire - NQ Gold"           : 1112,
    "Mission 12: Blind Fire - UF Gold"           : 1113,
    # UF, NQ, MC, CB                             
    "Mission 13: Phantom Battery - Completion"   : 1201,
    "Mission 13: Phantom Battery - UF Bronze"    : 1202,
    "Mission 13: Phantom Battery - NQ Bronze"    : 1203,
    "Mission 13: Phantom Battery - MC Bronze"    : 1204,
    "Mission 13: Phantom Battery - CB Bronze"    : 1205,
    "Mission 13: Phantom Battery - UF Silver"    : 1206,
    "Mission 13: Phantom Battery - NQ Silver"    : 1207,
    "Mission 13: Phantom Battery - MC Silver"    : 1208,
    "Mission 13: Phantom Battery - CB Silver"    : 1209,
    "Mission 13: Phantom Battery - UF Gold"      : 1210,
    "Mission 13: Phantom Battery - NQ Gold"      : 1211,
    "Mission 13: Phantom Battery - MC Gold"      : 1212,
    "Mission 13: Phantom Battery - CB Gold"      : 1213,
    # MF, UF, NQ, RE                             
    "Mission 14: Final Harvest - Completion"     : 1301,
    "Mission 14: Final Harvest - MF Bronze"      : 1302,
    "Mission 14: Final Harvest - UF Bronze"      : 1303,
    "Mission 14: Final Harvest - NQ Bronze"      : 1304,
    "Mission 14: Final Harvest - RE Bronze"      : 1305,
    "Mission 14: Final Harvest - MF Silver"      : 1306,
    "Mission 14: Final Harvest - UF Silver"      : 1307,
    "Mission 14: Final Harvest - NQ Silver"      : 1308,
    "Mission 14: Final Harvest - RE Silver"      : 1309,
    "Mission 14: Final Harvest - MF Gold"        : 1310,
    "Mission 14: Final Harvest - UF Gold"        : 1311,
    "Mission 14: Final Harvest - NQ Gold"        : 1312,
    "Mission 14: Final Harvest - RE Gold"        : 1313,
    # Just Endings (Gold level only)             
    "Mission 15: White Shells - Ending 1"        : 1401,
    "Mission 15: White Shells - Ending 2"        : 1402,
    "Mission 15: White Shells - Ending 3"        : 1403,
    "Mission 15: White Shells - Ending 4"        : 1404,
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
        "Mission 1: Calibration Fire - Completion",
        "Mission 1: Calibration Fire - OE Bronze" ,
        "Mission 1: Calibration Fire - OE Silver" ,
        "Mission 1: Calibration Fire - OE Gold"   ,
    ])
    mission_1.add_locations(mission_1_locations, IronNestLocation)

    mission_2_locations = get_location_names_with_ids([
        "Mission 2: Fire and Light - Completion",
        "Mission 2: Fire and Light - OE Bronze" ,
        "Mission 2: Fire and Light - OE Silver" ,
        "Mission 2: Fire and Light - OE Gold"   ,
    ])
    mission_2.add_locations(mission_2_locations, IronNestLocation)

    mission_3_locations = get_location_names_with_ids([
        "Mission 3: Liberation - Completion",
        "Mission 3: Liberation - MF Bronze" ,
        "Mission 3: Liberation - MF Silver" ,
        "Mission 3: Liberation - MF Gold" ,
        "Mission 3: Liberation - MC Bronze" ,
        "Mission 3: Liberation - MC Silver" ,
        "Mission 3: Liberation - MC Gold" ,
        "Mission 3: Liberation - UV Bronze" ,
        "Mission 3: Liberation - UV Silver" ,
        "Mission 3: Liberation - UV Gold" ,
        "Mission 3: Liberation - AS Bronze" ,
        "Mission 3: Liberation - AS Silver" ,
        "Mission 3: Liberation - AS Gold" ,
    ])
    mission_3.add_locations(mission_3_locations, IronNestLocation)

    mission_4_locations = get_location_names_with_ids([
        "Mission 4: Counter-Battery - Completion",
        "Mission 4: Counter-Battery - SC Bronze" ,
        "Mission 4: Counter-Battery - SC Silver" ,
        "Mission 4: Counter-Battery - SC Gold" ,
        "Mission 4: Counter-Battery - CB Bronze" ,
        "Mission 4: Counter-Battery - CB Silver" ,
        "Mission 4: Counter-Battery - CB Gold" ,
        "Mission 4: Counter-Battery - AS Bronze" ,
        "Mission 4: Counter-Battery - AS Silver" ,
        "Mission 4: Counter-Battery - AS Gold" ,
        "Mission 4: Counter-Battery - NQ Bronze" ,
        "Mission 4: Counter-Battery - NQ Silver" ,
        "Mission 4: Counter-Battery - NQ Gold" ,
    ])
    mission_4.add_locations(mission_4_locations, IronNestLocation)

    mission_5_locations = get_location_names_with_ids([
        "Mission 5: Iron Road - Completion",
        "Mission 5: Iron Road - MF Bronze" ,
        "Mission 5: Iron Road - MF Silver" ,
        "Mission 5: Iron Road - MF Gold" ,
        "Mission 5: Iron Road - UV Bronze" ,
        "Mission 5: Iron Road - UV Silver" ,
        "Mission 5: Iron Road - UV Gold" ,
        "Mission 5: Iron Road - OE Bronze" ,
        "Mission 5: Iron Road - OE Silver" ,
        "Mission 5: Iron Road - OE Gold" ,
        "Mission 5: Iron Road - UF Bronze" ,
        "Mission 5: Iron Road - UF Silver" ,
        "Mission 5: Iron Road - UF Gold" ,
    ])
    mission_5.add_locations(mission_5_locations, IronNestLocation)

    mission_6_locations = get_location_names_with_ids([
        "Mission 6: Siege of Cartagena - Completion",
        "Mission 6: Siege of Cartagena - MF Bronze" ,
        "Mission 6: Siege of Cartagena - MF Silver" ,
        "Mission 6: Siege of Cartagena - MF Gold" ,
        "Mission 6: Siege of Cartagena - NQ Bronze" ,
        "Mission 6: Siege of Cartagena - NQ Silver" ,
        "Mission 6: Siege of Cartagena - NQ Gold" ,
        "Mission 6: Siege of Cartagena - UF Bronze" ,
        "Mission 6: Siege of Cartagena - UF Silver" ,
        "Mission 6: Siege of Cartagena - UF Gold" ,
        "Mission 6: Siege of Cartagena - AS Bronze" ,
        "Mission 6: Siege of Cartagena - AS Silver" ,
        "Mission 6: Siege of Cartagena - AS Gold" ,
    ])
    mission_6.add_locations(mission_6_locations, IronNestLocation)

    mission_7_locations = get_location_names_with_ids([
        "Mission 7: The Gorge - Completion",
        "Mission 7: The Gorge - MF Bronze" ,
        "Mission 7: The Gorge - MF Silver" ,
        "Mission 7: The Gorge - MF Gold" ,
        "Mission 7: The Gorge - NQ Bronze" ,
        "Mission 7: The Gorge - NQ Silver" ,
        "Mission 7: The Gorge - NQ Gold" ,
        "Mission 7: The Gorge - UV Bronze" ,
        "Mission 7: The Gorge - UV Silver" ,
        "Mission 7: The Gorge - UV Gold" ,
        "Mission 7: The Gorge - OE Bronze" ,
        "Mission 7: The Gorge - OE Silver" ,
        "Mission 7: The Gorge - OE Gold" ,
    ])
    mission_7.add_locations(mission_7_locations, IronNestLocation)

    mission_8_locations = get_location_names_with_ids([
        "Mission 8: Rock of Gibraltar - Completion",
        "Mission 8: Rock of Gibraltar - MF Bronze" ,
        "Mission 8: Rock of Gibraltar - MF Silver" ,
        "Mission 8: Rock of Gibraltar - MF Gold" ,
        "Mission 8: Rock of Gibraltar - NQ Bronze" ,
        "Mission 8: Rock of Gibraltar - NQ Silver" ,
        "Mission 8: Rock of Gibraltar - NQ Gold" ,
        "Mission 8: Rock of Gibraltar - UF Bronze" ,
        "Mission 8: Rock of Gibraltar - UF Silver" ,
        "Mission 8: Rock of Gibraltar - UF Gold" ,
        "Mission 8: Rock of Gibraltar - AS Bronze" ,
        "Mission 8: Rock of Gibraltar - AS Silver" ,
        "Mission 8: Rock of Gibraltar - AS Gold" ,
    ])
    mission_8.add_locations(mission_8_locations, IronNestLocation)

    mission_9_locations = get_location_names_with_ids([
        "Mission 9: Dead Reckoning - Completion",
        "Mission 9: Dead Reckoning - MF Bronze" ,
        "Mission 9: Dead Reckoning - MF Silver" ,
        "Mission 9: Dead Reckoning - MF Gold" ,
        "Mission 9: Dead Reckoning - NQ Bronze" ,
        "Mission 9: Dead Reckoning - NQ Silver" ,
        "Mission 9: Dead Reckoning - NQ Gold" ,
        "Mission 9: Dead Reckoning - UV Bronze" ,
        "Mission 9: Dead Reckoning - UV Silver" ,
        "Mission 9: Dead Reckoning - UV Gold" ,
        "Mission 9: Dead Reckoning - AS Bronze" ,
        "Mission 9: Dead Reckoning - AS Silver" ,
        "Mission 9: Dead Reckoning - AS Gold" ,
    ])
    mission_9.add_locations(mission_9_locations, IronNestLocation)

    mission_10_locations = get_location_names_with_ids([
        "Mission 10: Fire and Call - Completion",
        "Mission 10: Fire and Call - MF Bronze" ,
        "Mission 10: Fire and Call - MF Silver" ,
        "Mission 10: Fire and Call - MF Gold" ,
        "Mission 10: Fire and Call - NQ Bronze" ,
        "Mission 10: Fire and Call - NQ Silver" ,
        "Mission 10: Fire and Call - NQ Gold" ,
        "Mission 10: Fire and Call - UF Bronze" ,
        "Mission 10: Fire and Call - UF Silver" ,
        "Mission 10: Fire and Call - UF Gold" ,
        "Mission 10: Fire and Call - OE Bronze" ,
        "Mission 10: Fire and Call - OE Silver" ,
        "Mission 10: Fire and Call - OE Gold" ,
    ])
    mission_10.add_locations(mission_10_locations, IronNestLocation)

    mission_11_locations = get_location_names_with_ids([
        "Mission 11: High Tide - Completion",
        "Mission 11: High Tide - UV Bronze" ,
        "Mission 11: High Tide - UV Silver" ,
        "Mission 11: High Tide - UV Gold" ,
        "Mission 11: High Tide - SC Bronze" ,
        "Mission 11: High Tide - SC Silver" ,
        "Mission 11: High Tide - SC Gold" ,
        "Mission 11: High Tide - MC Bronze" ,
        "Mission 11: High Tide - MC Silver" ,
        "Mission 11: High Tide - MC Gold" ,
    ])
    mission_11.add_locations(mission_11_locations, IronNestLocation)

    mission_12_locations = get_location_names_with_ids([
        "Mission 12: Blind Fire - Completion",
        "Mission 12: Blind Fire - AS Bronze" ,
        "Mission 12: Blind Fire - AS Silver" ,
        "Mission 12: Blind Fire - AS Gold" ,
        "Mission 12: Blind Fire - NQ Bronze" ,
        "Mission 12: Blind Fire - NQ Silver" ,
        "Mission 12: Blind Fire - NQ Gold" ,
        "Mission 12: Blind Fire - UF Bronze" ,
        "Mission 12: Blind Fire - UF Silver" ,
        "Mission 12: Blind Fire - UF Gold" ,
        "Mission 12: Blind Fire - UV Bronze" ,
        "Mission 12: Blind Fire - UV Silver" ,
        "Mission 12: Blind Fire - UV Gold" ,
    ])
    mission_12.add_locations(mission_12_locations, IronNestLocation)

    mission_13_locations = get_location_names_with_ids([
        "Mission 13: Phantom Battery - Completion",
        "Mission 13: Phantom Battery - UF Bronze" ,
        "Mission 13: Phantom Battery - UF Silver" ,
        "Mission 13: Phantom Battery - UF Gold"   ,
        "Mission 13: Phantom Battery - NQ Bronze" ,
        "Mission 13: Phantom Battery - NQ Silver" ,
        "Mission 13: Phantom Battery - NQ Gold"   ,
        "Mission 13: Phantom Battery - MC Bronze" ,
        "Mission 13: Phantom Battery - MC Silver" ,
        "Mission 13: Phantom Battery - MC Gold"   ,
        "Mission 13: Phantom Battery - CB Bronze" ,
        "Mission 13: Phantom Battery - CB Silver" ,
        "Mission 13: Phantom Battery - CB Gold" ,
    ])
    mission_13.add_locations(mission_13_locations, IronNestLocation)

    mission_14_locations = get_location_names_with_ids([
        "Mission 14: Final Harvest - Completion",
        "Mission 14: Final Harvest - UF Bronze" ,
        "Mission 14: Final Harvest - UF Silver" ,
        "Mission 14: Final Harvest - UF Gold" ,
        "Mission 14: Final Harvest - NQ Bronze" ,
        "Mission 14: Final Harvest - NQ Silver" ,
        "Mission 14: Final Harvest - NQ Gold" ,
        "Mission 14: Final Harvest - MF Bronze" ,
        "Mission 14: Final Harvest - MF Silver" ,
        "Mission 14: Final Harvest - MF Gold" ,
        "Mission 14: Final Harvest - RE Bronze" ,
        "Mission 14: Final Harvest - RE Silver" ,
        "Mission 14: Final Harvest - RE Gold" ,
    ])
    mission_14.add_locations(mission_14_locations, IronNestLocation)

    mission_15_locations = get_location_names_with_ids([
        "Mission 15: White Shells - Ending 1",
        "Mission 15: White Shells - Ending 2",
        "Mission 15: White Shells - Ending 3",
        "Mission 15: White Shells - Ending 4",
    ])
    mission_15.add_locations(mission_15_locations, IronNestLocation)

#def create_events(world: IronNestWorld) -> None:
