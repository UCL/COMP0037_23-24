from enum import Enum
from typing import Tuple
from typing import Optional
from typing import Union
from typing import Literal

from .cell_grid import Cell
from .cell_grid import CellGrid
from .occupancy_grid import OccupancyGrid
# The label which can be assigned to this cell


class SearchGridCellLabel(Enum):
    UNVISITED = 0
    DEAD = 1
    ALIVE = 2

# This class stores information about each cell - its coordinates in the grid,
# its label, and the path cost to reach it. It includes a few extra field which
# help with stuff like plotting as well.


class SearchGridCell(Cell):

    def __init__(self, coords: Tuple[int, int], is_obstruction: bool):

        Cell.__init__(self, coords)

        # The cell is initially given the label that it's not been visited.
        self._label: SearchGridCellLabel = SearchGridCellLabel.UNVISITED

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

    def coords(self) -> Tuple[int, int]:
        return self._coords

    # Get the cell label
    def label(self) -> SearchGridCellLabel:
        return self._label

    # Revise the label
    def set_label(self, label: SearchGridCellLabel):
        self._label = label

    def is_obstruction(self) -> bool:
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

    def __init__(self, width: int, height: int, resolution: float):
        CellGrid.__init__(self, "Search Grid", width, height)
        self._resolution = resolution

        
    # 
    def populate_from_occupancy_grid(self, occupancy_grid: OccupancyGrid):
        self._grid = [[SearchGridCell((x, y), (occupancy_grid._data[y][x] > 0)) for y in range(occupancy_grid._height)]
                for x in range(occupancy_grid._width)]
        
        # Construct the class using an occupancy grid object
    @classmethod
    def from_occupancy_grid(cls, occupancy_grid: OccupancyGrid):

        (self) = cls(occupancy_grid.width(),
                     occupancy_grid.height(), occupancy_grid.resolution())

        # Populate the search grid from the occupancy grid
        self.populate_from_occupancy_grid(occupancy_grid)

        return self

    def cell(self, x: int, y: int):
        return self._grid[x][y]

    def cell_from_coords(self, coords: Tuple[int, int]) -> SearchGridCell:
        return self._grid[coords[0]][coords[1]]

    # mypy can't handle the type check here
    def _set_search_grid(self, search_grid):
        self._grid = search_grid

