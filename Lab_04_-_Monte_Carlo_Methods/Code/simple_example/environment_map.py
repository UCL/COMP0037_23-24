'''
Created on 31 Jan 2023

@author: ucacsjj
'''

# The classes here are used to encode the scenario. The code here is a
# simplified version of what's in the coursework to help you get to
# grips with it.

from enum import Enum

from grid_search.cell_grid import Cell
from grid_search.cell_grid import CellGrid

# Label which shows the semantic label of the cell based on what real-world
# object it contains.
class MapCellType(Enum):
    UNKNOWN = -1
    OBSTACLE = 0
    OPEN_SPACE = 1
    GOAL = 2
    PIT_OF_DOOM = 3

# Class for the map cell.
class MapCell(Cell):

    # This is used to specify if a cell type obstructs the robot or not
    # Note that, to plan a path to a cell, we have to make that
    # cell not an obstruction
    _is_obstruction = {
        MapCellType.UNKNOWN: True,
        MapCellType.OBSTACLE: True,
        MapCellType.OPEN_SPACE: False,
        MapCellType.GOAL: False,
        MapCellType.PIT_OF_DOOM: False
    }

    # A state is terminal or not depending upon its type 
    _is_terminal_state = {
        MapCellType.UNKNOWN: True,
        MapCellType.OBSTACLE: False,
        MapCellType.OPEN_SPACE: False,
        MapCellType.GOAL: True,
        MapCellType.PIT_OF_DOOM: True
    }

    def __init__(self, coords, map_cell_type = MapCellType.OPEN_SPACE, params = None):
        
        Cell.__init__(self, coords)

        # The map cell type
        self._cell_type = map_cell_type
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

    # Other parameters
    def params(self):
        return self._params
    
    def set_params(self, params):
        self._params = params


class EnvironmentMap(CellGrid):
    '''
    classdocs
    '''

    def __init__(self, name, width, height):
        CellGrid.__init__(self, name, width, height)
        
        self._map = [[MapCell((x, y), params=-1) for y in range(self._height)] \
                 for x in range(self._width)]
        
    # Get the cell object stored at a particular set of coordinates
    def cell(self, x, y):
        return self._map[x][y]
    
    def is_obstruction(self, x, y):
        return self._map[x][y].is_obstruction()
        
    def add_goal(self, x, y, goal_reward = 100):
        cell = self._map[x][y]
        cell.set_cell_type(MapCellType.GOAL)
        cell.set_params(goal_reward)

    def add_hole(self, x, y, goal_reward = -100):
        cell = self._map[x][y]
        cell.set_cell_type(MapCellType.PIT_OF_DOOM)
        cell.set_params(goal_reward)
        
    def add_obstacle(self, x, y):
        cell = self._map[x][y]
        cell.set_cell_type(MapCellType.OBSTACLE)
