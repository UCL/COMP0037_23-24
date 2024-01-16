'''
Created on 14 Jan 2022

@author: ucacsjj
'''

import numpy as np

# Return an array which shows, over time the percentage of optimal actions taken.
# The input is the action_history, which is a timestep-by-timestep list of actions
# taken. The output at time T is the % of optimal actions taken up to time T, divided by the
# total time T.
def compute_percentage_of_optimal_actions_selected(environment, action_history):
    
    # Get the optimal action from the agent
    optimal_action, optimal_reward = environment.optimal_action()
    print(f'optimal_action={optimal_action}')
    
    num_actions_taken = len(action_history)
    
    correct_actions = np.zeros(num_actions_taken)
    
    for a in range(0, num_actions_taken):
        if a == 0:
            correct_actions[a] += (action_history[a] == optimal_action)
        else:
            correct_actions[a] = correct_actions[a-1] + (action_history[a] == optimal_action)
    
    return np.divide(correct_actions, np.arange(1, num_actions_taken + 1))

# Q4b:
# Compute the regret. For each timestep, compute the difference between the
# optimal return and the received return
def compute_regret(environment, reward_history):
    
    # Work out the optimal action
    optimal_action, optimal_reward = environment.optimal_action()
    
    num_actions_taken = len(reward_history)
    
    # Work out the cumulative reward
    cumulative_reward = np.cumsum(reward_history)
    
    regret = optimal_reward * np.arange(1, num_actions_taken + 1) - cumulative_reward
    
    return regret
   