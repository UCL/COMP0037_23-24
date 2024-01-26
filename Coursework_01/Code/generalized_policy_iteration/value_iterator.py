'''
Created on 29 Jan 2022

@author: ucacsjj
'''

from .dynamic_programming_base import DynamicProgrammingBase

# This class ipmlements the value iteration algorithm

class ValueIterator(DynamicProgrammingBase):

    def __init__(self, environment):
        DynamicProgrammingBase.__init__(self, environment)
        
        # The maximum number of times the value iteration
        # algorithm is carried out is carried out.
        self._max_optimal_value_function_iterations = 2000
   
    # Method to change the maximum number of iterations
    def set_max_optimal_value_function_iterations(self, max_optimal_value_function_iterations):
        self._max_optimal_value_function_iterations = max_optimal_value_function_iterations

    #    
    def solve_policy(self):

        # Initialize the drawers
        if self._policy_drawer is not None:
            self._policy_drawer.update()
            
        if self._value_drawer is not None:
            self._value_drawer.update()
        
        self._compute_optimal_value_function()
 
        self._extract_policy()
        
        # Draw one last time to clear any transients which might
        # draw changes
        if self._policy_drawer is not None:
            self._policy_drawer.update()
            
        if self._value_drawer is not None:
            self._value_drawer.update()
        
        return self._v, self._pi

    # Q3f:
    # Finish the implementation of the methods below.
    
    def _compute_optimal_value_function(self):

        # This method returns no value.
        # The method updates self._pi

        raise NotImplementedError()

    def _extract_policy(self):

        # This method returns no value.
        # The policy is in self._pi

        raise NotImplementedError()
