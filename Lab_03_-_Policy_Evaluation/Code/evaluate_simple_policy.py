#!/usr/bin/env python3

'''
Created on 6 Feb 2023

@author: ucacsjj
'''

from generalized_policy_iteration.policy_evaluator import PolicyEvaluator
from generalized_policy_iteration.value_function_drawer import ValueFunctionDrawer

from simple_example.environment_map import EnvironmentMap
from simple_example.environment import Environment
from simple_example.policy_drawer import PolicyDrawer

from simple_example.policy import Policy
from simple_example.action_types import ActionTypes

if __name__ == '__main__':
    
    # Create an environment map
    environment_map = EnvironmentMap("Simple 1D Test", 10, 1)
    
    # Q2:
    # Add here any holes and goals
    environment_map.add_goal(9, 0)
    environment_map.add_hole(0, 0)
    
    # Create the simulation environment from this map
    environment = Environment(environment_map)
    
    # Create the policy - the environment serves up a
    # default one for us which is of the right dimensions
    pi = environment.initial_policy()
    
    # Q2:
    # Set the policy
    for x in range(0, 10):
        pi.set_action(x, 0, ActionTypes.MOVE_RIGHT)
    
    # Draw the policy
    policy_drawer = PolicyDrawer(pi, 100)    
    policy_drawer.save_screenshot("q2_pi.pdf")
    policy_drawer.wait_for_key_press()
    
    # Set up the policy evaluator
    policy_evaluator = PolicyEvaluator(environment)
    policy_evaluator.set_policy(pi)
    policy_evaluator.set_max_policy_evaluation_steps_per_iteration(1)
       
    # Set up the value function drawer and pause
    value_function_drawer = ValueFunctionDrawer(policy_evaluator.value_function(), 100)
    value_function_drawer.set_font_size(20)    
    policy_evaluator.set_value_function_drawer(value_function_drawer)        
    value_function_drawer.wait_for_key_press()

    # Now iterate until the policy evaluator has converged. By running
    # a single iteration each time, we can update the evaluated policy
    # to see how the values evolve.
    converged = False
    while converged is False:
        converged  = policy_evaluator.evaluate()
        value_function_drawer.update()
        
    value_function_drawer.save_screenshot("q2_v.pdf")
        

    
    
