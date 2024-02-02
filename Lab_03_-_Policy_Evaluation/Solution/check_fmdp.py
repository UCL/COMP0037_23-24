#!/usr/bin/env python3

'''
Created on 7 Feb 2023

@author: ucacsjj
'''

from simple_example.environment_map import EnvironmentMap
from simple_example.environment import Environment

from simple_example.action_types import ActionTypes

if __name__ == '__main__':
    
    # Q3.b:
    # Modify the dimensions of the map to see the impact of 2D,
    # obstacles, etc.
    
    # Create an environment map
    environment_map = EnvironmentMap("Simple 1D Test", 10, 1)
    environment_map.add_goal(7, 0)
    environment_map.add_hole(3, 0)
    
    # Create the simulation environment from this map
    environment = Environment(environment_map)
    
    # Useful lambda to get details about a cell
    coord_extractor = lambda c : None if c is None else c.coords()
    
    # Check what happens when you call different actions
    
    # Q3.a:
    # Try different actions at different cells to see what the FMDP
    # does.
    action = ActionTypes.MOVE_RIGHT
    for x in range(10):
        print("==============================================================")
        print(f"Calling action {str(ActionTypes(action))} on cell {x,0}:")
        s_prime, r, p = environment.next_state_and_reward_distribution((x, 0), \
                                                                       ActionTypes.MOVE_RIGHT)
        
        print(f"s_prime={[coord_extractor(s) for s in s_prime]}")
        print(f"r={r}")
        print(f"p={p}")
        
        