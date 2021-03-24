#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:40:21 2020

@author: robert

using legend
"""
import numpy as np
# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
iris_data = pd.read_csv("iris-data-set.csv") 

import matplotlib.pyplot as plt

plt.scatter(setosa_len,setosa_wid,marker = 'o',
            color = 'red', label = 'setosa')
plt.scatter(versicolor_len,versicolor_wid,marker = 'o',
            color = 'green', label = 'versicolor')
plt.scatter(virginica_len,virginica_wid,marker = 'o',
            color = 'blue', label = 'virginica')

plt.legend(loc='upper right')
plt.title('Iris data')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.show()