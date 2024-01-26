#!/usr/bin/env python3

'''
Created on 3 Feb 2022

@author: ucacsjj
'''

from common.scenarios import full_scenario
from generalized_policy_iteration.policy_iterator import PolicyIterator
from generalized_policy_iteration.value_function_drawer import \
    ValueFunctionDrawer
from p2.low_level_environment import LowLevelEnvironment

if __name__ == '__main__':
    
    # Get the map for the scenario
    #airport_map, drawer_height = three_row_scenario()
    airport_map, drawer_height = full_scenario()
    
    # Set up the environment for the robot driving around
    airport_environment = LowLevelEnvironment(airport_map)
    
    # Configure the process model
    airport_environment.set_nominal_direction_probability(1)

    # Create the policy iterator
    policy_solver = PolicyIterator(airport_environment)

    # Set up initial state
    policy_solver.initialize()
    
    # We only do 10 policy evaluation steps per iteration
    policy_solver.set_max_policy_evaluation_steps_per_iteration(10)
            
    # Evaluate the policy. In this part of the question, only this is supported.
    V = policy_solver.evaluate_policy()
    
    value_function_drawer = ValueFunctionDrawer(V, drawer_height)

    # Run the evaluator repeatedly. This lets you see how the value changes
    # over time.    
    for steps in range(1000):
        policy_solver.evaluate_policy()
        value_function_drawer.update()
     
    # Wait for a final key press
    value_function_drawer.wait_for_key_press()
