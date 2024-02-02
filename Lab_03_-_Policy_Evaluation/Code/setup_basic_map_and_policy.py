#!/usr/bin/env python3

'''
Created on 6 Feb 2023

@author: ucacsjj
'''

from simple_example.environment_map import EnvironmentMap
from simple_example.environment import Environment
from simple_example.policy_drawer import PolicyDrawer

# Needed to support Q1.c
from simple_example.policy import Policy
from simple_example.action_types import ActionTypes

if __name__ == '__main__':
    
    # Create an environment map
    environment_map = EnvironmentMap("Simple 1D Test", 1, 2)
    
    # Q1.b:
    # Add a goal. An example is:
    # environment_map.add_goal(0, 0)
    
    # Create the simulation environment from this map
    environment = Environment(environment_map)
    
    # Create the policy - the environment serves up a
    # default one for us which is of the right dimensions
    pi = environment.initial_policy()
    
    # Q1.c:
    # Modify the policy to provide some useful actions
    pi.set_action(0, 0, ActionTypes.MOVE_RIGHT)
    pi.set_action(0, 1, ActionTypes.MOVE_RIGHT)
    
    # Draw the policy
    policy_drawer = PolicyDrawer(pi, 200)    
    # How to save the policy - use the common save commands
    #policy_drawer.save_screenshot("q1.pdf")
    policy_drawer.wait_for_key_press()
