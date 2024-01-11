'''
Created on 14 Jan 2022

@author: ucacsjj
'''

from .agent import Agent

# This agent randomly picks action. It subclasses from Agent, and
# inherits all the base class book keeping.

class RandomActionAgent(Agent):

    # Construct the agent. Because there is no special construction
    # for this class, we could skip explicitly writing the constructor
    # because it would be deferred automaticaly to the base
    # class. However, I personally prefer to include the class to
    # remind myself of what the constructor is doing.
    def __init__(self, environment):
        super().__init__(environment)
        
    # Q3a:
    # Choose a random action the agent will perform
    def _choose_action(self):
        return 0

        
