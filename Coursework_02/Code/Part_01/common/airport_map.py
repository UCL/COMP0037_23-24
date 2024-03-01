'''
Created on 25 Jan 2022

@author: ucacsjj
'''

# This class stores a cleaning scenario. The scenario is used by the
# environment and the path planner

import math

from enum import Enum

from grid_search.cell_grid import Cell
from grid_search.cell_grid import CellGrid
from grid_search.search_grid import SearchGridCell


# Label which shows the semantic label of the cell based on what real-world
# object it contains. It is used to do things like work out traversability
# costs. Note the labels here are different from the ones you find in the
# SearchGrid for the forward search algorithm. Those are used for book-keeping.
class MapCellType(Enum):
    UNKNOWN = -1
    WALL = 0
    OPEN_SPACE = 1
    BAGGAGE_CLAIM = 2
    CUSTOMS_AREA = 3
    SECRET_DOOR = 4
    TOILET = 5
    CHARGING_STATION = 6
    RUBBISH_BIN = 7
    CHAIR = 8
    ROBOT_START_LOCATION = 9
    ROBOT_END_STATION = 10
    
# Class for the map cell.
class MapCell(Cell):

    # This is used to specify if a cell type obstructs the robot or not
    # Note that, to plan a path to a cell, we have to make that
    # cell not an obstruction
    _is_obstruction = {
        MapCellType.UNKNOWN: True,
        MapCellType.WALL: True,
        MapCellType.OPEN_SPACE: False,
        MapCellType.BAGGAGE_CLAIM: True,
        MapCellType.CUSTOMS_AREA: False,
        MapCellType.SECRET_DOOR: False,
        MapCellType.TOILET: True,
        MapCellType.CHARGING_STATION: False,
        MapCellType.RUBBISH_BIN: False,
        MapCellType.CHAIR: True,
        MapCellType.ROBOT_START_LOCATION: False,
        MapCellType.ROBOT_END_STATION: False
    }

    # A state is terminal or not depending upon its type 
    _is_terminal_state = {
        MapCellType.UNKNOWN: True,
        MapCellType.WALL: False,
        MapCellType.OPEN_SPACE: False,
        MapCellType.BAGGAGE_CLAIM: False,
        MapCellType.CUSTOMS_AREA: False,
        MapCellType.SECRET_DOOR: False,
        MapCellType.TOILET: False,
        MapCellType.CHARGING_STATION: False,
        MapCellType.RUBBISH_BIN: False,
        MapCellType.CHAIR: False,
        MapCellType.ROBOT_START_LOCATION: False,
        MapCellType.ROBOT_END_STATION: True
    }

    def __init__(self, coords, map_cell_type = MapCellType.OPEN_SPACE, params = None):
        
        Cell.__init__(self, coords)

        # The map cell type
        self._cell_type = map_cell_type
        
        self._p_slip = 0
        
        # Any parameters
        self._params = params
        

    # Return the coordinates of the cell
    def coords(self):
        return self._coords

    # Get the cell label
    def cell_type(self):
        return self._cell_type
    
    # Set the cell type        
    def set_cell_type(self, map_cell_type):
        self._cell_type = map_cell_type

    # Returns True if the cell type is one where the terminal action gets fired.    
    def is_terminal(self):
        return MapCell._is_terminal_state.get(self._cell_type)
    
    # Returns true if the robot cannot pass through this cell
    def is_obstruction(self):
        return MapCell._is_obstruction.get(self._cell_type)

    def set_p_slip(self, p_slip):
        self._p_slip = p_slip
        
    def p_slip(self):
        return self._p_slip

    # Other parameters
    def params(self):
        return self._params
    
    def set_params(self, params):
        self._params = params
        
        

# The airport map. This is an annotated grid which has extra
# parameters depending upon the type.
# You'll notice some areas are 'set_*' whereas others are 'add_*'.
# The idea is that you set properties of cells, but add objects

