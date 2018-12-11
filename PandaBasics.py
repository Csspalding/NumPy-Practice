# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:10:49 2018
Tutorial http://www.learnpython.org/en/Pandas_Basics

Pandas is a high-level data manipulation tool developed by Wes McKinney. 
It is built on the Numpy package and its key data structure is called the DataFrame. 
DataFrames allow you to store and manipulate tabular data in rows of observations 
and columns of variables.
@author: Cassie
"""

#creating a DataFrame from a Python Dictionary

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

#automatically making brics a DataFrame gives the dictionary items in this case Countries 
#a numerical index, 
#Instead to use the first two letters of each country instead using <dateframename>.index

# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)

#Another way to create a DataFrame is by importing a csv file using Pandas.

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)