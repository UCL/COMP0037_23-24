'''
Created on 3 Feb 2023

@author: ucacsjj
'''

from enum import IntEnum

# The actions the robot can take
# MOVE_LEFT,_RIGHT: self-explanatory
# WAIT: The robot does not move

# These are special:

# TERMINATE: The robot transitions to the terminal state; exclusively used at terminal sites
# NONE: The robot cannot take any action; exclusively used inside obstacles

class ActionTypes(IntEnum):
    MOVE_RIGHT = 0
    MOVE_UP = 1
    MOVE_LEFT = 2
    MOVE_DOWN = 3
    WAIT = 4
    TERMINATE = 5
    NONE = 6
    TOTAL_NUMBER_OF_MOVE_ACTIONS = 5
    TOTAL_NUMBER_OF_ACTIONS = 7