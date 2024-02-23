#!/usr/bin/env python3

'''
Created on 23 Feb 2024

@author: ucacsjj
'''

# FMDP-based techniques
from generalized_policy_iteration.policy_evaluator import PolicyEvaluator
from generalized_policy_iteration.value_function_drawer import ValueFunctionDrawer

# Specific example stuff

from simple_example.environment_map import EnvironmentMap
from simple_example.environment import Environment
from simple_example.policy_drawer import PolicyDrawer

from simple_example.action_types import ActionTypes
from simple_example.simple_example_soft_policy import SimpleExampleSoftPolicy

if __name__ == '__main__':
        # Create an environment map
    environment_map = EnvironmentMap("Simple 1D Test", 5, 5)
    
    # Add here any holes and goals
    environment_map.add_goal(2, 2)
    environment_map.add_hole(3, 0)
    
    # Create the simulation environment from this map
    environment = Environment(environment_map)
    
    # Create the policy - the environment serves up a
    # default one for us which is of the right dimensions
    pi = SimpleExampleSoftPolicy("Target policy", environment_map)
    
    # Note this is an epsilon greedy policy, so there is sampling by default.
    # We set epsilon to zero to disable this behaviour
    pi.set_epsilon(0)
     
    # Set the policy
    pi.set_action(0, 0, ActionTypes.MOVE_RIGHT)
    pi.set_action(1, 0, ActionTypes.MOVE_RIGHT)
    pi.set_action(2, 0, ActionTypes.MOVE_RIGHT)
    pi.set_action(4, 0, ActionTypes.MOVE_UP)
    pi.set_action(4, 1, ActionTypes.MOVE_UP)
    pi.set_action(4, 2, ActionTypes.MOVE_UP)
    pi.set_action(4, 3, ActionTypes.MOVE_UP)
    pi.set_action(4, 4, ActionTypes.MOVE_LEFT)
    pi.set_action(3, 4, ActionTypes.MOVE_LEFT)
    pi.set_action(2, 4, ActionTypes.MOVE_LEFT)
    pi.set_action(1, 4, ActionTypes.MOVE_LEFT)
    pi.set_action(0, 4, ActionTypes.MOVE_DOWN)
    pi.set_action(0, 3, ActionTypes.MOVE_DOWN)
    pi.set_action(0, 2, ActionTypes.MOVE_DOWN)
    pi.set_action(3, 1, ActionTypes.MOVE_UP)   
    pi.set_action(3, 2, ActionTypes.MOVE_UP)
    pi.set_action(3, 3, ActionTypes.MOVE_LEFT)
    pi.set_action(2, 3, ActionTypes.MOVE_LEFT)
    pi.set_action(1, 3, ActionTypes.MOVE_DOWN)
    pi.set_action(1, 2, ActionTypes.MOVE_RIGHT)
    
    policy_drawer = PolicyDrawer(pi, 300)
    
    policy_drawer.update()
    policy_drawer.wait_for_key_press()
    
    policy_evaluator = PolicyEvaluator(environment)
    policy_evaluator.set_policy(pi)
    policy_evaluator.set_max_policy_evaluation_steps_per_iteration(1)
       
    # Set up the value function drawer and pause
    value_function_drawer = ValueFunctionDrawer(policy_evaluator.value_function(), 300)
    value_function_drawer.set_font_size(20)    
    policy_evaluator.set_value_function_drawer(value_function_drawer)
    
    # Now iterate until the policy evaluator has converged. By running
    # a single iteration each time, we can update the evaluated policy
    # to see how the values evolve.
    converged = False
    while converged is False:
        converged  = policy_evaluator.evaluate()
        value_function_drawer.update()
        
    value_function_drawer.wait_for_key_press()
        
    value_function_drawer.save_screenshot("q2_v.pdf")
    