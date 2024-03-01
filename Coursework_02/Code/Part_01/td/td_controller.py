'''
Created on 8 Mar 2023

@author: ucacsjj
'''

import random
import math
import numpy as np

from monte_carlo.episode_sampler import EpisodeSampler

from .td_algorithm_base import TDAlgorithmBase

class TDController(TDAlgorithmBase):
    '''
    classdocs
    '''

    def __init__(self, environment):
        TDAlgorithmBase.__init__(self, environment)

    def initialize(self):
        
        TDAlgorithmBase.initialize(self)
        
        # Allocate the Q value estimate; inelegant way to figure out
        # the dimensions needed :(
        environment = self._environment
        environment_map = environment.map()
        w = environment_map.width()
        h = environment_map.height()
        action_space = environment.action_space
        self._num_actions = action_space.n
        
        # Allocate Q
        self._Q = -100 * np.ones((w, h, self._num_actions))

    def set_initial_policy(self, pi):
        self._pi = pi
        self.initialize()
        
    def policy(self):
        return self._pi

    def find_policy(self):
        
        # Although this can be done in real-time, we follow the convention
        # of running it MC-like. 
        episode_sampler = EpisodeSampler(self._environment)
        
        for episode in range(self._number_of_episodes):

            # Choose the start for the episode            
            start_x, start_a = self._select_episode_start()
            self._environment.reset(start_x)
            
            # Sample the episode
            new_episode = episode_sampler.sample_episode(self._pi, start_x, start_a)

            # If we didn't reach a terminal state, the 
            # episode was not successful, so we skip it
            if new_episode.terminated_successfully() is False:
                continue
            
            # Update with the current episode
            self._update_action_and_value_functions_from_episode(new_episode)
            
            # Pick several randomly from the experience replay buffer and update with those as well
            for _ in range(min(self._replays_per_update, self._stored_experiences)):
                episode = self._draw_random_episode_from_experience_replay_buffer()
                self._update_action_and_value_functions_from_episode(episode)
                
            self._add_episode_to_experience_replay_buffer(new_episode)
        
    def _update_action_and_value_functions_from_episode(self, episode):
        raise NotImplementedError()
        
    def _update_q_and_policy(self, coords, a, new_q):
        
        # Update the Q value
        
        # Update Q
        self._Q[coords[0], coords[1], a] = new_q

        # Identify the set of non-zero actions available at this cell        
        action_space = self._pi.action_space(coords[0], coords[1])
                
        # Figure out the valid action with the highest Q value and set that
        # as the greedy optimal action
        max_a = action_space[0]
        max_q = self._Q[coords[0], coords[1],  action_space[0]]
        for a in range(1, len(action_space)):
            if self._Q[coords[0], coords[1],  action_space[a]] > max_q:
                max_a = action_space[a]
                max_q = self._Q[coords[0], coords[1],  action_space[a]]
            elif self._Q[coords[0], coords[1],  action_space[a]] == max_q:
                if random.random() < 0.5:
                    max_a = a

        self._pi.set_action(coords[0], coords[1], max_a)

        # Work out the state value
        v = 0
        total_p = 0
        for a in range(len(action_space)):
            p = self._pi.action_probability(coords[0], coords[1], action_space[a])
            #print(f"{a}:{p}")
            if p == 0:
                continue
            v = v + p * self._Q[coords[0], coords[1],  action_space[a]]
            total_p = total_p + p
            
        #print(f"total_p={total_p}")
        assert(math.fabs(total_p-1)<1e-6)
        self._v.set_value(coords[0], coords[1], v)
 


   
