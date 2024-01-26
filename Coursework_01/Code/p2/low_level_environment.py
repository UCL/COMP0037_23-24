'''
Created on 25 Jan 2022

@author: ucacsjj
'''

from enum import Enum

import numpy as np
from gymnasium import Env, spaces

from common.airport_map import MapCellType
from generalized_policy_iteration.tabular_value_function import \
    TabularValueFunction

from .low_level_actions import LowLevelActionType
from .low_level_policy import LowLevelPolicy

# This environment affords a much lower level control of the robot than the
# battery environment. It is partially inspired by the AI Gymn Frozen Lake
# example.

class LowLevelEnvironment(Env):
    '''
    classdocs
    '''

    def __init__(self, airport_map):
        '''
        Constructor
        '''
        # Store the map
        self._airport_map = airport_map
        
        # Direction perturbations
        self._driving_deltas=(
            (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))

        # The action space
        self.action_space = spaces.Discrete(int(LowLevelActionType.NUMBER_OF_ACTIONS))

        # Set probability that the robot will go in the intended direction
        self.set_nominal_direction_probability(0.8)
        
    # Reset the environment state
    def reset(self):
        self._current_coords = None
        return self._current_coords

    # set the probability will go in the nominal direction
    def set_nominal_direction_probability(self, nominal_direction_probability):
        self._p = nominal_direction_probability
        self._q = 0.5 * (1 - self._p)

    # Return the probability the robot will move i the correcc direction        
    def nominal_direction_probability(self):
        return self._p
    
    def enable_verbose_graphics(self, verbose_graphics):
        self._planner.show_graphics(verbose_graphics)
    
    # Not really used right now
    def step(self, action):
        pass
    
    def map(self):
        return self._airport_map
            
    # Critical the initial value function
    def initial_value_function(self):
        # Assign
        v = TabularValueFunction("Value Function", self._airport_map)
        
        # Go through and set the values
        for x in range(v.width()):
            for y in range (v.height()):
                cell = self._airport_map.cell(x, y)
                if cell.is_obstruction():
                    v.set_value(x, y, float('nan'))
                elif cell.is_terminal():
                    v.set_value(x, y, cell.params())
        
        return v
        
    def initial_policy(self):
        pi = LowLevelPolicy("Policy", self._airport_map)
        return pi
    
    # The available actions - same everywhere
    def available_actions(self):
        return self.action_space
    
    # Compute the distribution of the state, value and rewards
    def next_state_and_reward_distribution(self, s, a, print_cell= False):
        
        # Get the current cell
        current_cell = self._airport_map.cell(s[0], s[1])
        
        # Return values
        s_prime = []
        r = []
        p = []        
        
        # Debugging
        if print_cell:
            print(f'action={str(DrivingActionType(a))}')
        
        # First handle the easy cases
        
        # If the action is terminate, check if we are at
        # a terminal cell. If we are, transition to the terminal
        # state, set the reward equal to the terminal state reward,
        # and enforce this has to be right with probabilitiy 1.
        if a == LowLevelActionType.TERMINATE:
            if current_cell.is_terminal() is True:
                s_prime = [None]
                r = [current_cell.params()]
                p = [1]
                return s_prime, r, p
                
        # If the action is none, the robot stays in the same place with probability
        # 1 and accrues a penality of -1.
        if a == LowLevelActionType.NONE:
            s_prime = [current_cell]
            r = [-1]
            p = [1]
            return s_prime, r, p
        
        # All other cases are moving in a given direction
        
        # If the nominal direction is a, we get samples for moving in the directions
        # (a-1, a, a+1).        
        for i in range(-1,2):
            
            # What's the probability of this outcome?
            if i == 0:
                pr = self._p
            else:
                pr = self._q
                
            # Handle index wrapping
            idx = a + i
            
            if idx > 7:
                idx =- 3
            
            # Get the offset for the specified direction
            delta = self._driving_deltas[idx]            
            
            if print_cell:
                print(f'delta={delta}')
            
            # Compute the new robot position
            new_x = s[0] + delta[0]
            new_y = s[1] + delta[1]
            
            # If the action would take the robot off the edge of the map,
            # they can't move and so their position remains the same.
            # There is a nominal cost associated with being stationary
            if (new_x < 0) or (new_x >= self._airport_map.width()) \
                or (new_y < 0) or (new_y >= self._airport_map.height()):
                s_prime.append(current_cell)
                r.append(-1)
                if print_cell:
                    print(f'{current_cell.coords()}->{(new_x,new_y)}->E{current_cell.coords()}')

            else:
                
                # Work out the new type of cell we are entering                        
                new_cell = self._airport_map.cell(new_x, new_y)
            
                # If the cell is obstructed, the logic is the same as before -
                # we can't move. If we can move, subtract the cost for the movement. If
                # it's a baggage claim cell, add an extra penalty.
                if new_cell.is_obstruction():
                    s_prime.append(current_cell)
                    if new_cell.cell_type() is MapCellType.BAGGAGE_CLAIM:
                        r.append(-10)
                    else:
                        r.append(-1)
                    if print_cell:
                        print(f'{current_cell.coords()}->{(new_x,new_y)}->O{current_cell.coords()}')
                else:
                    # The cost is the cost
                    s_prime.append(new_cell)
                    r.append(-self._airport_map.compute_transition_cost(current_cell.coords(), new_cell.coords()))
                    #print(new_cell.coords())
                    if print_cell:
                        print(f'{current_cell.coords()}->{(new_x,new_y)}->A{new_cell.coords()}')
    
            p.append(pr)
            
        return s_prime, r, p
        
 