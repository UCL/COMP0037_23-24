import random

from .graphics import *
from .grid_drawer import GridDrawer
from .search_grid import SearchGridCellLabel


class SearchGridDrawer(GridDrawer):

    def __init__(self, search_grid, maximum_grid_drawer_window_height_in_pixels, top_left_in_pixels = None, draw_parent_arrows = True):

        GridDrawer.__init__(self, search_grid, maximum_grid_drawer_window_height_in_pixels, top_left_in_pixels)

        self._draw_parent_arrows = draw_parent_arrows
                
        if (self._draw_parent_arrows is True):
            self._parent_arrows = {}
                
    def reset(self):
        for arrow in self._parent_arrows.values():
            arrow.undraw()
        self._parent_arrows = {}
                
    def update(self):

        ### Figure out the width and height
        width = self._grid.width();
        height = self._grid.height();

        for i in range(width):
            for j in range(height):
                
                # First update the grid cell
                cell = self._grid.cell_from_coords((i, j))
                cell_label = cell.label()
                if cell.is_obstruction() is True:
                    color = 'purple'
                elif cell.is_start is True:
                    color = 'red'
                elif cell.is_goal is True:
                    color = 'green'
                elif cell.is_on_path is True:
                    color = 'yellow'
                elif cell_label == SearchGridCellLabel.UNVISITED:
                    color = 'gray'
                elif cell_label == SearchGridCellLabel.DEAD:
                    color = 'black'
                else:
                    color = 'white'
                self._rectangles[j][i].setFill(color);
                
                # Now handle drawing the parent arrow if required
                if (self._draw_parent_arrows is False):
                    continue
                
                # If we have no parent continue
                if (cell.parent is None):
                    continue

                # Get the coordinates
                cell_coords = cell.coords()
                parent_cell_coords = cell.parent.coords()

                # If we have a parent object, and the parent has changed, redraw the arrow
                # Note that the graphics doesn't have an API to do this, so had to hack it
                if (cell in self._parent_arrows):
                    parent_arrow = self._parent_arrows[cell]
                    if (cell.parent_changed is True):
                        parent_arrow.undraw()
                        parent_arrow.p2 = Point((parent_cell_coords[0] + 0.5)* self._cell_size, \
                                               (height - parent_cell_coords[1] - 0.5) * self._cell_size)
                        cell.parent_changed = False
                        parent_arrow.setOutline('red')
                        parent_arrow.draw(self._win)
                        
                    else:
                        parent_arrow.setOutline('cyan')

                    continue
                
                # Create a new parent arrow and draw it
                parent_arrow = Line(Point((cell_coords[0] + 0.5)* self._cell_size, \
                                         (height - cell_coords[1] - 0.5) * self._cell_size), \
                                   Point((parent_cell_coords[0] + 0.5)* self._cell_size, \
                                         (height - parent_cell_coords[1] - 0.5) * self._cell_size))
                
                parent_arrow.setArrow('last')
                parent_arrow.setOutline('red')
                self._parent_arrows[cell] = parent_arrow
                parent_arrow.draw(self._win)                

        # Flush the drawing right at the very end for speed
        self._win.flush()
 
