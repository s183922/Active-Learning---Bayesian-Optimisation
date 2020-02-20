# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:41:22 2020

@author: peter
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import GPyOpt 

n = 100

lattitude = (9.5, 11)
longitude = (55, 55.5)

domain = [{'name': 'Xcoordinates', 'type': 'continuous', 'domain': lattitude},
          {'name': 'Ycoordinates', 'type': 'continuous', 'domain': longitude}]


true_vals = np.linspace(0,100,100)

# plt.plot(2*longitude**2/lattitude**2*200*np.sin(longitude*2))

def objective_function(x):
    
    coordinates = x[0]
    print(coordinates)

    obj = 2
    return obj



opt = GPyOpt.methods.BayesianOptimization(f = objective_function,   # function to optimize
                                              domain = domain,         # box-constrains of the problem
                                              acquisition_type = 'EI'      # Select acquisition function MPI, EI, LCB
                                              )

opt.acquisition.exploration_weight = 2

opt.run_optimization(max_iter = 10) 


x_best = opt.X[np.argmin(opt.Y)]

# print("The best parameters obtained: n_estimators=" + str(x_best[0]) + ", max_depth=" + str(x_best[1]) + ", max_features=" + str(
#     x_best[2])  + ", criterion=" + str(
#     x_best[3]))