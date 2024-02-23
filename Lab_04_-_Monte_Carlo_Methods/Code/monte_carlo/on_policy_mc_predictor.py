'''
Created on 20 Feb 2023

@author: ucacsjj
'''

import numpy as np

from .monte_carlo_policy_predictor import MonteCarloPolicyPredictor

class OnPolicyMCPredictor(MonteCarloPolicyPredictor):
    '''
    classdocs
    '''

    def __init__(self, environment):
        
        MonteCarloPolicyPredictor.__init__(self, environment)            

    def initialize(self):
        
        MonteCarloPolicyPredictor.initialize(self)
                
        # Grids for computing values
        # Get the environment and environment_map
        environment = self._environment
        environment_map = environment.environment_map()
        w = environment_map.width()
        h = environment_map.height()
        
        # This stores the total return computed for each cell in the grid
        self._returns_grid = np.zeros((w, h))

        # This stores the number of episodes which have visited each cell in the grid
        self._count_grid = np.zeros((w, h))
            
        self._v.set_name("OnPolicyMCPredictor")
            
    # For the on policy, the start action has to be according to the 
    # policy and can't be random.
    def _select_episode_start(self):
        
        if self._use_exploring_starts is True:
            start_x = self._environment.random_initial_state()
        else:
            start_x = self._environment.get_state(0, 0)
        
        coords = start_x.coords()
        start_a = self._pi.action(coords[0], coords[1])
       
        return start_x, start_a
            
    def _update_value_function_from_episode(self, episode):

        # Complete the implementation of this method.
        G = 0
        #G = G + self._gamma * episode.reward(episode.number_of_steps() - 1)
        #state = episode.state(episode.number_of_steps() - 1).coords()
        #self._v.set_value(state[0], state[1], average_return)        
            
            
        