class AirportMap(CellGrid):
    '''
    classdocs
    '''

    def __init__(self, name, width, height):
        CellGrid.__init__(self, name, width, height)

        self._map = [[MapCell((x, y)) for y in range(self._height)] \
                     for x in range(self._width)]
                
        # set lists used to simplify stuff
        self._charging_stations = []
        
        self._rubbish_bins = []
        
        self._toilets = []        
                
        # Start without using the type-dependent traversability costs
        self._use_cell_type_traversability_costs = True
    
    def resolution(self):
        return 1

    # Get the cell object stored at a particular set of coordinates
    def cell(self, x, y):
        return self._map[x][y]
    
    def is_obstruction(self, x, y):
        return self._map[x][y].is_obstruction()
    
    def set_wall(self, x, y):
        self._map[x][y].set_cell_type(MapCellType.WALL)
        
    def set_open_space(self, x, y):
        self._map[x][y].set_cell_type(MapCellType.OPEN_SPACE)
            
    def set_customs_area(self, x, y):
        self._map[x][y].set_cell_type(MapCellType.CUSTOMS_AREA)

    def add_secret_door(self, x, y):#, door_cost):
        cell = self._map[x][y]
        cell.set_cell_type(MapCellType.SECRET_DOOR)
        door_cost = 0
        cell.set_params((door_cost))
        
    def add_robot_end_station(self, x, y, terminal_action_reward = 0):
        cell = self._map[x][y]
        cell.set_cell_type(MapCellType.ROBOT_END_STATION)
        cell.set_params((terminal_action_reward))        

    # Add a charging station
    def add_toilet(self, x, y):
        cell = self._map[x][y]
        cell.set_cell_type(MapCellType.TOILET)
        self._toilets.append(cell)
        
    def toilet(self, toilet_num):
        return self._toilets[toilet_num]
    
    def all_toilets(self):
        return self._toilets

    # Add a charging station
    def add_charging_station(self, x, y, mean, covariance):
        cell = self._map[x][y]
        cell.set_cell_type(MapCellType.CHARGING_STATION)
        cell.set_params({"mean": mean, "covariance" : covariance, "p_slip" : 0})
        self._charging_stations.append(cell)
        
    def charging_station(self, station_num):
        return self._charging_stations[station_num]
    
    def all_charging_stations(self):
        return self._charging_stations
        
    # Add a charging station
    def add_rubbish_bin(self, x, y):
        cell = self._map[x][y]
        cell.set_cell_type(MapCellType.RUBBISH_BIN)
        self._rubbish_bins.append(cell)
        
    def rubbish_bin(self, rubbish_bin_num):
        return self._rubbish_bins[rubbish_bin_num]
    
    def all_rubbish_bins(self):
        return self._rubbish_bins
    
    def set_cell_type(self, x, y, cell_type):
        self._map[x][y].set_cell_type(cell_type)
        
    def set_use_cell_type_traversability_costs(self, use_cell_type_traversability_costs):
        self._use_cell_type_traversability_costs = use_cell_type_traversability_costs
    
    def compute_transition_cost(self, last_coords, current_coords):
        
        # Compute the basic Euclidean cost
        dX = current_coords[0] - last_coords[0]
        dY = current_coords[1] - last_coords[1]
        L = math.sqrt(dX * dX + dY * dY)
            
        return L
        
    def populate_search_grid(self, search_grid):
        grid = [[SearchGridCell((x, y), self._map[x][y].is_obstruction()) for y in range(self._height)] \
                     for x in range(self._width)]
       
        for x in range(self._width):
            for y in range(self._height):
                type = self._map[x][y].cell_type()
                if self._map[x][y].cell_type() is MapCellType.ROBOT_START_LOCATION:
                    grid[x][y].is_start = True
                elif self._map[x][y].cell_type() is MapCellType.ROBOT_END_STATION:
                    grid[x][y].is_goal = True
                    
        search_grid._set_search_grid(grid)

    
