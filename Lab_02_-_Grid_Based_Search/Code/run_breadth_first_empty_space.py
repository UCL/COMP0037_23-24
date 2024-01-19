#!/usr/bin/env python3

from grid_search.occupancy_grid import OccupancyGrid
from grid_search.breadth_first_planner import BreadthFirstPlanner

# Create the occupancy grid
# Q1c:
# Modify the occupancy grid size
occupancy_grid = OccupancyGrid(
    "Breadth First Search in Empty Space", 10, 10, 0.5)

# Q1d:

# Add obstacles to the occupancy grid. The last term is the probability
# that a cell is occupied. In this module, we really only deal with the cases
# where it's a 0 or a 1.
# occupancy_grid.set_cell(7, 2, 1)

# Create the planner object. This takes in the occupancy grid, which
# specifies where the robot can go.
planner = BreadthFirstPlanner(occupancy_grid)

# Set some configuration values for showing the graphics. On different
# OS combinations, the update can be very fast or very slow. If it's
# slow, set update_graphics_each_iteration to False.
planner.set_pause_time(0.01)
planner.update_graphics_each_iteration(True)

# This is how to change the size of the window if it's too big. We only
# set the height to ensure the aspect ratio is always computed properly.
# planner.set_maximum_grid_drawer_window_height_in_pixels(200)

# Q1b:
# Set the start and end values to the specified
start = (0, 0)
goal = (9, 4)

# Run the planner to work out the path from the start to the goal
planner.plan(start, goal)

# Pause
planner.wait_for_key_press()

# Show the path
planner.extract_path_to_goal()

# Pause again
planner.wait_for_key_press()

# This how to take a screenshot of the search grid
search_grid_drawer = planner.search_grid_drawer()
search_grid_drawer.save_screenshot('breadth_first_empty_space.pdf')
search_grid_drawer.save_screenshot('breadth_first_empty_space.png')
