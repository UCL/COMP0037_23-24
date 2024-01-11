'''
Created on 14 Jan 2022

@author: ucacsjj
'''

import numpy as np

from .agent import Agent

class EpsilonGreedyAgent(Agent):
    
    def __init__(self, environment, epsilon):
        super().__init__(environment)
        self._epsilon = epsilon

    # Q5a:
    # Change the implementation to use the epsilon greedy algorithm
    def _choose_action(self):
        action = 0
        return action
            
        
