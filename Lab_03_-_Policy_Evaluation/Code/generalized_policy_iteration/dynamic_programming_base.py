'''
Created on 31 Jan 2022

@author: ucacsjj
'''

# This is the base class for policy and value iteration

from typing import Optional

from .environment_base import EnvironmentBase
from .tabular_value_function import TabularValueFunction
from .value_function_drawer import ValueFunctionDrawer

class DynamicProgrammingBase(object):

    def __init__(self, environment: EnvironmentBase):

        # The environment_map the system works with        
        self._environment = environment

        # The discount factor        
        self._gamma = 1
        
        # Threshold on maximum change in the value function to test
        # for convergence in policy evaluation
        self._theta = 1e-6
        
        # Flag to show if initialized
        self._initialized = False
        
        # Working scratch variables for the current value function
        # and policy
        self._v = None
        
        # Shows debug output interactively
        self._value_drawer = None
        
                          
    # Set the drawer which will show the value function.
    # If set, this will update interactively.                                    
    def set_value_function_drawer(self, value_drawer: ValueFunctionDrawer):
        self._value_drawer = value_drawer

    # Set the discount factor        
    def set_gamma(self, gamma: float):
        self._gamma = gamma

    # Retrieve the discount factor        
    def gamma(self) -> float:
        return self._gamma
    
    # Set the threshold on value function changes
    def set_theta(self, theta: float):
        self._theta = theta

    # Return the threshold on value function changes        
    def theta(self) -> float:
        return self._theta
    
    # Initialize the policy and value function. Must be called
    # before trying to solve for the policy.
    def initialize(self, initial_v: Optional[TabularValueFunction] = None):
        
        # If initial values were specified, use them. Otherwise
        # get the default from the environment.
        if initial_v is None:
            self._v = self._environment.initial_value_function()
        else:
            self._v = initial_v
            
        self._initialized = True
            
    # Reset the iterator
    def reset(self):
        # Reset
        self._v = None
        self._initialized = False

    # Return the current value function      
    def value_function(self) -> TabularValueFunction:
        return self._v
        
