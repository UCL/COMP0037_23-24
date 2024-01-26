import math

from .cell_grid import CellGrid
from .helpers import clamp
from .search_grid import SearchGridCell

# This class stores the occupancy grid. This is a "chessboard-like"
# representation of the environment. The environment is represented by
# a set of square cells. Each cell encodes whether that bit of the
# environment is free, or whether it is blocked. A "0" says that a
# cell is free and so the robot can travel over it. A "1" means that
# it is blocked and the robot cannot travel over it.

class OccupancyGrid(CellGrid):

    # Construct a new occupancy grid with a given width and
    # height. The resolution says the lenght of the side of each cell
    # in metres. By default, all the cells are set to "0" which means
    # that there are no obstacles.
    def __init__(self, name, width, height, resolution):
        CellGrid.__init__(self, name, width, height)
        self._resolution = resolution
        self._data = [[0 for x in range(width)] for y in range(height)]

    # The resolution of each cell (the length of its side in metres)
    def resolution(self):
        return self._resolution

    # Get the status of a cell.
    def cell(self, x, y):
        return self._data[y][x]

    # Set the status of a cell.
    def set_cell(self, x, y, c):
        self._data[y][x] = c
    
    def compute_transition_cost(self, last_coords, current_coords):
        
        dX = current_coords[0] - last_coords[0]
        dY = current_coords[1] - last_coords[1]
        return math.sqrt(dX * dX + dY * dY)
    
    # Take a position in world coordinates (i.e., m) and turn it into
    # cell coordinates. Clamp the value so that it always falls within
    # the grid. The conversion uses integer rounding.
    def get_cell_coordinates_from_world_coordinates(self, worldCoords):

        cellCoords = (clamp(int(worldCoords[0] / self._resolution), 0, self._width - 1), \
                      clamp(int(worldCoords[1] / self._resolution), 0, self._height - 1))
        
        return cellCoords
    
    # Convert a position in cell coordinates to world coordinates. The
    # conversion uses the centre of a cell, hence the mysterious 0.5
    # addition. No clamping is currently done.
    def get_world_coordinates_from_cell_coordinates(self, cellCoords):

        worldCoords = ((cellCoords[0] + 0.5) * self._resolution, \
                      (cellCoords[1] + 0.5) * self._resolution)

        return worldCoords
    
    def populate_search_grid(self, search_grid):
        grid = [[SearchGridCell((x, y), (self._data[y][x] > 0)) for y in range(self._height)] \
                     for x in range(self._width)]
        
        search_grid._set_search_grid(grid)
