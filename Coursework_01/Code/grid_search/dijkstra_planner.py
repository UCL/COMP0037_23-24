'''
Created on 2 Jan 2022

@author: ucacsjj
'''

from collections import deque
from math import sqrt
from queue import PriorityQueue

from .occupancy_grid import OccupancyGrid
from .planner_base import PlannerBase

class DijkstraPlanner(PlannerBase):

    # This implements Dijkstra. The priority queue is the path length
    # to the current position.
    
    def __init__(self, occupancy_grid: OccupancyGrid):
        PlannerBase.__init__(self, occupancy_grid)
        self.priority_queue = PriorityQueue()  # type: ignore

    # Q1d:
    # Modify this class to finish implementing Dijkstra
