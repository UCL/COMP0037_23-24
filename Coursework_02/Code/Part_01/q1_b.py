#!/usr/bin/env python3

'''
Created on 7 Mar 2023

@author: steam
'''

from common.scenarios import test_three_row_scenario
from common.airport_map_drawer import AirportMapDrawer

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
    v_pe.update()  
    
    # On policy MC predictor
    mcpp = OnPolicyMCPredictor(env)
    mcpp.set_target_policy(pi)
    mcpp.set_experience_replay_buffer_size(64)
    
    # Q1b: Experiment with this value
    mcpp.set_use_first_visit(True)
    
    v_mcpp = ValueFunctionDrawer(mcpp.value_function(), drawer_height)
    
    # Off policy MC predictor
    mcop = OffPolicyMCPredictor(env)
    mcop.set_target_policy(pi)
    mcop.set_experience_replay_buffer_size(64)
    b = env.initial_policy()
    b.set_epsilon(0.2)
    mcop.set_behaviour_policy(b)
    
    # Q1b: Experiment with this value
    mcop.set_use_first_visit(True)

    v_mcop = ValueFunctionDrawer(mcop.value_function(), drawer_height)
        
    for e in range(100):
        mcpp.evaluate()
        v_mcpp.update()
        mcop.evaluate()
        v_mcop.update()
        
    # Sample way to generate outputs    
    v_pe.save_screenshot("q1_b_truth_pe.pdf")
    v_mcop.save_screenshot("q1_b_mc-off_pe.pdf")
    v_mcpp.save_screenshot("q1_b_mc-on_pe.pdf")