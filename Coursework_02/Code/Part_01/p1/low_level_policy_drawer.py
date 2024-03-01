'''
Created on 30 Jan 2022

@author: ucacsjj
'''

from grid_search.graphics import *

from grid_search.grid_drawer import GridDrawer

from .low_level_actions import LowLevelActionType

# Draw the computed policy. This consists of a set of a set of arrows showing the nominal
# trajectory will show at each location.

class LowLevelPolicyDrawer(GridDrawer):

    def __init__(self, driving_policy, maximum_grid_drawer_window_height_in_pixels, top_left_in_pixels = None):

        GridDrawer.__init__(self, driving_policy, maximum_grid_drawer_window_height_in_pixels, top_left_in_pixels)
  
        self._action_glyph = {}
        
        # If set to true, sample the action using e-greedy rather than 
        # show the greedy optimal action
        self._render_sampled_action = False
        
        # Direction perturbations; same as in the environment
        self._driving_deltas=(
            (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))        
                
    def render_sampled_action(self, render_sampled_action):
        self._render_sampled_action = render_sampled_action
                
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

    def _update(self, render_move_actions):

        ### Figure out the width and height
        width = self._grid.width();
        height = self._grid.height();

        for x in range(width):
            for y in range(height):
                
                # Coordinates; mostly used as a key for the dictionary
                cell_coords = (x, y)
                
                # Get the action at the cell
                if self._render_sampled_action is True:
                    action = self._grid.action(x, y)
                else:
                    action = self._grid.greedy_optimal_action(x, y)
                
                # Current cell coordinates in pixels                
                current_x = (x + 0.5) * self._cell_size
                current_y = (height - y - 0.5) * self._cell_size
                current_point = Point(current_x, current_y)
                
                # Flag to say if we've already handled this action
                glyph_already_drawn = cell_coords in self._action_glyph
                
                # These actions only apply inside obstructions
                if action == LowLevelActionType.NONE:
                    if glyph_already_drawn is False:
                        circle = Circle(current_point, 0.15 * self._cell_size)
                        circle.setFill("black")
                        circle.draw(self._win)
                        self._action_glyph[cell_coords] = circle
                    continue                
                
                # If the action is terminate, draw a circle
                if action == LowLevelActionType.TERMINATE:
                    if glyph_already_drawn is False:
                        circle = Circle(current_point, 0.25 * self._cell_size)
                        circle.setFill("red")
                        circle.draw(self._win)
                        self._action_glyph[cell_coords] = circle
                    continue
                
                # Move actions are from here on down, so skip them if not rendering this time
                if render_move_actions is False:
                    continue
                
                # Driving action; figure out the direction and draw the arrow if needed              
                deltas = self._driving_deltas[action]
                
                # Work out the end location                
                end_x = (x + deltas[0] + 0.5) * self._cell_size
                end_y = (height - y - deltas[1] - 0.5) * self._cell_size
                end_point = Point(end_x, end_y)
                
                # Create an arrow if we need to
                if glyph_already_drawn is True:
                    arrow = self._action_glyph[cell_coords]
                    arrow.undraw()
                    
                    # If it turns out this is the wrong type, remove and recreate
                    if isinstance(arrow, Line) is False:
                        arrow = Line(current_point, end_point)
                        arrow.setArrow('last')
                        arrow.setOutline('red')
                        self._action_glyph[cell_coords] = arrow
                    else:
                        arrow.p2 = end_point
                else:
                    arrow = Line(current_point, end_point)
                    arrow.setArrow('last')
                    arrow.setOutline('red')
                    self._action_glyph[cell_coords] = arrow
                    
                arrow.draw(self._win)   
                
        # Flush the drawing right at the very end for speed
        self._win.flush()
                
       