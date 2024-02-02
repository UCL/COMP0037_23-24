'''
Created on 26 Jan 2024

@author: ucacsjj
'''

from gymnasium import Env, spaces

from .tabular_policy import TabularPolicy
from .tabular_value_function import TabularValueFunction

class EnvironmentBase(Env):
    '''
    This class is the base representation of environments.
    It extends the gymnasium env environment to support 
    '''
    
    def __init__(self, environment_map):
        '''
        Constructor
        '''
        self._environment_map = environment_map

    
    # Critical the initial value function
    def initial_value_function(self) -> TabularValueFunction:
        raise NotImplementedError()

    def initial_policy(self) -> TabularPolicy:
        raise NotImplementedError()
    
    def map(self):
        return self._environment_map

    # This method returns, for the specified state and action, the following:
    # 1. The set of output states
    # 2. The set of rewards
    # 3. The probabilities. 
    def next_state_and_reward_distribution(self, s_coords, action):
        raise NotImplementedError()
       
        