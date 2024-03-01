'''
Created on 3 Feb 2023

@author: ucacsjj
'''

import random

from generalized_policy_iteration.epsilon_greedy_soft_policy import EpsilonGreedySoftPolicy

from .low_level_actions import LowLevelActionType

class LowLevelPolicy(EpsilonGreedySoftPolicy):
    '''
    classdocs
    '''

    def __init__(self, name, environment_map, epsilon = 0):
        EpsilonGreedySoftPolicy.__init__(self, name, environment_map, epsilon)
        
        # When we set up the policy, we MUST put a TERMINATE action in the cells which
        # are terminals. If the cell is in a wall, the action is flagged to NONE. For
        # all other cells, the initial strategy is to move right.
        
        type_creator = lambda x, y: LowLevelActionType.TERMINATE if environment_map.cell(x, y).is_terminal() \
                                    else LowLevelActionType.NONE if environment_map.cell(x, y).is_obstruction() \
                                    else LowLevelActionType.MOVE_RIGHT
        
        self._policy = [[type_creator(x,y) for y in range(self._height)] \
                            for x in range(self._width)]
        
        self._environment_map = environment_map

    def set_action(self, x, y, action):
        
        # Change to action enum
        action_type = LowLevelActionType(action)
        
        # Sanity checks
        if self._environment_map.cell(x, y).is_terminal() and action != LowLevelActionType.TERMINATE:
            print(f"Attempt to set action on terminal cell {x,y} to {str(LowLevelActionType(action))}; ignoring")
            return
        
        if self._environment_map.cell(x, y).is_obstruction() and action != LowLevelActionType.NONE:
            print(f"Attempt to set action on obstructed cell {x,y} to {str(LowLevelActionType(action))}; ignoring")
            return
        
        self._policy[x][y] = action_type

    def set_greedy_optimal_action(self, x, y, action):
        self.set_action(x, y, action)
        
    def greedy_optimal_action(self, x, y):
        return self._policy[x][y]

    def action_space(self,x , y):
        
        if self._environment_map.cell(x, y).is_terminal():
            actions = [LowLevelActionType.TERMINATE]
            return actions
        
        actions = [LowLevelActionType.MOVE_RIGHT,
                   LowLevelActionType.MOVE_UP_RIGHT,
                   LowLevelActionType.MOVE_UP,
                   LowLevelActionType.MOVE_UP_LEFT,
                   LowLevelActionType.MOVE_LEFT,
                   LowLevelActionType.MOVE_DOWN_LEFT,
                   LowLevelActionType.MOVE_DOWN,
                   LowLevelActionType.MOVE_DOWN_RIGHT,
                   LowLevelActionType.NONE]
        
        return actions
                            
    def action_probability(self, x, y, action):
        
        #print(f"action={action};self._policy[x][y]={self._policy[x][y]};self._epsilon={self._epsilon}")
        
        assert(self._environment_map.cell(x, y).is_obstruction() == False)
        
        # Handle the special cases first
        if self._environment_map.cell(x, y).is_terminal():
            if action == LowLevelActionType.TERMINATE:
                return 1
            else:
                return 0
            
        if action == LowLevelActionType.TERMINATE:
            raise NotImplementedError()
            return 0
            
        if self._environment_map.cell(x, y).is_obstruction():
            if action == LowLevelActionType.NONE:
                return 1
            else:
                return 0
                    

                    
        # Handle all other cases        
        if action == self._policy[x][y]:
            return (1 - self._epsilon) + self._epsilon / LowLevelActionType.TOTAL_NUMBER_OF_MOVE_ACTIONS
        else:
            return self._epsilon / LowLevelActionType.TOTAL_NUMBER_OF_MOVE_ACTIONS
    
    def _sample_random_action(self, x, y):
        
        if self._environment_map.cell(x, y).is_terminal() is True:
            return LowLevelActionType.TERMINATE
        elif self._environment_map.cell(x, y).is_obstruction() is True:
            return LowLevelActionType.NONE
        else:
            return random.randint(0, LowLevelActionType.TOTAL_NUMBER_OF_MOVE_ACTIONS - 1)
    
    def airport_map(self):
        return self._airport_map
        
    def show(self):
        
        # Print out the policy as a string. Note we have to reverse y because
        # y=0 is at the origin and so we need to print top-to-bottom
        for y in reversed(range(self._height)):
            line_string = str(int(self._policy[0][y]))
            for x in range(1,self._width):
                line_string += str(" ") + str(int(self._policy[x][y]))
            print(line_string)

        
        
        
