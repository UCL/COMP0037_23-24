'''
Created on 20 Feb 2023

@author: ucacsjj
'''

import random

from generalized_policy_iteration.tabular_policy import TabularPolicy

# Implement an epsilon greedy policy
# Internally, this contain an "optimal" policy
# which we can sample from randomly using epsilon greedy


class EpsilonGreedySoftPolicy(TabularPolicy):
    '''
    classdocs
    '''

    def __init__(self, name, environment_map, epsilon = 0):
        TabularPolicy.__init__(self, name, environment_map)
        
        self._epsilon = epsilon
    
    def set_epsilon(self, epsilon):
        
        self._epsilon = epsilon
        
    def epsilon(self):
        
        return self._epsilon
    
    def action(self, x, y):
        
        if random.random() < self._epsilon:
            return self._sample_random_action(x, y)
        else:
            return self._sample_greedy_optimal_action(x, y)
        
    def action_probability(self, x, y):
        raise NotImplementedError()
        
    def _sample_random_action(self, x, y):
        raise NotImplementedError()
    
    def _sample_greedy_optimal_action(self, x, y):
        return self._policy[x][y]
    