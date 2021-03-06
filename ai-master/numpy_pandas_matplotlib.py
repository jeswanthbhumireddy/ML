# -*- coding: utf-8 -*-
"""numpy_pandas_matplotLib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oxhnqrohsvxH-EtpIpJA5L5Bjv3UNbvr

# NumPy

NumPy is a Python mathematical library for Machine Learning and scientific computing

In Machine Learning typically data is provided in tabular format (rows and columns ). We need to understand the basics on NumPy Arrays which will be used to store data for Machine learning programming

import NumPy
"""

import numpy as np

"""Create an one dimensional array from a Python List"""

sample_list = [10,20,30,40,50,60]

sample_numpy_1d_array = np.array(sample_list)

print(sample_numpy_1d_array)

type(sample_numpy_1d_array)

"""2 Dimensional NumPy Array"""

sample_numpy_2d_array = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
sample_numpy_2d_array

sample_numpy_2d_array.reshape(2,6)

sample_numpy_2d_array.reshape(4,3)

sample_numpy_2d_array.reshape(1,-1)

sample_numpy_2d_array.reshape(-1,1)

sample_numpy_2d_array_2 = np.array([[1,2,3,4],[40,50,60,50],[7,8,9,12],[10,11,12,13]])
sample_numpy_2d_array_2

"""You can slice and dice a NumPy array the same way we slice and dice a Python List"""

sample_numpy_2d_array_2[1:3,2:4]

sample_numpy_2d_array_2.mean()

np.median(sample_numpy_2d_array_2)

# To calcualte mode use scipy funciton
from scipy import stats
print(stats.mode([1,2,2,3,3,3,4,4,4,4,5,5]))

"""# Pandas

Pandas is an open source library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
"""

import pandas as pd

sample_series = pd.Series ([10,20,30,40])
sample_series

type(sample_series)

sample_series_2 = pd.Series ([10,20,30,40],['A','B','C','D'])
sample_series_2

sample_series_2[2]

sample_series_2['C']

sample_dataframe = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
sample_dataframe

sample_dataframe_2 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],['Row1','Row2','Row3','Row4'],['Column1','Column2','Column3'])
sample_dataframe_2

sample_dataframe_2['Column3']

type(sample_dataframe_2['Column3'])

sample_dataframe_2[['Column1','Column3']]

sample_dataframe_2.loc['Row1']

sample_dataframe_2.loc[['Row2','Row3'],['Column2','Column3']]

sample_dataframe_2

sample_dataframe_2.iloc[0:2, 1:3]

sample_dataframe_2.iloc[1:2, 2:4]

sample_dataframe_2.iloc[:, :-1]

type(sample_dataframe_2.iloc[:, :-1])

# convert Pandas to NumPy
sample_dataframe_2.iloc[:, :-1].values

sample_dataframe_2.iloc[:, -1]

type(sample_dataframe_2.iloc[:, -1])

sample_dataframe_2.iloc[:, -1].values

type(sample_dataframe_2.iloc[:, -1].values)

sample_dataframe_2

sample_dataframe_2['Column1']>4

sample_dataframe_2[sample_dataframe_2['Column1']>4]

df = pd.read_csv("https://raw.githubusercontent.com/futurexskill/ai/master/customerpurchase.csv")
df

type(df)

df.describe()

df.info()

df.head()

df.head(2)

# customers who purcased
df[df['Purchased']== 1]

# Customers with age < 30

df[df['Age']< 30 ]

# Store Age and Salary in  a 2D array
X = df.iloc[:, :-1].values
X

type(X)

# Store Purchase information in an array
y = df.iloc[:, -1].values
y

"""# MatPlotLib"""

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,25,35,40,50,60,80,90,95,100]

plt.plot(x,y)

plt.scatter(x,y)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sample plot')
plt.plot(x,y)

df

plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Salary Analysis')
plt.plot(df['Age'],df['Salary'])

plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Salary Analysis')
plt.scatter(df['Age'],df['Salary'])

plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Salary Analysis')
plt.scatter(df['Age'][df['Salary']>50000],df['Salary'][df['Salary']>50000],c = 'orange')
plt.scatter(df['Age'][df['Salary']<=50000],df['Salary'][df['Salary']<=50000],c = 'black')

# histogram
plt.hist([10,20,20,30,30,30,40,40,50])

"""## Further read


## http://www.numpy.org/

## https://pandas.pydata.org/ 

## https://matplotlib.org/
"""