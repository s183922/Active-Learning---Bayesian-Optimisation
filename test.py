# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 20:31:36 2020

@author: peter
"""


import pandas as pd
import numpy as np
import scipy.stats as scistat
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import sys

os.chdir(sys.path[0])

# Read Data and initialise Top heights and corresponding coordinates.

BO = pd.read_csv("df_BO1.csv")
Random = pd.read_csv("df_random1.csv")
Keys = ["Alps", "Kaukasus", "Fyn / Germany", "Himmalaya"]
tops = [4810, 4000, 168, 8848]
top_coords = [np.array([6.865575, 45.832119]),  np.array([42.4392,43]), np.array([[10.725150,10.112292],[55.338056,54.207114]]), np.array([86.922623,27.986065])]

# For images... To be implemented
extends = [[6,8,45,47], [41,43,41,43],[10,12,54,56],[86,88,27,29]]

# Plot elevations levels found by BO and random guessing.
fig = plt.figure(figsize = (20,20))
for j in range(4):
    fig.add_subplot(2,2,j+1)

    # Rearrange Data
    df = pd.DataFrame.from_records([np.array(eval(BO.iloc[j,i].replace("\n","").replace("array",""))[1]).flatten() for i in range(1,11)]) 
    df2 = pd.DataFrame.from_records([np.array(eval(Random.iloc[j,i].replace("\n","").replace("array",""))[1]).flatten() for i in range(1,11)])

    plt.plot(df.max().to_numpy(), c = 'blue', alpha = 0.2, linestyle = 'dashed', label = 'Max Bayesian Opt.')
    # plt.plot(df2.max().to_numpy(), c = 'red', alpha = 0.2, linestyle = 'dashed')
    plt.plot(df.mean().to_numpy(), c = 'blue', label = 'Mean Bayesian Opt.')
    plt.plot(df2.mean().to_numpy(), c = 'red', label = 'Mean Random')

    plt.vlines(np.arange(0,50), df.mean().to_numpy()-df.std().to_numpy(),df.mean().to_numpy()+df.std().to_numpy(), colors = 'blue', alpha = 0.3)
    plt.vlines(np.arange(0,50), df2.mean().to_numpy()-df2.std().to_numpy(),df2.mean().to_numpy()+df2.std().to_numpy(), colors = 'red', alpha = 0.3)
    plt.hlines(tops[j], 0, 49, linestyles='dashed',alpha = 0.5, label = 'Max Height')
    plt.title(Keys[j])
    plt.grid(linestyle='dashed')
    plt.legend()
plt.show()

# Heatmap / 2d histograms for guesses by BO
fig = plt.figure(figsize = (20,20)) 
for j in range(4):
    fig.add_subplot(2,2,j+1)

    # Rearrange data
    df = pd.DataFrame.from_records([np.array(eval(BO.iloc[j,i].replace("\n","").replace("array",""))[0]).flatten() for i in range(1,11)])
    df2 = pd.DataFrame.from_records([np.array(eval(Random.iloc[j,i].replace("\n","").replace("array",""))[0]).flatten() for i in range(1,11)]).iloc[0,:].to_numpy().reshape(50,2)
    x = df[df.columns[::2]].to_numpy().flatten()
    y = df[df.columns[1::2]].to_numpy().flatten()
    plt.hist2d(x[~np.isnan(x)], y[~np.isnan(y)], bins = 50)
    plt.colorbar()

    # For images - Still not working...
    # img = mpimg.imread('Desktop\\img_{:}.png'.format(Keys[j]))
    # plt.imshow(img, origin='lower', extent = extends[j])

    plt.scatter(top_coords[j][0], top_coords[j][1], c = 'red') # Marks peaks.
    plt.title(Keys[j])
plt.show()



