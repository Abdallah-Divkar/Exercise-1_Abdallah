# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 20:25:00 2024

@author: Abdallah Divker
"""

# Importing necessary libraries with conventional aliases for clarity
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler  

# Constants for easy configuration and readability
SEED = 41  
UNIFORM_LOW = -15  
UNIFORM_HIGH = 15  
SAMPLE_SIZE = 100  
LINEAR_COEFFICIENT = 12  
LINEAR_INTERCEPT = -4  
NOISE_MEAN = 0  
NOISE_STD = 5  

# Setting a random seed for reproducibility
np.random.seed(SEED)

# Sampling from a uniform distribution
x = np.random.uniform(UNIFORM_LOW, UNIFORM_HIGH, SAMPLE_SIZE)

# First Plot: Calculating y using y = 12x - 4 (without noise)
y = LINEAR_COEFFICIENT * x + LINEAR_INTERCEPT

# Plotting values without noise
plt.scatter(x, y, alpha=0.5)
plt.title("Scatter Plot without Noise")
plt.xlabel("Sample Input (x)")
plt.ylabel("Linear Output (y)")
plt.show()

# Adding Gaussian noise to y
noise = np.random.normal(NOISE_MEAN, NOISE_STD, SAMPLE_SIZE)
y_noise = LINEAR_COEFFICIENT * x + LINEAR_INTERCEPT + noise

# Second Plot: Plotting values with noise
plt.scatter(x, y_noise, alpha=0.5)
plt.title("Scatter Plot with Noise")
plt.xlabel("Sample Input (x)")
plt.ylabel("Noisy Output (y)")
plt.show()
