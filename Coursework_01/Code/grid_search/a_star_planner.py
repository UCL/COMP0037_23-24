'''
Created on 2 Jan 2022

@author: ucacsjj
'''

import math

from .dijkstra_planner import DijkstraPlanner
from .occupancy_grid import OccupancyGrid
    
    def __init__(self, occupancy_grid: OccupancyGrid):
        DijkstraPlanner.__init__(self, occupancy_grid)

    # Q2d:
    # Complete implementation of A*.
