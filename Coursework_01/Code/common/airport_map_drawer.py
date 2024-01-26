'''
Created on 25 Jan 2022

@author: ucacsjj
'''

from grid_search.grid_drawer import GridDrawer

#from .airport_map import MapCell
from .airport_map import MapCellType

#from .airport_map import AirportMap

class AirportMapDrawer(GridDrawer):

    def __init__(self, airport_map, maximum_grid_drawer_window_height_in_pixels, top_left_in_pixels = None):

        GridDrawer.__init__(self, airport_map, maximum_grid_drawer_window_height_in_pixels, top_left_in_pixels)

        # This dictionary is used to map the cell type to a colour        
        self._draw_colours = {
            MapCellType.UNKNOWN:'gray',
            MapCellType.WALL:'purple',
            MapCellType.OPEN_SPACE:'azure3',
            MapCellType.BAGGAGE_CLAIM:'deep sky blue',
            MapCellType.CUSTOMS_AREA:'firebrick1',
            MapCellType.SECRET_DOOR:'yellow',
            MapCellType.TOILET:'brown',
            MapCellType.CHARGING_STATION:'green',
            MapCellType.RUBBISH_BIN:'dark goldenrod',
            MapCellType.CHAIR:'medium orchid'
        }
        
    def _draw_colour(self, cell):
        return self._draw_colours.get(cell.cell_type(), 'black')
                
    def update(self):

        ### Figure out the width and height
        width = self._grid.width();
        height = self._grid.height();

        # Go through and shade all the cells according to their type
        for i in range(width):
            for j in range(height):
                
                # First update the grid cell
                cell = self._grid.cell(i, j)                
                # Switch and case statement
                colour = self._draw_colour(cell)
                                
                self._rectangles[j][i].setFill(colour)
                
        # Flush the drawing right at the very end for speed
        self._win.flush()
        