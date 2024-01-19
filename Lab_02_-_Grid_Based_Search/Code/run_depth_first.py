#!/usr/bin/env python3

from grid_search.occupancy_grid import OccupancyGrid
from grid_search.depth_first_planner import DepthFirstPlanner

# Create the occupancy grid
occupancy_grid = OccupancyGrid("Depth-First Example", 21, 21, 0.5)

# Change to range(1, 20) for the simpler example
for y in range(0, 20):
    occupancy_grid.set_cell(11, y, 1)

start = (0, 20)
goal = (20, 0)

planner = DepthFirstPlanner(occupancy_grid)

# Run the planner to work out the path from the start to the goal
planner.plan(start, goal)

# Pause
planner.wait_for_key_press()

# Show the path
planner.extract_path_to_goal()

# Pause again
planner.wait_for_key_press()
