'''
Created on 31 Jan 2023

@author: ucacsjj
'''

import random

from .dynamic_programming_base import DynamicProgrammingBase

class PolicyEvaluator(DynamicProgrammingBase):
    '''
    classdocs
    '''

    def __init__(self, environment):
        DynamicProgrammingBase.__init__(self, environment)
        
        # The maximum number of times the policy evaluation algorithm
        # will be run before the for loop is exited.
        self._max_policy_evaluation_steps_per_iteration = 100
        
    def set_policy(self, policy):
        self._pi = policy
        
        self.initialize()
        
        
    def evaluate(self):
        
        # Get the environment and environment_map
        environment = self._environment
        environment_map = environment.map()
        
        # Execute the loop at least once
        
        iteration = 0
        
        while True:
            
            delta = 0

            # Sweep systematically over all the states
            
            # Q1: modify the iteration so that you select a random number of cells in a random order
            for x in range(environment_map.width()):#random.randint(0, environment_map.width()):#
                for y in range(environment_map.height()):# random.randint(0, environment_map.height()):#
            
                    if environment_map.cell(x, y).is_obstruction() or environment_map.cell(x, y).is_terminal():
                        continue
                    
                    new_v, d_v = self._compute_new_value_of_v(x, y)
                        
                    # Set the new value in the value function
                    self._v.set_value(x, y, new_v)
                                        
                    # Update the maximum deviation
                    delta = max(delta, d_v)
         
                    # Increment the policy evaluation counter        
                    iteration += 1
                       
            print(f'Finished policy evaluation iteration {iteration}')
            
            # Terminate the loop if the change was very small
            if delta < self._theta:
                return True
                
            # Terminate the loop if the maximum number of iterations is met. Generate
            # a warning
            if iteration >= self._max_policy_evaluation_steps_per_iteration:
                print('Maximum number of iterations exceeded')
                return False
                        
    def set_max_policy_evaluation_steps_per_iteration(self, \
                                                      max_policy_evaluation_steps_per_iteration):
            self._max_policy_evaluation_steps_per_iteration = max_policy_evaluation_steps_per_iteration

    def _compute_new_value_of_v(self, x, y):
        # We skip obstructions and terminals. If a cell is obstructed,
        # there's no action the robot can take to access it, so it doesn't
        # count. If the cell is terminal, it executes the terminal action
        # state. The value of the value of the terminal cell is the reward.
        # The reward itself was set up as part of the initial conditions for the
        # value function.
        
        environment_map = self._environment.map()
                           
        # Unfortunately the need to use coordinates is a bit inefficient, due
        # to legacy code
        cell = (x, y)
        
        # Get the previous value function
        old_v = self._v.value(x, y)
        
        if environment_map.cell(x, y).is_obstruction() or environment_map.cell(x, y).is_terminal():
            return old_v, 0
        
        # Compute p(s',r|s,a)
        s_prime, r, p = self._environment.next_state_and_reward_distribution(cell, \
                                                                         self._pi.action(x, y))
        
        # Sum over the rewards
        new_v = 0
        for t in range(len(p)):
            sc = s_prime[t].coords()
            new_v = new_v + p[t] * (r[t] + self._gamma * self._v.value(sc[0], sc[1]))     
        
        d_v = abs(old_v-new_v)
        
        return new_v, d_v
        
