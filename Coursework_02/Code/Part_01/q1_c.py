#!/usr/bin/env python3

'''
Created on 7 Mar 2023

@author: steam
'''

from common.scenarios import test_three_row_scenario
from common.airport_map_drawer import AirportMapDrawer

from td.td_policy_predictor import TDPolicyPredictor
from monte_carlo.on_policy_mc_predictor import OnPolicyMCPredictor
from monte_carlo.off_policy_mc_predictor import OffPolicyMCPredictor

from generalized_policy_iteration.value_function_drawer import ValueFunctionDrawer
from generalized_policy_iteration.policy_evaluator import PolicyEvaluator

from p1.low_level_environment import LowLevelEnvironment
from p1.low_level_actions import LowLevelActionType
from p1.low_level_policy_drawer import LowLevelPolicyDrawer

if __name__ == '__main__':
    airport_map, drawer_height = test_three_row_scenario()
    env = LowLevelEnvironment(airport_map)
    env.set_nominal_direction_probability(0.8)

    # Policy to evaluate
    pi = env.initial_policy()
    pi.set_epsilon(0)
    pi.set_action(14, 1, LowLevelActionType.MOVE_DOWN)
    pi.set_action(14, 2, LowLevelActionType.MOVE_DOWN)  
    
    # Policy evaluation algorithm
    pe = PolicyEvaluator(env)
    pe.set_policy(pi)
    v_pe = ValueFunctionDrawer(pe.value_function(), drawer_height)  
    pe.evaluate()
    v_pe.update()
    # Calling update a second time clears the "just changed" flag
    # which means all the digits will be rendered in black
    v_pe.update()  
    
    # Off policy MC predictors
    
    epsilon_b_values = [0.1, 0.2, 0.5, 1.0]
    
    num_values = len(epsilon_b_values)
    
    mc_predictors = [None] * num_values
    mc_drawers = [None] * num_values

    for i in range(num_values):
        mc_predictors[i] = OffPolicyMCPredictor(env)
        mc_predictors[i].set_use_first_visit(True)
        b = env.initial_policy()
        b.set_epsilon(epsilon_b_values[i])
        mc_predictors[i].set_target_policy(pi)
        mc_predictors[i].set_behaviour_policy(b)
        mc_predictors[i].set_experience_replay_buffer_size(64)
        mc_drawers[i] = ValueFunctionDrawer(mc_predictors[i].value_function(), drawer_height)
        
    for e in range(100):
        for i in range(num_values):
            mc_predictors[i].evaluate()
            mc_drawers[i].update()
       
    v_pe.save_screenshot("q1_c_truth_pe.pdf")
    for i in range(num_values):
        mc_drawers[i].save_screenshot(f"mc-off-{int(epsilon_b_values[i]*10):03}-pe.pdf")