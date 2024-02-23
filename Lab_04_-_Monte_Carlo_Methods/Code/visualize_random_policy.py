#!/usr/bin/env python3

'''
Created on 6 Feb 2023

@author: ucacsjj
'''

import time

from simple_example.environment_map import EnvironmentMap
from simple_example.environment import Environment
from simple_example.policy_drawer import PolicyDrawer

from simple_example.action_types import ActionTypes
from simple_example.simple_example_soft_policy import SimpleExampleSoftPolicy

if __name__ == '__main__':
    
    # Create an environment map
    environment_map = EnvironmentMap("Simple 1D Test", 10, 1)
    
    # Add here any holes and goals
    environment_map.add_goal(7, 0)
    environment_map.add_hole(3, 0)
    
    # Create the simulation environment from this map
    environment = Environment(environment_map)
    
    # Create the policy - the environment serves up a
    # default one for us which is of the right dimensions
    # Create the policy - the environment serves up a
    # default one for us which is of the right dimensions
    pi = SimpleExampleSoftPolicy("Target policy", environment_map)
    pi.set_action(0, 0, ActionTypes.MOVE_RIGHT)
    pi.set_action(1, 0, ActionTypes.MOVE_RIGHT)
    pi.set_action(3, 0, ActionTypes.MOVE_LEFT)
    pi.set_action(4, 0, ActionTypes.MOVE_LEFT)
    pi.set_action(5, 0, ActionTypes.MOVE_LEFT)
    pi.set_action(5, 0, ActionTypes.MOVE_RIGHT)
    pi.set_action(8, 0, ActionTypes.MOVE_LEFT)
    pi.set_action(9, 0, ActionTypes.MOVE_LEFT)
        
    # The off policy predictor
    b = SimpleExampleSoftPolicy("Behaviour policy", environment_map, 0.1)
    
    b_policy_drawer = PolicyDrawer(b, 100)
    # Show the effect of the behaviour policy
    
    for i in range(50):
        b_policy_drawer.update()
        time.sleep(0.1)
    
