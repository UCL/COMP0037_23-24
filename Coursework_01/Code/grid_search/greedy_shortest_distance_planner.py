from random import random
from math import sqrt
from queue import PriorityQueue

from .planner_base import PlannerBase
from .occupancy_grid import OccupancyGrid
from .search_grid import SearchGridCell

class GreedyShortestDistancePlanner(PlannerBase):

    # This order the cells on a priority queue, sorted in terms of distance to target: shorter is better

    def __init__(self, occupancyGrid: OccupancyGrid):
        PlannerBase.__init__(self, occupancyGrid)
        self._priority_queue = PriorityQueue()

    # Sort in order of distance from the target and use that
    def push_cell_onto_queue(self, cell: SearchGridCell):

        # Q4a:
        # Complete the implementation by specifying a proper
        # priority. Values with larger priority are pulled off the queue
        # first
        
        # Assign random priority
        # priority: float = random()

        # Assign priority based on Euclidean distance
        cell_coords = cell.coords()
        goal_coords = self.goal.coords()

        dX = cell_coords[0] - goal_coords[0]
        dY = cell_coords[1] - goal_coords[1]
        priority = sqrt(dX * dX + dY * dY)
        
        self._priority_queue.put((priority, cell))

    # Check the queue size is zero
    def is_queue_empty(self) -> bool:
        return self._priority_queue.empty()

    # Simply pull from the front of the list
    def pop_cell_from_queue(self) -> SearchGridCell:
        t = self._priority_queue.get()
        return t[1]

    def resolve_duplicate(self, cell: SearchGridCell, parent_cell: SearchGridCell):
        # Nothing to do in this case
        pass
