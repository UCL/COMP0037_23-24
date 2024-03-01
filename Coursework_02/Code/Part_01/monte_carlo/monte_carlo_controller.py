'''
Created on 23 Feb 2023

@author: steam
'''

import numpy as np

from .mc_algorithm_base import MCAlgorithmBase

# Monte Carlo techniques
from .episode_sampler import EpisodeSampler

class MonteCarloController(MCAlgorithmBase):

    def __init__(self, environment):
        
        MCAlgorithmBase.__init__(self, environment)
        self._Q = None

    def initialize(self):
        
        MCAlgorithmBase.initialize(self)
        environment = self._environment
        environment_map = environment.environment_map()
        w = environment_map.width()
        h = environment_map.height()
        
        action_space = environment.action_space
        
        # Allocate Q and A
        self._Q = np.zeros((w, h, action_space.n))

    def set_initial_policy(self, policy):        
        self._pi = policy        
        self.initialize()

    def find_policy(self):
        
        episode_sampler = EpisodeSampler(self._environment)
        
        for episode in range(self._number_of_episodes):

            # Choose the start for the episode            
            start_x, start_a = self._select_episode_start()
            
            # Now sample it
            episode = episode_sampler.sample_episode(self._pi, start_x, start_a)

            
            # If we didn't terminate, skip this episode
            if episode.terminated_successfully() is False:
                continue
            
            self._update_state_action_function_from_episode(episode)
            
    def _select_episode_start(self):
        raise NotImplementedError
            
    def _update_action_function_from_episode(self, episode):
        raise NotImplementedError 
    