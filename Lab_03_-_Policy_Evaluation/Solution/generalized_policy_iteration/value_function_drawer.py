'''
Created on 3 Feb 2022

@author: ucacsjj
'''

import math

from grid_search.graphics import *

from grid_search.grid_drawer import GridDrawer

class ValueFunctionDrawer(GridDrawer):

    def __init__(self, value_function, maximum_grid_drawer_window_height_in_pixels, \
                 top_left_in_pixels = None):

        GridDrawer.__init__(self, value_function, maximum_grid_drawer_window_height_in_pixels, \
                            top_left_in_pixels)
        
        # Not very efficient way to do it!
        self._last_values = {}
        self._value_texts = {}
        
        # The font size
        self._font_size = 5
        
        # The minimum change in value to trigger the red text appearing
        self._value_change_threshold = 5e-3
        
    def reset(self):
        for value_text in self._value_texts.values():
            value_text.undraw()
        self._value_texts = {}
        self._last_values = {}
        
    def set_font_size(self, new_font_size):
        
        if new_font_size != self._font_size:
            self._font_size = new_font_size
            self.reset()
            self.update()
            
    def set_value_change_threshold(self, value_change_threshold):
        self._value_change_threshold = value_change_threshold
       
    def update(self):
        ### Figure out the width and height
        width = self._grid.width();
        height = self._grid.height();

        for x in range(width):
            for y in range(height):
                
                # Coordinates; mostly used as a key for the dictionary
                cell_coords = (x, y)
                
                # Get the value at the cell
                value = self._grid.value(x, y)
                
                # Flag to say if we've already handled this action
                value_txt_already_drawn = cell_coords in self._value_texts
                
                # Format the value text
                value_text_string = "{0:.3g}".format(value)
                
                if value_txt_already_drawn is True:
                    text_label = self._value_texts[cell_coords]
                    if math.fabs(self._last_values[cell_coords] - value) > self._value_change_threshold:
                        text_label.setText(value_text_string)
                        text_label.setTextColor('red')
                        self._last_values[cell_coords] = value
                    else:
                        text_label.setTextColor('black')
                else:
                    current_x = (x + 0.5) * self._cell_size
                    current_y = (height - y - 0.5) * self._cell_size
                    current_point = Point(current_x, current_y)
                    text_label = Text(current_point, value_text_string)
                    text_label.setSize(self._font_size)
                    text_label.draw(self._win)
                    text_label.setTextColor('red')
                    self._value_texts[cell_coords] = text_label
                    self._last_values[cell_coords] = value
                    if math.isnan(value) is True:
                        self._rectangles[y][x].setFill('gray68')
        
        # Flush the drawing right at the very end for speed
        self._win.flush()


 
        