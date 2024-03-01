'''
Created on 23 Feb 2023

@author: steam
'''

import numpy as np

from .monte_carlo_controller import MonteCarloController

class OnPolicyMCPredictor(MonteCarloController):
    
    def initialize(self):
        
        MonteCarloController.initialize(self)
                
        # Grids for computing values
        # Get the environment and environment_map
        environment = self._environment
        environment_map = environment.map()
        w = environment_map.width()
        h = environment_map.height()
        
        action_space = environment.action_space
        
        # Allocate the count grid
        self._count_grid = np.zeros((w, h, action_space.m))
            
    def _select_episode_start(self):
        
        if self._use_exploring_starts is True:
            start_x = self._environment.random_initial_state()
        else:
            start_x = self._environment.get_state(0, 0)
        
        print(f"start_x={start_x}")
        
        coords = start_x.coords()
        start_a = self._pi.action(coords[0], coords[1])
        
        return start_x, start_a
            
    def _update_action_function_from_episode(self, episode):
        
        G = 0

        for s in range(episode.number_of_steps() - 1, -1, -1):
            
            # Work out the return              
            G = episode.reward(s) + self._gamma * G
            
            # Handle first visit logic down here sometime
            
            state = episode.state(s).coords()
            a = episode.action(s)
            
            self._returns_grid[state[0], state[1], a] += G
            self._count_grid[state[0], state[1], a] += 1
            
            average_return = self._returns_grid[state[0], state[1], a] / self._count_grid[state[0], state[1]]
            
            self._Q[state[0], state[1], a] = average_return
            
            # Update the action
            q_vals = self._Q[state[0], state[1], :]
            a_max = np.argmax(q_vals)
            self._pi.set_action(state[0], state[1], a_max)
            
            
            
