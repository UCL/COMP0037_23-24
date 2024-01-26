from collections import deque
from .occupancy_grid import OccupancyGrid
from .planner_base import PlannerBase
from .search_grid import SearchGridCell

# This class implements the FIFO - or breadth first search - planning
# algorithm. It works by using a double ended queue: cells are pushed
# onto the back of the queue, and are popped from the front of the
# queue.


class BreadthFirstPlanner(PlannerBase):

    # This implements a simple FIFO search algorithm

    def __init__(self, occupancyGrid: OccupancyGrid):
        PlannerBase.__init__(self, occupancyGrid)
        self.fifoQueue = deque()  # type: ignore

    # Simply put on the end of the queue
    def push_cell_onto_queue(self, cell: SearchGridCell):
        self.fifoQueue.append(cell)

    # Check the queue size is zero
    def is_queue_empty(self) -> bool:
        return not self.fifoQueue

    # Simply pull from the front of the list
    def pop_cell_from_queue(self) -> SearchGridCell:
        cell = self.fifoQueue.popleft()
        return cell

    def resolve_duplicate(self, cell: SearchGridCell, parent_cell: SearchGridCell):
        # Nothing to do in this case
        pass
