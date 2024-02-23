'''
Created on 17 Feb 2023

@author: ucacsjj
'''

# This class samples an episode from the environment

from .episode import Episode

class EpisodeSampler(object):
    '''
    classdocs
    '''

    def __init__(self, environment, params = None):
        '''
        Constructor
        '''
        
        self._environment = environment
        self._max_steps = 2000
        
    def set_max_steps(self, max_steps):
        self._max_steps = max_steps
        
    def max_steps(self):
        return self._max_steps

    def sample_episode(self, pi, start_x = None, start_a = None):
        
        # Select the start state. This was either specified by the 
        # user or is chosen randomly.
        if start_x is None:
            state = self._environment.random_initial_state()
        else:
            state = start_x

        # Select the start action. This was either specified by the 
        # user or is chosen randomly.
        if start_a is None:
            action = self._environment.random_initial_action(state)
        else:
            action = start_a
        
        episode = Episode(self._max_steps)
        
        self._environment.reset(state) 
        
        # Iterate over the episode
        for _ in range(self._max_steps):
            
            next_state, reward, done, is_truncated, info = self._environment.step(action)
            
            #print(f"next_state={next_state};action={action};reward={reward};done={done}")
            
            episode.append(state, action, reward)
            
            if done is True:
                episode.set_terminated_successfully(True)
                #print(f"final_state={state};action={action};reward={reward};done={done}")
                break
            
            state = next_state
            
            # Now pick the next action according to the policy; this
            # should be random for this to work
            xy = state.coords()
            action = pi.action(xy[0], xy[1])
            
        return episode
                