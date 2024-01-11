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

    # Q6a:
    # Implement UCB
    def _choose_action(self):
        action = 0
        return action
