'''
Created on 23 Feb 2023

@author: steam
'''

import numpy as np

from .monte_carlo_policy_predictor import MonteCarloPolicyPredictor

class OffPolicyMCPredictor(MonteCarloPolicyPredictor):

    def __init__(self, environment):
        
        MonteCarloPolicyPredictor.__init__(self, environment)
        self._Q = None
        self._b = None

    def set_behaviour_policy(self, b):
        self._b = b
        
        self.initialize()

    def initialize(self):
        
        MonteCarloPolicyPredictor.initialize(self)
        
        environment = self._environment
        environment_map = environment.environment_map()
        w = environment_map.width()
        h = environment_map.height()
        
        action_space = environment.action_space
        
        # Allocate Q and A
        self._Q = np.zeros((w, h, action_space.n))
        self._C = np.zeros((w, h, action_space.n))
        
        self._v.set_name("OffPolicyMCPredictor")

    def _select_episode_start(self):
        
        if self._use_exploring_starts is True:
            start_x = self._environment.random_initial_state()
            start_a = self._environment.random_initial_action(start_x)
        else:
            start_x = self._environment.get_state(0, 0)
            start_a = 0
        
        return start_x, start_a

    def _update_value_function_from_episode(self, episode):

        G = 0
        W = 1
        
        # Implement the update for the policy predictor. Note that, unlike the
        # on policy case, you have to update both the Q and V values.
