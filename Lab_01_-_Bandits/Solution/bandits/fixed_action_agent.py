'''
Created on 14 Jan 2022

@author: ucacsjj
'''

from .agent import Agent

# This agent is really simple - it picks a constant action through all time

class FixedActionAgent(Agent):

    # Construct the agent
    def __init__(self, environment, action):
        super().__init__(environment)
        self._action = action
        
    # Choose the action the agent will perform
    def _choose_action(self):
        return self._action

        