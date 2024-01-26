'''
Created on 29 Jan 2022

@author: ucacsjj
'''

from generalized_policy_iteration.tabular_policy import TabularPolicy

from .low_level_actions import LowLevelActionType

# The driving policy. For each cell in the state space, in which direction do we go next?

class LowLevelPolicy(TabularPolicy):

    def __init__(self, name, airport_map):
        TabularPolicy.__init__(self, name, airport_map)
        
        # When we set up the policy, we MUST put a TERMINATE action in the cells which
        # are terminals. If the cell is in a wall, the action is flagged to NONE. For
        # all other cells, the initial strategy is to move right.
        
        type_creator = lambda x, y: LowLevelActionType.TERMINATE if airport_map.cell(x, y).is_terminal() \
                                    else LowLevelActionType.NONE if airport_map.cell(x, y).is_obstruction() \
                                    else LowLevelActionType.RIGHT
        
        self._policy = [[type_creator(x,y) for y in range(self._height)] \
                            for x in range(self._width)]
        
        self._airport_map = airport_map

    def set_action(self, x, y, action):
        self._policy[x][y] = LowLevelActionType(action)
        
    def action(self, x, y):
        return self._policy[x][y]
    
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
        
        
        
    