# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:41:22 2020

@author: peter
"""

import ee
import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt


import GPyOpt 

n = 1000

lattitude = (9.5, 11)
longitude = (55, 55.5)

#lattitude = (36.1, 24.1)
#longitude = (75.1, 89.1)

domain = [{'name': 'X-coordinates', 'type': 'continuous', 'domain': lattitude},
          {'name': 'Y-coordinates', 'type': 'continuous', 'domain': longitude}]


##########################


# Initialize the Earth Engine module.

ee.Initialize()

dem = ee.Image('USGS/SRTMGL1_003')


###########################


def objective_function(x):
    
    coordinates = x[0]
    
    xy = ee.Geometry.Point([coordinates[0], coordinates[1]])

    elev = dem.sample(xy, 30).first().get('elevation').getInfo()
    print("elevation:", elev)
    print("Coordinates:", coordinates)
    
    
    return -elev


#print(objective_function([[ 9.5000343,  55.00037209]]))


opt = GPyOpt.methods.BayesianOptimization(f = objective_function,   # function to optimize
                                              domain = domain,         # box-constrains of the problem
                                              acquisition_type = 'EI'       # Select acquisition function MPI, EI, LCB
                                             )

opt.acquisition.exploration_weight = 2

opt.run_optimization(max_iter = 40)


x_best = opt.X[np.argmin(opt.Y)]
print("The best parameters obtained: n_estimators=" + str(x_best[0]) + ", max_depth=" + str(x_best[1]) + ", max_features=" + str(
    x_best[2])  + ", criterion=" + str(
    x_best[3]))

