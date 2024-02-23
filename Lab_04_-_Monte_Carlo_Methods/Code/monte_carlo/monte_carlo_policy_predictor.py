'''
Created on 20 Feb 2023

@author: ucacsjj
'''

from generalized_policy_iteration.dynamic_programming_base import DynamicProgrammingBase

# Monte Carlo techniques
from .episode_sampler import EpisodeSampler

class MonteCarloPolicyPredictor(DynamicProgrammingBase):
    '''
    classdocs
    '''

    def __init__(self, environment):
        
        DynamicProgrammingBase.__init__(self, environment)
        self._use_first_visit = True
        self._number_of_episodes = 10
        self._use_exploring_starts = True
        self._pi = None
        
    def set_use_first_visit(self, use_first_visit):
        self._use_first_visit = use_first_visit

    def set_target_policy(self, policy):        
        self._pi = policy        
        self.initialize()
        
    def set_number_of_episodes(self, number_of_episodes):
        self._number_of_episodes = number_of_episodes
        
    def set_use_exploring_starts(self, use_exploring_start_state):
        self._use_exploring_start_state = use_exploring_start_state
        
    def initialize(self):
        
        DynamicProgrammingBase.initialize(self)

    def evaluate(self):
        
        episode_sampler = EpisodeSampler(self._environment)
        
        for episode in range(self._number_of_episodes):

            # Choose the start for the episode            
            start_x, start_a = self._select_episode_start()
            
            # Now sample it
            episode = episode_sampler.sample_episode(self._pi, start_x, start_a)

            
            # If we didn't terminate, skip this episode
            if episode.terminated_successfully() is False:
                continue
            
            self._update_value_function_from_episode(episode)
            
    def _select_episode_start(self):
        raise NotImplementedError
            
    def _update_value_function_from_episode(self, episode):
        raise NotImplementedError 
            
            
            
        