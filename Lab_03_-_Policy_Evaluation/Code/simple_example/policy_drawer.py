'''
Created on 30 Jan 2022

@author: ucacsjj
'''

from typing import Optional

from grid_search.graphics import *

from grid_search.grid_drawer import GridDrawer

from .action_types import ActionTypes
from .policy import TabularPolicy

# Draw the computed policy. This consists of a set of a set of arrows showing the nominal
# trajectory will show at each location.

class PolicyDrawer(GridDrawer):

    def __init__(self, policy: TabularPolicy, maximum_grid_drawer_window_height_in_pixels: int,
                 top_left_in_pixels: Optional[int] = None):

        GridDrawer.__init__(self, policy, maximum_grid_drawer_window_height_in_pixels, top_left_in_pixels)
  
        self._action_glyph = {} # type: ignore
        
        # Direction perturbations; space as action types
        self._driving_deltas=(
             (1, 0), (0, 1), (-1, 0), (0, -1), (0, 0))
        
        self.update()     
                
    def reset(self):
        for arrow in self._action_glyph.values():
            arrow.undraw()
        self._action_glyph = {}
       
    def update(self):
        
        # Do two passes to order the rendering. In the first pass,
        # render the non-movement actions. In the second pass,
        # render the movement actions
        
        self._update(False)
        self._update(True)
        
    def _update(self, render_move_actions: bool):

        ### Figure out the width and height
        width = self._grid.width();
        height = self._grid.height();

        for x in range(width):
            for y in range(height):
                
                # Coordinates; mostly used as a key for the dictionary
                cell_coords = (x, y)
                
                # Get the action at the cell
                action = self._grid.action(x, y) # type: ignore
                
                # Current cell coordinates in pixels                
                current_x = (x + 0.5) * self._cell_size
                current_y = (height - y - 0.5) * self._cell_size
                current_point = Point(current_x, current_y)
                
                # Flag to say if we've already handled this action
                glyph_already_drawn = cell_coords in self._action_glyph

                # These actions only apply inside obstructions
                if action is ActionTypes.NONE:
                    if glyph_already_drawn is False:
                        circle = Circle(current_point, 0.15 * self._cell_size)
                        circle.setFill("black")
                        circle.draw(self._win)
                        self._action_glyph[cell_coords] = circle
                    continue
                
                # If the action is terminate, draw a circle
                if action is ActionTypes.TERMINATE:
                    if glyph_already_drawn is False:
                        circle = Circle(current_point, 0.25 * self._cell_size)
                        circle.setFill("red")
                        circle.draw(self._win)
                        self._action_glyph[cell_coords] = circle
                    continue
                
                if render_move_actions is False:
                    continue
                
                # If the action type is wait, draw a small square
                if action is ActionTypes.WAIT:
                    if glyph_already_drawn is False:
                        rectangle = Rectangle(current_point, 0.25 * self._cell_size)
                        rectangle.setFill("red")
                        rectangle.draw(self._win)
                        self._action_glyph[cell_coords] = rectangle
                    continue
                   
                # Driving action; figure out the direction and draw the arrow if needed                
                deltas = self._driving_deltas[action]
                
                # Work out the end location; we truncate this to the grid
                # size so that movements off the edge of the grid aren't just
                # a straight line going nowhere
                end_x = max(min(x + deltas[0] + 0.5, width), 0) * self._cell_size
                end_y = max(min(height - y - deltas[1] - 0.5, height), 0) * self._cell_size
                end_point = Point(end_x, end_y)
                
                # Create an arrow if we need to
                if glyph_already_drawn is True:
                    arrow = self._action_glyph[cell_coords]
                    arrow.undraw()
                    arrow.p2 = end_point
                else:                
                    arrow = Line(current_point, end_point)
                    arrow.setArrow('last')
                    arrow.setOutline('green')
                    self._action_glyph[cell_coords] = arrow
                    
                arrow.draw(self._win)   
                
        # Flush the drawing right at the very end for speed
        self._win.flush()
                
       
