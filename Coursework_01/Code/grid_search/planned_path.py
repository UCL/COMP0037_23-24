from collections import deque

# This class is a plain old data structure (=no hidden fields)
# which stores the planned path

class PlannedPath(object):

    # Construct a new planner object and set defaults.
    def __init__(self):

        # Does the path actually reach the goal or not?
        self.goal_reached = False
        
        # The list of waypoint cells, from start to finish, which make
        # up the path.
        self.waypoints = deque()

        # Performance information - number of waypoints, and the
        # travel cost of the path.
        self.number_of_waypoints = 0
        self.path_travel_cost = 0
        
        # The number of cells visited to plan the path
        self.number_of_cells_visited = 0
