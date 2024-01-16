'''
Created on 13 Jan 2022

@author: ucacsjj
'''

import math

import numpy as np

# The agent is our octopus which can pull the different arms on the
# bandits. Note this is the base class for the agent. It sets up
# common book keeping but doesn't actually do anything on its own. The
# interesting stuff is carried out in the (hidden) method
# _choose_action.

class Agent(object):
    '''
    classdocs
    '''

    def __init__(self, environment):
        # Store the environment and common information
        self._environment = environment
        self._number_of_bandits = self._environment.number_of_bandits()
        
        # Store how many times we pull the arms when we pull all arms.
        # This is used for all algorithms to bootstrap them. For the
        # try them all algorithms, 
        self.initial_number_of_arm_pulls = 1
        
        # Do all the actions to reset the agent's internal state
        self.reset()
        
    def reset(self):
        
        # For each action store the total reward and the the number
        # of times that action has been taken
        self.total_reward = np.zeros(self._number_of_bandits)
        self.number_of_pulls = np.zeros(self._number_of_bandits)
    
        # This array stores the average
        self.q = np.zeros(self._number_of_bandits)
        
        # The total number of times an arm has been pulled. This could be
        # computed from summing over number_of_pulls, but this is cached
        # value that's just easier to use
        
        self.total_number_of_pulls = 0

        # Seed the initial values by pulling all the arms once        
        self._pull_all_arms()
        
    def step(self):
        
        # Pick the action we want to take. This will be the bandit
        # to pull
        action = self._choose_action()
        
        # Get the reward
        obs, reward, done, info = self._environment.step(action)
        
        # Update the information for the action
        self.total_reward[action] += reward
        self.number_of_pulls[action] += 1
        
        self.total_number_of_pulls += 1
        
        return action, reward
        
    def total_number_of_steps(self):
        return self.total_number_of_pulls
        
    def _choose_action(self):
        '''Pick which bandit to pull next'''
        raise NotImplementedError

        
    # Pull all the arms a pre-specified number of times
    def _pull_all_arms(self):
    
        # Bootstrap by pulling each arm once    
        for b in range(0, self._environment.number_of_bandits()):
            for s in range(0, self.initial_number_of_arm_pulls):
                obs, reward, done, info = self._environment.step(b)
                self.total_reward[b] += np.mean(reward)
                
            self.number_of_pulls[b] += self.initial_number_of_arm_pulls
            self.total_number_of_pulls += self.initial_number_of_arm_pulls


            
    
    
    
