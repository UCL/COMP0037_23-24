'''
Created on 20 Feb 2023

@author: ucacsjj
'''

from .mc_algorithm_base import MCAlgorithmBase

# Monte Carlo techniques
from .episode_sampler import EpisodeSampler

class MonteCarloPolicyPredictor(MCAlgorithmBase):
    '''
    classdocs
    '''

    def __init__(self, environment):
        
        MCAlgorithmBase.__init__(self, environment)

    def set_target_policy(self, policy):        
        self._pi = policy        
        self.initialize()

    def evaluate(self):
        
        episode_sampler = EpisodeSampler(self._environment)

        # Get the policy we use for sampling the episode
        episode_pi = self._episode_pi()
        
        # Iterate through and sample the episodes
        for episode in range(self._number_of_episodes):

            # Choose the start for the episode            
            start_x, start_a = self._select_episode_start(episode_pi)
            
            # Now sample it
            new_episode = episode_sampler.sample_episode(episode_pi, start_x, start_a)

            # If we didn't terminate, skip this episode
            if new_episode.terminated_successfully() is False:
                continue
            
            # Update with the current episode
            self._update_value_function_from_episode(new_episode)
            
            # Pick several randomly from the experience replay buffer and update with those as well
            for _ in range(5):
                episode = self._draw_random_episode_from_experience_replay_buffer()
                if episode is not None:
                    self._update_value_function_from_episode(episode)
                
            self._add_episode_to_experience_replay_buffer(new_episode)
            
    # This method is used to pick the exporing start. The state is selected at random
    # The action is drawn from the policy
    def _select_episode_start(self, pi):
        
        # Choose the starting state at random
        if self._use_exploring_starts is True:
            start_x = self._environment.random_initial_state()
        else:
            start_x = self._environment.get_state(0, 0)

        # Choose the starting action from the appropriate policy
        start_coords = start_x.coords()
        start_a = pi.action(start_coords[0], start_coords[1])
        
        return start_x, start_a
            
    # Update the value function using the episode
    def _update_value_function_from_episode(self, episode):
        raise NotImplementedError

     # Return the policy used for sampling episodes.
    def _episode_pi(self):
        raise NotImplementedError
        
            
            
            
        
