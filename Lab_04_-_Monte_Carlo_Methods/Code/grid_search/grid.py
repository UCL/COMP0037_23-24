'''
Created on 26 Jan 2022

@author: ucacsjj
'''


class Grid:

    def __init__(self, name: str, width: int, height: int):
        self._name = name
        self._width = width
        self._height = height

    # The width of the occupancy map in cells
    def width(self) -> int:
        return self._width

    # The height of the occupancy map in cells
    def height(self) -> int:
        return self._height

    def set_name(self, name: str):
        self._name = name

    def name(self) -> str:
        return self._name
