#!/usr/bin/env python3

'''
Created on 7 Feb 2023

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
    environment_map = EnvironmentMap("Cliff of doom", 10, 5)
    
    
    # Add the goal
    environment_map.add_goal(9, 0)
    
    # Add the holes
    
    for x in range(1,8):
        environment_map.add_hole(x, 0)
    
    # Create the simulation environment from this map
    environment = Environment(environment_map)
    
    # Q4.b:
    # Modify this value
    environment.set_epsilon(0.1)
    
    # Create the policy - the environment serves up a
    # default one for us which is of the right dimensions
    pi = environment.initial_policy()
    
    # Q4.a, Q4.c:
    # Write a policy to get to the goal
    pi.set_action(0, 0, ActionTypes.MOVE_UP)
    
    for y in range(5):
        pi.set_action(9, y, ActionTypes.MOVE_DOWN)
    
    # Draw the policy
    policy_drawer = PolicyDrawer(pi, 400)    
    
    # Set up the policy evaluator
    policy_evaluator = PolicyEvaluator(environment)
    policy_evaluator.set_policy(pi)
    policy_evaluator.set_max_policy_evaluation_steps_per_iteration(1)
       
    # Set up the value function drawer and pause
    value_function_drawer = ValueFunctionDrawer(policy_evaluator.value_function(), 400)
    value_function_drawer.set_font_size(20)    
    policy_evaluator.set_value_function_drawer(value_function_drawer)        
    value_function_drawer.wait_for_key_press()


    # Now iterate until the policy evaluator has converged. By running
    # a single iteration each time, we can update the evaluaed policy
    # to see how the values evolve.
    converged = False
    while converged is False:
        converged  = policy_evaluator.evaluate()
        value_function_drawer.update()
        
    value_function_drawer.wait_for_key_press()        
