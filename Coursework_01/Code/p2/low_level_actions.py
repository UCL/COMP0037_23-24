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
    RIGHT = 0
    UP_RIGHT = 1
    UP = 2
    UP_LEFT = 3
    LEFT = 4
    DOWN_LEFT = 5
    DOWN = 6
    DOWN_RIGHT = 7
    TERMINATE = 8
    NONE = 9
    NUMBER_OF_ACTIONS = 10
