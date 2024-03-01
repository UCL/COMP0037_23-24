#!/usr/bin/env python3

'''
Created on 9 Mar 2023

@author: ucacsjj
'''

import math

from common.scenarios import slippy_corridor
from common.airport_map_drawer import AirportMapDrawer


from td.sarsa import SARSA
from td.q_learner import QLearner

from generalized_policy_iteration.value_function_drawer import ValueFunctionDrawer

from p1.low_level_environment import LowLevelEnvironment
from p1.low_level_actions import LowLevelActionType
from p1.low_level_policy_drawer import LowLevelPolicyDrawer

if __name__ == '__main__':
    airport_map, drawer_height = slippy_corridor()

    # Show the scenario        
    airport_map_drawer = AirportMapDrawer(airport_map, drawer_height)
    airport_map_drawer.update()
    
    # Create the environment
    env = LowLevelEnvironment(airport_map)
    
    # Specify array of learners, renderers and policies
    learners = [None] * 2
    v_renderers = [None] * 2
    p_renderers = [None] * 2 
    pi = [None] * 2
    
    pi[0] = env.initial_policy()
    pi[0].set_epsilon(1)
    learners[0] = SARSA(env)
    learners[0].set_alpha(0.1)
    learners[0].set_experience_replay_buffer_size(64)
    learners[0].set_number_of_episodes(32)
    learners[0].set_initial_policy(pi[0])
    v_renderers[0] = ValueFunctionDrawer(learners[0].value_function(), drawer_height)    
    p_renderers[0] = LowLevelPolicyDrawer(learners[0].policy(), drawer_height)
    
    
    pi[1] = env.initial_policy()
    pi[1].set_epsilon(1)
    learners[1] = QLearner(env)
    learners[1].set_alpha(0.1)
    learners[1].set_experience_replay_buffer_size(64)
    learners[1].set_number_of_episodes(32)
    learners[1].set_initial_policy(pi[1])      
    v_renderers[1] = ValueFunctionDrawer(learners[1].value_function(), drawer_height)    
    p_renderers[1] = LowLevelPolicyDrawer(learners[1].policy(), drawer_height)

    for i in range(10000):
        print(i)
        for l in range(2):
            learners[l].find_policy()
            v_renderers[l].update()
            p_renderers[l].update()
            pi[l].set_epsilon(1/math.sqrt(1+0.25*i))
        