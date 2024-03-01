'''
Created on 25 Jan 2022

@author: ucacsjj
'''

from common.airport_map import MapCellType
from common.airport_map import AirportMap

# This file contains a set of functions which build different maps. Only
# two of these are needed for the coursework. Others are ones which were
# used for developing and testing the algorithms and might be of use.

# Helper function which fills sets the type of all cells in a rectangular
# region to have the same type.
def _set_block_to_single_type(airport_map, cell_type, start_coords, end_coords):
    for x in range(start_coords[0], end_coords[0] + 1):
        for y in range(start_coords[1], end_coords[1] + 1):
            airport_map.set_cell_type(x, y, cell_type)
            
            
def _set_block_to_same_p_slip(airport_map, p_slip, start_coords, end_coords):
    for x in range(start_coords[0], end_coords[0] + 1):
        for y in range(start_coords[1], end_coords[1] + 1):
            airport_map.cell(x, y).set_p_slip(p_slip)

# This scenario can be used to test the different traversability costs
def test_traversability_costs_scenario():
    
    airport_map = AirportMap("Test Traversabilty Map", 15, 15)

    for x in range(0, 14):
        airport_map.set_wall(x, 7)  
           
    airport_map.add_secret_door(7, 7)
    
    return airport_map, 200

def test_one_row_scenario():
    
    airport_map = AirportMap("One Row Scenario", 5, 1)
    
    airport_map.add_robot_end_station(4, 0, 0)
    
    return airport_map, 200
     
def test_two_row_scenario():
    
    airport_map = AirportMap("Two Row Scenario", 15, 2)
    
    airport_map.add_robot_end_station(14, 0, 0)
    
    return airport_map, 150
          
def test_three_row_scenario():
    airport_map = AirportMap("Three Row Scenario", 15, 3)
    
    airport_map.set_cell_type(2, 1, MapCellType.WALL)
    
    airport_map.add_robot_end_station(14, 0, 100)
    
    return airport_map, 150


def test_2x2_scenario():
    
    airport_map = AirportMap("2x2 Scenario", 2, 2)
    
    airport_map.add_robot_end_station(0, 1, 100)
    
    return airport_map, 400
          
          
def test_3x3_scenario():
    
    airport_map = AirportMap("3x3 Scenario", 3, 3)
    
    airport_map.add_robot_end_station(0, 2, 100)
    
    return airport_map, 400

def corridor_scenario():
    airport_map = AirportMap("Corridor Scenario", 20, 7)
    
    _set_block_to_single_type(airport_map, MapCellType.WALL, (0, 0), (19, 0))
    _set_block_to_single_type(airport_map, MapCellType.WALL, (0, 6), (19, 6))
    
    _set_block_to_single_type(airport_map, MapCellType.CHAIR, (2, 1), (5, 1))
    
    for y in range(3,7):
        airport_map.add_robot_end_station(19, y, 100)
    #_set_block_to_single_type(airport_map, MapCellType.ROBOT_END_STATION, (19, 0), (19, 6))
    
    return airport_map, 450  
     
def test_nearest_charging_station_scenario():

    airport_map = AirportMap("Test Nearest Charging Station", 45, 15)
    airport_map.add_charging_station(0, 7, 1, 1)
    airport_map.add_charging_station(44, 7, 1, 1)
    
    return airport_map, 200

def mini_scenario():
    
    # Create the map
    airport_map = AirportMap("Mini Scenario", 15, 15)
    
    # Create the wall on either side and the customs area
    for x in range(0, 15):
        airport_map.set_wall(x, 7)
        
    for x in range(5, 7):        
        airport_map.set_customs_area(x, 7)
    
    airport_map.add_charging_station(4, 4, 1, 1)
    
    airport_map.add_secret_door(14, 7)
    
    airport_map.add_toilet(4, 1)
    
    airport_map.add_robot_end_station(0, 14, 0)
    
    return airport_map, 200

