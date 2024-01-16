'''
Created on 12 Jan 2022

@author: ucacsjj
'''
import math
import numpy as np

import gym
from gym import spaces

# This class implements an individual bandit. It is parameterized by a
# mean and covariance. One or more samples can be drawn.

class Bandit:

    def __init__(self, mean, sigma):
        """Construct bandit."""
        self._mean = mean
        self._sigma = sigma
    
    def mean(self):
        return self._mean

    def sigma(self):
        return self._sigma
    
    def pull_arm(self):
        reward = np.random.normal(self._mean, self._sigma)
        return reward

# This class is a collection of our k bandits. It is implemented in
# OpenAI Gym. We are only using a tiny bit of it for this coursework.
# The state space isn't really defined (bandits are a stateless
# problem). The action is the numerical value of the arm to pull.

class BanditEnvironment(gym.Env):
    
    def __init__(self, number_of_bandits):
        super().__init__()
        self._bandits = [None] * number_of_bandits
        self.action_space = spaces.Discrete(number_of_bandits)
        
    def set_bandit(self, bandit_number, bandit):
        """Add the bandit."""
        self._bandits[bandit_number] = bandit
        
    def bandit(self, bandit_number):
        return self._bandits[bandit_number]
           
    def number_of_bandits(self):
        return len(self._bandits)
        
                
    def optimal_action(self):
        
        max_q = self._bandits[0].mean()
        max_q_action = 0
        
        for b in range(1, len(self._bandits)):
            q = self._bandits[b].mean()
            if q > max_q:
                max_q = q
                max_q_action = b
            elif q == max_q:
                if np.random.uniform(1) < 0.5:
                    max_q_action = b
                    
        return max_q_action, max_q
        
    def reset(self):
        pass
        
    def step(self, action):
        reward = self._bandits[action].pull_arm()
        return {}, reward, False, {}

    
