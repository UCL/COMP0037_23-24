from enum import Enum

from .cell_grid import Cell, CellGrid

# The label which can be assigned to this cell

class SearchGridCellLabel(Enum):
    UNVISITED=0
    DEAD=1
    ALIVE=2

# This class stores information about each cell - its coordinates in the grid,
# its label, and the path cost to reach it. It includes a few extra field which
# help with stuff like plotting as well.

class SearchGridCell(Cell):

    def __init__(self, coords, is_obstruction):

        Cell.__init__(self, coords)
        
        # The cell is initially given the label that it's not been visited.
        self._label = SearchGridCellLabel.UNVISITED

        # Flag if the cell is obstructed
        self._is_obstruction = is_obstruction
         
        # Initially the cell has no parents.
        self.parent = None

        # The initial path cost is infinite. For algorithms that need
        # it, this is the necessary initial condition.
        self.path_cost = float("inf")
        
        # Flags to show if the cell is at the start or the goal        
        self.is_start = False
        self.is_goal = False
        
        # These variables are used for plotting
        self.is_on_path = False
        self.parent_changed = False

    def coords(self):
        return self._coords

    # Get the cell label
    def label(self):
        return self._label

    # Revise the label        
    def set_label(self, label):
        self._label = label

    def is_obstruction(self):
        return self._is_obstruction
        
    # If it has changed, change the parent to this cell    
    def set_parent(self, parent):
        
        # Nothing to do if the same
        if self.parent == parent:
            return 
        
        self.parent = parent
        self.parent_changed = True
        
    # Tie breaker; normally you'd make it random, but this is to 
    # give deterministic behaviour
    def __lt__(self, other):
        return True

class SearchGrid(CellGrid):

    # This class stores the state of a search grid to illustrate forward search

    def __init__(self, width, height, resolution):
        CellGrid.__init__(self, "Search Grid", width, height)
        self._resolution = resolution

        # Construct the class using an occupancy grid object
    @classmethod
    def from_environment_map(cls, environment_map):

        (self) = cls(environment_map.width(), environment_map.height(), environment_map.resolution())

        # Populate the search grid from the occupancy grid
        self.set_from_environment_map(environment_map)
        
        return self

    # Reset the state of the search grid to the value of the occupancy grid
    def set_from_environment_map(self, environment_map):
        environment_map.populate_search_grid(self)        

    def cell(self, x, y):
        return self._grid[x][y]

    def cell_from_coords(self, coords):
        return self._grid[coords[0]][coords[1]]
    
    def _set_search_grid(self, search_grid):
        self._grid = search_grid
