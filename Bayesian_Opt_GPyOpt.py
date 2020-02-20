# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:41:22 2020

@author: peter
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import GPyOpt 

n = 1000

lattitude = np.linspace(9.5, 11,  n)
longitude = np.linspace(55, 55.5, n)

domain = [{'name': 'X-coordinates', 'type': 'continous', 'domain': lattitude},
          {'name': 'Y-coordinates', 'type': 'continous', 'domain': longitude}]




def objective_function(x):
    
    coordinates = x[0]
    
    
    
    
    
    
    return true_vals[index]



opt = GPyOpt.methods.BayesianOptimization(f = objective_function,   # function to optimize
                                              domain = domain,         # box-constrains of the problem
                                              acquisition_type = 'EI' ,      # Select acquisition function MPI, EI, LCB
                                             )

opt.acquisition.exploration_weight = 2

opt.run_optimization(max_iter = 15) 


