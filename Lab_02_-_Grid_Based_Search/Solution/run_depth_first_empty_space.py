#!/usr/bin/env python3

from grid_search.occupancy_grid import OccupancyGrid
from grid_search.depth_first_planner import DepthFirstPlanner

# Create the occupancy grid
occupancy_grid = OccupancyGrid("Depth-First Example", 21, 21, 0.5)

# Create the planner object. This takes in the occupancy grid, which
# specifies where the robot can go.
planner = DepthFirstPlanner(occupancy_grid)

# Set some configuration values for showing the graphics. On different
# OS combinations, the update can be very fast or very slow. If it's
# slow, set update_graphics_each_iteration to False.
planner.set_pause_time(0.01)
planner.update_graphics_each_iteration(True)

start = (10, 10)
goal = (10, 0)

# Run the planner to work out the path from the start to the goal
planner.plan(start, goal)

# Pause
planner.wait_for_key_press()

# Show the path
planner.extract_path_to_goal()

# Pause again
planner.wait_for_key_press()
