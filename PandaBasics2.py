# -*- coding: utf-8 -*-
"""
NB this code does not run
Created on Wed Nov 21 19:23:05 2018
Tutorial http://www.learnpython.org/en/Pandas_Basics
@author: Cassie
"""

import pandas as pd

# Import the cars.csv data: cars

#cars = pd.read_csv('cars.csv')

# Print out cars

#print(cars)

#There are several ways to index a Pandas DataFrame. One of the easiest ways
# to do this is by using square bracket notation.
#read just one index column from the file

cars = pd.read_csv('cars.csv', index_col = 0)

#Square brackets can also be used to access observations (rows) from a DataFrame. 

# Print out country column as Pandas Series
print(cars['cars_per_cap'])

# Print out country column as Pandas DataFrame
print(cars[['cars_per_cap']])

# Print out DataFrame with country and drives_right columns
print(cars[['cars_per_cap', 'country']])

# Print out first 4 observations
print(cars[0:4])

# Print out fifth, sixth, observation
print(cars[4:6])

#use loc and iloc to perform just about any data selection operation.
# loc is label-based, which means that you have to specify rows and columns based
# on their row and column labels. iloc is integer index based, 
#so you have to specify rows and columns by their integer index

# Print out observation for Japan
print('Observations for Japan:')
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print('Observations for Austrialia and Egypt:')
print(cars.loc[['AUS', 'EG']])











