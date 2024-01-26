'''
Created on 26 Jan 2022

@author: ucacsjj
'''

class Grid:

    def __init__(self, name, width, height):
        self._name = name
        self._width = width
        self._height = height

    # The width of the occupancy map in cells                
    def width(self):
        return self._width

    # The height of the occupancy map in cells                
    def height(self):
        return self._height
    
    def name(self):
        return self._name     