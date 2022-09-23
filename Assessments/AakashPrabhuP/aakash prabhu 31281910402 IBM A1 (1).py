# -*- coding: utf-8 -*-
"""Copy of Assignment_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15lsiCSz_w2-FXH54OA1yBHPYG75b25-1

# Basic Python

## 1. Split this string
"""

s = "Hi there Sam!"

t=s.split()
print(t)

"""## 2. Use .format() to print the following string. 

### Output should be: The diameter of Earth is 12742 kilometers.
"""

planet = "Earth"
diameter = 12742

print("the diameter of {} is {} kilometers.".format(planet,diameter));

"""## 3. In this nest dictionary grab the word "hello"
"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

print(d['k1'][3]["tricky"][3]['target'][3])

"""# Numpy"""

import numpy as np

"""## 4.1 Create an array of 10 zeros? 
## 4.2 Create an array of 10 fives?
"""

arr=np.zeros(10)
print(arr)

arr1=np.ones(10)*5
print(arr1)

"""## 5. Create an array of all the even integers from 20 to 35"""

array=(np.arange(20,36,2))
print(array)

"""## 6. Create a 3x3 matrix with values ranging from 0 to 8"""

arr2=np.arange(0,9).reshape((3,3))
print(arr)

"""## 7. Concatenate a and b 
## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])
"""

a=np.array([1,2,3])
b=np.array([4,5,6])
ab=np.concatenate((a,b))
print(ab)

"""# Pandas

## 8. Create a dataframe with 3 rows and 2 columns
"""

import pandas as pd

data={"Domain":['AI','ML','DS'], "Intrest":['yes','yes','yes']}
df=pd.DataFrame(data)
print(df)

"""## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023"""

pd.date_range("01-01-2023","02-10-2023")

"""## 10. Create 2D list to DataFrame

lists = [[1, 'aaa', 22],
         [2, 'bbb', 25],
         [3, 'ccc', 24]]
"""

lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]

df=pd.DataFrame(lists,columns=['Number','Name','ID.No'])
print(df)