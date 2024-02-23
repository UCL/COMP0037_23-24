'''
Created on 3 Feb 2023

@author: ucacsjj
'''

import random

from monte_carlo.epsilon_greedy_soft_policy import EpsilonGreedySoftPolicy

from .action_types import ActionTypes

class SimpleExampleSoftPolicy(EpsilonGreedySoftPolicy):
    '''
    classdocs
    '''

    def __init__(self, name, environment_map, epsilon = 0):
        EpsilonGreedySoftPolicy.__init__(self, name, environment_map, epsilon)
        
        # When we set up the policy, we MUST put a TERMINATE action in the cells which
        # are terminals. If the cell is in a wall, the action is flagged to NONE. For
        # all other cells, the initial strategy is to move right.
        
        type_creator = lambda x, y: ActionTypes.TERMINATE if environment_map.cell(x, y).is_terminal() \
                                    else ActionTypes.NONE if environment_map.cell(x, y).is_obstruction() \
                                    else ActionTypes.MOVE_RIGHT
        
        self._policy = [[type_creator(x,y) for y in range(self._height)] \
                            for x in range(self._width)]
        
        self._environment_map = environment_map

    def set_action(self, x, y, action):
        
        # Change to action enum
        action_type = ActionTypes(action)
        
        # Sanity checks
        if self._environment_map.cell(x, y).is_terminal() and action is not ActionTypes.TERMINATE:
            print(f"Attempt to set action on terminal cell {x,y} to {str(ActionTypes(action))}; ignoring")
            return
        
        if self._environment_map.cell(x, y).is_obstruction() and action is not ActionTypes.NONE:
            print(f"Attempt to set action on obstructed cell {x,y} to {str(ActionTypes(action))}; ignoring")
            return
        
        self._policy[x][y] = action_type
                            
    def action_probability(self, x, y, action):
        
        if action is self._policy[x][y]:
            return (1 - self._epsilon) + self._epsilon / ActionTypes.TOTAL_NUMBER_OF_MOVE_ACTIONS
        else:
            return self._epsilon / ActionTypes.TOTAL_NUMBER_OF_MOVE_ACTIONS
    
    def _sample_random_action(self, x, y):
        if self._environment_map.cell(x, y).is_terminal() is True:
            return ActionTypes.TERMINATE
        else:
            return random.randint(ActionTypes.MOVE_RIGHT, ActionTypes.WAIT)
    
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

        
        
        
