'''
Created on 14 Jan 2022

@author: ucacsjj
'''

import math

import numpy as np

from .agent import Agent

class UpperConfidenceBoundAgent(Agent):

    def __init__(self, environment, c):
        super().__init__(environment)
        self._c = c

    def _choose_action(self):
        # Work out the optimal Q value
        Qt = np.divide(self.total_reward, self.number_of_pulls)
        
        # Work out the UCB C value
        Ct = self._c * np.sqrt(np.divide(math.log(self.total_number_of_pulls), self.number_of_pulls))
        
        print(Ct)
        
        weighted_Q = Qt + Ct
        
        best_action = np.where(weighted_Q == np.amax(weighted_Q))[0]        
        action = best_action[0]
        
        return action