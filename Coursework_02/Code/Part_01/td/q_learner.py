'''
Created on 8 Mar 2023

@author: steam
'''

import random
import numpy as np

from .td_controller import TDController

# Simplified version of the predictor from S+B

class QLearner(TDController):
    '''
    classdocs
    '''

    def __init__(self, environment):
        TDController.__init__(self, environment)

    def initialize(self):
               
        # Set up experience replay buffer
        TDController.initialize(self)
        
        # Change names to change titles on drawn windows
        self._v.set_name("Q-Learning Expected Value Function")
        self._pi.set_name("Q-Learning Greedy Policy")
            
    def _update_action_and_value_functions_from_episode(self, episode):
        
        # Q2b:
        # Complete implementation of this method
        # Each time you update the state value function, you will need to make a
        # call of the form:
        #
        # self._update_q_and_policy(coords, a, new_q) 
        #
        # This calls a method in the TDController which will update the
        # Q value estimate in the base class and will update
        # the greedy policy and estimated state value function
        
        
        # Handle everything up to the last state transition to the terminal state
        s = episode.state(0)
        coords = s.coords()
        reward = episode.reward(0)
        a = episode.action(0)
        
        for step_count in range(1, episode.number_of_steps()):
            new_q = (1 - self._alpha) * self._Q[coords[0], coords[1], a] + self._alpha * reward
            s_prime = episode.state(step_count)
            coords_prime = s_prime.coords()
            
            # Figure out the best action
            action_values = self._Q[coords_prime[0], coords_prime[1],  :]
            max_actions = (np.where(action_values == np.amax(action_values)))[0]
            max_action = max_actions[random.choice(range(max_actions.size))]
            
            new_q += self._alpha * self._gamma * self._Q[coords_prime[0], coords_prime[1], max_action]
            self._update_q_and_policy(coords, a, new_q)
            reward = episode.reward(step_count)
            s = s_prime
            coords = coords_prime
            a = episode.action(step_count)
            
        new_q = reward
        
        self._update_q_and_policy(coords, a, new_q)     
        