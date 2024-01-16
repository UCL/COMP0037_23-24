#!/usr/bin/env python3

'''
Created on 13 Jan 2022

@author: ucacsjj
'''

import matplotlib.pyplot as plt
import numpy as np

from bandits.bandit import Bandit

if __name__ == '__main__':
    
    # Q1b:
    # Vary the number of times the agent gets fired to see what you find out
    number_of_steps = 1000

    # Array to store the reward
    rewards = np.zeros(number_of_steps)

    # Q1a: Create a bandit object here with the right mean and
    # covariance and use the pull_arm method to query the reward from
    # the bandit a large number of times. We use this iterative one
    # sample-at-a-time approach because this is used later for the
    # different learning frameworks we will encounter.
    bandit = Bandit(1, 2)
    for s in range(0, number_of_steps):
        rewards[s] = bandit.pull_arm()

    # Generate the plots below. Please note that we use labels, titles and
    # captions. We expect you to do this in any material you submit,
    # because labelling graphs is fundamental to presenting and analysing
    # results.
        
    # Generate the reward plot
    plt.xlabel('Sample number')
    plt.ylabel('Reward')
    plt.plot(rewards, color = 'red', label = 'Reward')
    
    # Generate the histogram of the reward plot
    plt.figure()    
    n, bins, patches = plt.hist(rewards, 50, density=True, facecolor='g', alpha=0.75)
    plt.xlabel('Rewards')
    plt.ylabel('Probability')
    plt.title('Reward Histogram')
    plt.grid(True)

    print(f'batch mean={np.mean(rewards)}, batch sigma={np.std(rewards)}')    

    # Q1c:
    # Change the way the reward is computed to use the iterative expression
    # instead of storing an array of all rewards and computing the mean
    # at the end
    recursive_q = rewards[0]
    for s in range(1, number_of_steps):
        recursive_q = recursive_q + (rewards[s] - recursive_q) / (s + 1)

    print(f'recursive mean={recursive_q}')
    
    # Do not block on the individual plots. Instead, wait for key press
    plt.ion()
    plt.show()
    plt.pause(0.001)
    input()
