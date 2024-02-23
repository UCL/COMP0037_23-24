#!/usr/bin/env python3

'''
Created on 6 Feb 2023

@author: ucacsjj
'''

# FMDP-based techniques
from generalized_policy_iteration.policy_evaluator import PolicyEvaluator
from generalized_policy_iteration.value_function_drawer import ValueFunctionDrawer

# Monte Carlo techniques
from monte_carlo.on_policy_mc_predictor import OnPolicyMCPredictor

# Specific example stuff

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
    pi = SimpleExampleSoftPolicy("Target policy", environment_map)
    pi.set_action(0, 0, ActionTypes.MOVE_RIGHT)
    pi.set_action(1, 0, ActionTypes.MOVE_RIGHT)
    pi.set_action(3, 0, ActionTypes.MOVE_LEFT)
    pi.set_action(4, 0, ActionTypes.MOVE_LEFT)
    pi.set_action(5, 0, ActionTypes.MOVE_LEFT)
    pi.set_action(5, 0, ActionTypes.MOVE_RIGHT)
    pi.set_action(8, 0, ActionTypes.MOVE_LEFT)
    pi.set_action(9, 0, ActionTypes.MOVE_LEFT)
    
    policy_evaluator = PolicyEvaluator(environment)
    policy_evaluator.set_policy(pi)
    policy_evaluator.set_max_policy_evaluation_steps_per_iteration(1)
       
    # Set up the value function drawer and pause
    value_function_drawer = ValueFunctionDrawer(policy_evaluator.value_function(), 100)
    value_function_drawer.set_font_size(20)    
    policy_evaluator.set_value_function_drawer(value_function_drawer)        

    # The policy evaluation algorithm
    converged = False
    while converged is False:
        converged  = policy_evaluator.evaluate()
        value_function_drawer.update()
        
    value_function_drawer.wait_for_key_press()

    # The on policy predictor
    on_policy_evaluator = OnPolicyMCPredictor(environment)
    on_policy_evaluator.set_target_policy(pi)
    on_policy_evaluator.set_number_of_episodes(1)
    
    value_function_drawer = ValueFunctionDrawer(on_policy_evaluator.value_function(), 100)
    value_function_drawer.set_font_size(20)    
    on_policy_evaluator.set_value_function_drawer(value_function_drawer)        
    value_function_drawer.wait_for_key_press()
    
    for i in range(20):
        on_policy_evaluator.evaluate()
        value_function_drawer.update()
        value_function_drawer.wait_for_key_press()
        
    value_function_drawer.wait_for_key_press()