def full_scenario():

    airport_map = AirportMap("Full Scenario", 60, 40)
    
    # The wall separating the two areas, including the customs area
    # and the secret door
    _set_block_to_single_type(airport_map, MapCellType.WALL, (0, 18), (59, 20))
    _set_block_to_single_type(airport_map, MapCellType.CUSTOMS_AREA, (25, 18), (35, 20))    
    _set_block_to_single_type(airport_map, MapCellType.SECRET_DOOR, (59, 18), (59, 20))

    # The reclaim areas
    airport_map.add_rubbish_bin(2, 33)
    _set_block_to_single_type(airport_map, MapCellType.BAGGAGE_CLAIM, (5, 30), (8, 36))
    airport_map.add_rubbish_bin(11, 33)
    _set_block_to_single_type(airport_map, MapCellType.BAGGAGE_CLAIM, (15, 28), (18, 39))
    airport_map.add_rubbish_bin(22, 38)
    _set_block_to_single_type(airport_map, MapCellType.BAGGAGE_CLAIM, (25, 28), (28, 39))
    airport_map.add_rubbish_bin(31, 38)
    _set_block_to_single_type(airport_map, MapCellType.BAGGAGE_CLAIM, (35, 28), (38, 39))
    airport_map.add_rubbish_bin(41, 38)
    _set_block_to_single_type(airport_map, MapCellType.BAGGAGE_CLAIM, (45, 28), (48, 39))
    airport_map.add_rubbish_bin(51, 33)
    _set_block_to_single_type(airport_map, MapCellType.BAGGAGE_CLAIM, (55, 30), (58, 36))
    
    # The bins in the reclaim areas

    # Add the horizontal chairs with bins at either end
    for i in range(5):
        y_coord = 2 + i * 3
        _set_block_to_single_type(airport_map, MapCellType.CHAIR, (5, y_coord), (18, y_coord))
        airport_map.add_rubbish_bin(4, y_coord)
        airport_map.add_rubbish_bin(19, y_coord)

    # Add the vertical chairs with bins at either end
    for i in range(5):
        x_coord = 42 + i * 3
        _set_block_to_single_type(airport_map, MapCellType.CHAIR, (x_coord, 2), (x_coord, 14))
        airport_map.add_rubbish_bin(x_coord, 1)
        airport_map.add_rubbish_bin(x_coord, 15)


    # The toilets. These generate rubbish to be collected
    airport_map.add_toilet(0, 21)
    airport_map.add_toilet(0, 17)
    airport_map.add_toilet(38, 0)
    airport_map.add_toilet(58, 21)   
   
    # These charge the robot back up again
    airport_map.add_charging_station(1, 38, 15, 1)
    airport_map.add_charging_station(58, 38, 15, 1)
    airport_map.add_charging_station(36, 0, 30, 1)
    airport_map.add_charging_station(59, 0, 40, 1)
    
    airport_map.add_robot_end_station(1, 21, 50)
    
    return airport_map, 800

def t0_waiting_area():
    
    airport_map = AirportMap("Waiting Area T0", 3, 4)
    
    airport_map.set_cell_type(0, 0, MapCellType.ROBOT_START_LOCATION)
    airport_map.set_cell_type(1, 0, MapCellType.ROBOT_START_LOCATION)
    airport_map.set_cell_type(1, 1, MapCellType.RUBBISH_BIN)
    airport_map.set_cell_type(2, 2, MapCellType.ROBOT_END_STATION)
    airport_map.set_cell_type(2, 3, MapCellType.ROBOT_END_STATION)
    
    airport_map.cell(0, 2).set_p_slip(0.8)
    
    return airport_map, 200

def slippy_corridor():
    # Get the basic corridor
    airport_map, drawer_height = corridor_scenario()

    # Now modify it to add a large slippery block in the middle
    _set_block_to_same_p_slip(airport_map, 0.5, (5, 3), (18, 5))

    return airport_map, drawer_height

def all_scenarios():

    scenario_generators = [test_traversability_costs_scenario, \
                               test_one_row_scenario, \
                               test_two_row_scenario, \
                               test_three_row_scenario, \
                               mini_scenario, \
                               full_scenario]

    return scenario_generators
