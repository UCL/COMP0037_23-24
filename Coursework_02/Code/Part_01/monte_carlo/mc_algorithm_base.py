'''
Created on 7 Mar 2023

@author: steam
'''

import random

from generalized_policy_iteration.dynamic_programming_base import DynamicProgrammingBase

class MCAlgorithmBase(DynamicProgrammingBase):
    '''
    classdocs
    '''

    def __init__(self, environment):
        
        DynamicProgrammingBase.__init__(self, environment)
        
        self._use_first_visit = False
        self._number_of_episodes = 10
        self._use_exploring_starts = True
        self._pi = None
        self._use_experience_replay = False
        self.set_experience_replay_buffer_size(10)
      
    def set_use_first_visit(self, use_first_visit):
        self._use_first_visit = use_first_visit

    def set_target_policy(self, policy):        
        self._pi = policy        
        self.initialize()
        
    def set_number_of_episodes(self, number_of_episodes):
        self._number_of_episodes = number_of_episodes
        
    def set_use_exploring_starts(self, use_exploring_start_state):
        self._use_exploring_start_state = use_exploring_start_state
        
    def set_experience_replay_buffer_size(self, experience_replay_buffer_size):
        self._experience_replay_buffer_size = experience_replay_buffer_size
        self._experience_replay_buffer = [None] * experience_replay_buffer_size
        self._stored_experiences = 0
        
    def initialize(self):
        
        DynamicProgrammingBase.initialize(self)
        
    def _add_episode_to_experience_replay_buffer(self, episode):
        
        if self._stored_experiences < self._experience_replay_buffer_size:
            self._experience_replay_buffer[self._stored_experiences] = episode
            self._stored_experiences += 1
        else:
            idx = random.randint(0, self._stored_experiences - 1)
            self._experience_replay_buffer[idx] = episode
            
    def _draw_random_episode_from_experience_replay_buffer(self):
        
        if self._stored_experiences == 0:
            return None        
        
        idx = random.randint(0, self._stored_experiences - 1)
        return self._experience_replay_buffer[idx]
        
        