'''
Created on 29 Jan 2022

@author: ucacsjj
'''

from enum import IntEnum

# The low-level driving directions actions the robot can take when stepping
# in different directions or recharging. The TERMINATE action takes the
# robot to the (virtual) terminal state and can only be executed from
# cells whose type is a terminal one.

class LowLevelActionType(IntEnum):
    MOVE_RIGHT = 0
    MOVE_UP_RIGHT = 1
    MOVE_UP = 2
    MOVE_UP_LEFT = 3
    MOVE_LEFT = 4
    MOVE_DOWN_LEFT = 5
    MOVE_DOWN = 6
    MOVE_DOWN_RIGHT = 7
    NONE = 8
    TERMINATE = 9
    NUMBER_OF_ACTIONS = 10
    TOTAL_NUMBER_OF_MOVE_ACTIONS = 9
