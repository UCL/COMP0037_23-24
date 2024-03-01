'''
Created on 7 Mar 2023

@author: steam
'''

import random

from generalized_policy_iteration.dynamic_programming_base import DynamicProgrammingBase

class TDAlgorithmBase(DynamicProgrammingBase):
    '''
    classdocs
    '''

    def __init__(self, environment):
        
        DynamicProgrammingBase.__init__(self, environment)
        
        self._use_first_visit = True
        self._number_of_episodes = 10
        self._use_exploring_starts = True
        self._pi = None
        self._use_experience_replay = False
        self.set_experience_replay_buffer_size(10)
        self._alpha = 1e-3
        self._replays_per_update = 10
      
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
        
    def set_number_of_replays_per_update(self, replays_per_update):
        self._replays_per_update = replays_per_update
        
    def set_alpha(self, alpha):
        self._alpha = alpha
        
    def alpha(self):
        return self._alpha
        
    def initialize(self):
        
        DynamicProgrammingBase.initialize(self)
        
        
    # Select the start state S and start action A
    def _select_episode_start(self):
        if self._use_exploring_starts is True:
            start_x = self._environment.random_initial_state()
        else:
            start_x = self._environment.get_state(0, 0)
        
        coords = start_x.coords()
        start_a = self._pi.action(coords[0], coords[1])
            
        return start_x, start_a
        
        
    # Add the latest episode to our cheesy replay buffer.
    # If the buffer is full, throw an old epsiode out at random.
    def _add_episode_to_experience_replay_buffer(self, episode):
        
        if self._stored_experiences < self._experience_replay_buffer_size:
            self._experience_replay_buffer[self._stored_experiences] = episode
            self._stored_experiences += 1
        else:
            idx = random.randint(0, self._stored_experiences - 1)
            self._experience_replay_buffer[idx] = episode
            
    # Draw an episode at random. If the buffer is empty, return None
    def _draw_random_episode_from_experience_replay_buffer(self):
        
        if self._stored_experiences == 0:
            return None        
        
        idx = random.randint(0, self._stored_experiences - 1)
        return self._experience_replay_buffer[idx]
        
        