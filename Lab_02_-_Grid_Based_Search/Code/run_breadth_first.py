#!/usr/bin/env python3

from grid_search.occupancy_grid import OccupancyGrid
from grid_search.breadth_first_planner import BreadthFirstPlanner

# Create the occupancy grid
occupancy_grid = OccupancyGrid("Breadth-First Example", 21, 21, 0.5)

# Q3c:
# Change to range(1, 20) for the simpler example
for y in range(0, 20):
    occupancy_grid.set_cell(11, y, 1)

start = (0, 20)
goal = (20, 0)

planner = BreadthFirstPlanner(occupancy_grid)

planner.set_pause_time(0)
planner.update_graphics_each_iteration(True)


planner.plan(start, goal)

# Pause
planner.wait_for_key_press()

# Show the path
planner.extract_path_to_goal()
planner.wait_for_key_press()
