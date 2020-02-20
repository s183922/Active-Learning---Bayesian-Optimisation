# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:41:22 2020

@author: peter
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import GPyOpt 



domain = [{'name': 'X-coordinates', 'type': 'continous', 'domain': 'unknown'},
          {'name': 'Y-coordinates', 'type': 'continous', 'domain': 'unknown'}]


true_vals = []

def objective_function(x):
    
    params = x[0]
    
    
    
    index = 0
    
    return true_vals[index]



opt = GPyOpt.methods.BayesianOptimization(f = objective_function,   # function to optimize
                                              domain = domain,         # box-constrains of the problem
                                              acquisition_type = 'LCB' ,      # Select acquisition function MPI, EI, LCB
                                             )


