#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modeling Risk with Monte Carlo Simulation
Case Study: Coin Flipping Example

Felipe Jaramillo Penagos


"""

import numpy as np
import matplotlib.pyplot as plt

#%% Flip 20 Coins 10 Times

# Set Up Variables
number_of_coins = 20
simulations = 10
p = 0.5           # probability each coin lands in heads

# Simulate number of heads from flipping 20 coins 10 times
simulation_results = np.random.binomial(n=number_of_coins, p=p, size=simulations)

# Test whether each simulation generated exactly 10 heads
sim_has_ten_heads = np.equal(simulation_results, 10)
    # One out of 10 simulations had 10 heads (in this case)
    
# Calculate the observed probability of getting 10 heads in any given simulation
ten_heads_probability = np.equal(simulation_results, 10).mean() # mean = 0.1 (i.e 10%)

# Calculate observed probabilities of each number of heads in a simulation with 20 coins
probabilities = [np.equal(simulation_results, i).mean() for i in range(number_of_coins)]

# Plot the probability distribution
plt.figure(1)
plt.plot(list(range(number_of_coins)), probabilities)
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.show()

# We can ran the simulation more times to 
# visualize different scenarios.
r

#%% Flip 20 coins 10,000 times

# Set up variables
number_of_coins = 20
simulations_no_10k = 10000
p = 0.5

simulation_10000 = np.random.binomial(n=number_of_coins, p=p, size=simulations_no_10k)
print(simulation_10000)

probabilities_10k = [np.equal(simulation_10000, i).mean() for i in range(number_of_coins)]
print(probabilities_10k) # For each number 1-20, computes the prob for heads appearing the no. of times,

plt.figure(2)
plt.plot(list(range(number_of_coins)), probabilities_10k)
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.show()  # This is now way closer to a Normal Distribution.
            # The larger the amount of simulations, the more our distribution is accurate.
            
"""Recap:
Observations: we did not analyze any historical data in this example.
Distributions: Binomial, the probability of getting heads is a 50%
Simulations: flipping 20 coins – the 1st model ran 10 simulations, the 2nd model ran 10,000 simulations
Quantifications: our 2nd model was able to generate a consistent accurate normal distribution
"""