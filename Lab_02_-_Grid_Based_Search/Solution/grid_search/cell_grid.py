from .helpers import clamp

from .grid import Grid

# A cell grid consists of a set of cells ordered in a 2D array. The type of
# cells depends on what's used


class Cell:
    def __init__(self, coords):
        self._coords = coords

    def coords(self):
        return self._coords


class CellGrid(Grid):

    def __init__(self, name: str, width: int, height: int):
        Grid.__init__(self, name, width, height)

    def compute_transition_cost(self, last_coords, current_coords):
        raise NotImplementedError()

    # Get the status of a cell.
    def cell(self, x, y):
        raise NotImplementedError()

    # Set the status of a cell.
    def set_cell(self, x, y, c):
        raise NotImplementedError()
