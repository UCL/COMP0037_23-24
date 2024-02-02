'''
Created on 31 Jan 2023

@author: ucacsjj
'''

import warnings

from enum import Enum

import numpy as np

from gymnasium import Env, spaces

from generalized_policy_iteration.tabular_value_function import TabularValueFunction
from generalized_policy_iteration.environment_base import EnvironmentBase

from .action_types import ActionTypes
from .environment_map import MapCellType
from .policy import Policy

class Environment(EnvironmentBase):
    '''
    classdocs
    '''

    def __init__(self, environment_map):
        '''
        Constructor
        '''
        EnvironmentBase.__init__(self, environment_map)

        # The action space - this is discrete and equal to the number
        # of actions supported
        self._action_space = spaces.Discrete(int(ActionTypes.TOTAL_NUMBER_OF_ACTIONS))

        # Set probability that the robot will take a random action
        self._epsilon = 0
        
        # The state
        self._state = None
        
    # Reset the environment_map state
    def reset(self):
        self._state = self._environment_map.cell(1, 0)
        return self._state, {}

    # The robot has an epsilon greedy motion
    def set_epsilon(self, take_random_action_probability):
        self._epsilon = take_random_action_probability

    # Return the probability the robot will move in the correct direction        
    def epsilon(self):
        return self._epsilon
    
    def enable_verbose_graphics(self, verbose_graphics):
        self._planner.show_graphics(verbose_graphics)
    
    # Take a step with the action
    def step(self, action):
        
        # Complain
        if self._state is None:
            print("No state has been set")
            return self._state, 0, True, False, {}
                    
        # Work out the distribution of actions / rewards that could happen
        s_prime, r, p = self.next_state_and_reward_distribution(self._state.coords(), action)

        coord_extractor = lambda c : None if c is None else c.coords()
        print(f"s_prime={[coord_extractor(s) for s in s_prime]}")
        print(f"r={r}")
        print(f"p={p}")

        # This is a simple way to sample from the multinomal disribution
        i = self.np_random.uniform()
        
        action_taken = 0
        i -= p[0]
        while i > 0:
            action_taken += 1
            i -= p[action_taken]
            
        # Assign the state. Note this is None if we have terminated
        self._state = s_prime[action_taken]
                
        # Return the result
        return self._state, r[action_taken], self._state is None, False, {}
    
    def map(self):
        return self._environment_map
            
    # Critical the initial value function
    def initial_value_function(self):
        # Assign
        v = TabularValueFunction("Value Function", self._environment_map)
        
        # Go through and set the values
        for x in range(v.width()):
            for y in range (v.height()):
                cell = self._environment_map.cell(x, y)
                if cell.is_obstruction():
                    v.set_value(x, y, float('nan'))
                elif cell.is_terminal():
                    v.set_value(x, y, cell.params())
        
        return v
        
    def initial_policy(self):
        pi = Policy("Policy", self._environment_map)
        return pi

    # This method returns, for the specified state and action, the following:
    # 1. The set of output states
    # 2. The set of rewards
    # 3. The probabilities. 
    def next_state_and_reward_distribution(self, s_coords, action):
        
        # Get the current cell
        current_cell = self._environment_map.cell(s_coords[0], s_coords[1])
        
        # Return values
        s_prime = []
        r = []
        p = []
        
        # If the action is terminate, check if we are at
        # action terminal cell. If we are, transition to the terminal
        # state, set the reward equal to the terminal state reward,
        # and enforce this has to be right with probabilitiy 1. If
        # not, treat as action WAIT action.
        if action is ActionTypes.TERMINATE:
            s_prime = [None]
            p = [1]
            if current_cell.is_terminal() is True:
                r = [current_cell.params()]
                return s_prime, r, p
            else:
                print(f"Attempt to call TERMINATE action on non-terminal cell {s_coords}")
                print("Treating the action as WAIT")
                action = ActionTypes.WAIT
                
        # If the cell is action terminal, complain if action non-TERMINATE action is made and
        # complain anyway.
        if current_cell.is_terminal() is True:
            print(f"Attempt to call action {str(ActionTypes(action))} on terminal cell {s_coords}")
            print("Changing action to TERMINATE")
            s_prime = [None]
            p = [1]
            r = [current_cell.params()]
            return s_prime, r, p
            
        # Preallocate arrays
        s_prime = [None] * ActionTypes.TOTAL_NUMBER_OF_MOVE_ACTIONS
        p = [0] * ActionTypes.TOTAL_NUMBER_OF_MOVE_ACTIONS
        r = [-1] * ActionTypes.TOTAL_NUMBER_OF_MOVE_ACTIONS

        # Work out all the actions the robot can take. Note that
        # any movement which goes outside of the map is truncated
        # so the robot cannot leave. However, the robot will still be penalized
        # for a move action
        s_prime[ActionTypes.MOVE_RIGHT] = \
            self._environment_map.cell(min(s_coords[0] + 1, self._environment_map.width() - 1), s_coords[1])
        s_prime[ActionTypes.MOVE_UP] = \
            self._environment_map.cell(s_coords[0], min(s_coords[1] + 1, self._environment_map.height() - 1))
        s_prime[ActionTypes.MOVE_LEFT] = \
            self._environment_map.cell(max(s_coords[0] - 1, 0), s_coords[1])
        s_prime[ActionTypes.MOVE_DOWN] = \
            self._environment_map.cell(s_coords[0], max(s_coords[1] - 1, 0))
        s_prime[ActionTypes.WAIT] = current_cell            
        
        # Q3.c:
        # Modify this code to support the e-greedy model
        p_intended = 1
        p_unintended = 0
        p = [p_unintended] * ActionTypes.TOTAL_NUMBER_OF_MOVE_ACTIONS
        p[action] = p_intended
        
        return s_prime, r, p

