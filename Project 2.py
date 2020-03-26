#!/usr/bin/env python
# coding: utf-8

# In[160]:


from scipy.spatial import distance
import pandas as pd
import random, numpy, math, copy, matplotlib.pyplot as plt
test_set = pd.read_csv("C:/Users/horwe/Desktop/Y4s2/Computation Thinking/OWN/data/flags_r1.csv") #replace with own file directory

#naming columns of given data 
test_set.columns = ['flag_ID', 'points','x-coordinate','y-coordinate']

#adding starting coordinate 0,0
starting_point = (0,0)

#creating new columns: distance to get euclidean distance from (0,0), value_for_distance for points/distance
for flag in test_set:
    test_set['distance'] = (test_set['x-coordinate']**2 + test_set['y-coordinate']**2)**0.5
    test_set['value_for_distance'] = test_set['points'] / test_set['distance']

print(test_set)

#creating list to store sequence of flags
sequence =[]

#creating list to store points 
points = []

#first flag will be the one that has lowest distance to (0,0)
#append flag_ID to sequence(not sure how to get rid of ID....)
sequence.append(test_set.flag_ID[test_set.value_for_distance == test_set.value_for_distance.max()])

#update number of points

print(sequence)


    





