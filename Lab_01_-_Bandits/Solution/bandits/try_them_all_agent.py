'''
Created on 13 Jan 2022

@author: ucacsjj
'''

import math
import numpy as np

from .agent import Agent

# This agent implements the try-them-all strategy which goes through and
# pulls each arm in turn. Some of this code looks a bit redundant (the
# agent base class does a sweep itself). However, this has been written this
# way to show a bit more how the agent contains its own state and does
# step-by-step change in its behaviour.

class TryThemAllAgent(Agent):
    '''
    classdocs
    '''


    def __init__(self, environment, number_of_pulls):
        self._number_of_pulls = number_of_pulls
        super().__init__(environment)        
        
    def reset(self):
        super().reset()
        # The current arm we are pulling
        self._current_arm = 0
        self._current_arm_count = 0
        
        # Shows when we finish pulling all arms
        self._finished_sweeping_over_arms = False
        
        # The best action
        self._best_action = None
       
    def _choose_action(self):
        
        # If we have finished our sweep through all the arms, return
        # which one is best        
        if self._finished_sweeping_over_arms is True:
            return self._best_action

        # Update the count for the current arm                
        self._current_arm_count += 1
        
        # We haven't pulled this arm all the times we are going to.
        # Therefore, return the current arm
        if self._current_arm_count < self._number_of_pulls:
            return self._current_arm
        
        # Move to the next arm to pull and set the arm count to 1      
        self._current_arm_count = 1
        self._current_arm += 1
            
        # If we've not exhausted the arms, then return this one
        if self._current_arm < self._number_of_bandits:
            return self._current_arm

        # We have finished the sweep so stop doing it            
        self._finished_sweeping_over_arms = True
            
        # Work out the element with the highest weighted average
        average_q = np.divide(self.total_reward, self.number_of_pulls)
        best_action = np.where(average_q == np.amax(average_q))[0]        
        self._best_action = best_action[0]
        print(f'Choosing best action={self._best_action}')

        return self._best_action
        
                    
            
            

    