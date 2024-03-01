'''
Created on 17 Feb 2023

@author: ucacsjj
'''

class Episode(object):
    '''
    classdocs
    '''

    def __init__(self, max_capacity):
        '''
        Constructor
        '''
        
        self._terminated_successfully = False
        
        # Preallocate arrays
        self._s = [None] * max_capacity
        self._a = [None] * max_capacity
        self._r = [None] * max_capacity
        
        self._number_of_steps = 0
        
    def append(self, state, action, reward):
        
        self._s[self._number_of_steps]= state
        self._a[self._number_of_steps]= action
        self._r[self._number_of_steps]= reward
        
        self._number_of_steps += 1
        
    def state(self, s):
        return self._s[s]
    
    def action(self, s):
        return self._a[s]
    
    def reward(self, s):
        return self._r[s]
    
    def number_of_steps(self):
        return self._number_of_steps
    
    def set_terminated_successfully(self, terminated_successfully):
        self._terminated_successfully = terminated_successfully
        
    def terminated_successfully(self):
        return self._terminated_successfully