'''
Created on 14 Jan 2022

@author: ucacsjj
'''
import math
import numpy as np

from .agent import Agent

class DampedEpsilonGreedyAgent(Agent):
    
    def __init__(self, environment, epsilon):
        super().__init__(environment)
        self._epsilon = epsilon

    def _choose_action(self):
        if np.random.uniform() < self._compute_epsilon():
            action = np.random.choice(self._number_of_bandits)
        else:
            average_q = np.divide(self.total_reward, self.number_of_pulls)
            best_action = np.where(average_q == np.amax(average_q))[0]        
            action = best_action[0]
            
        return action
    
    # Q5.c:
    # Explore with different values for this function and see what happens.
    def _compute_epsilon(self):
        
        return self._epsilon * math.exp(-0.05 * self.total_number_of_pulls)
            
        