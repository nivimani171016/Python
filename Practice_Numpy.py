# -*- coding: utf-8 -*-
#importing a package 
import numpy #or import numpy as np 
n = numpy.array([1,2,3,4,5])
print (n)

# to import only the array from the numpy 
from numpy import array 
m = array([5,6,8])
print (m)

#importing a math 
import math as m
p = m.pi 
r = 5.6
circumference = 2*p*r
area = p*(r**2)
print (circumference)
print (area)

#calculation of radians 
r = 156253
phi = 12
from math import radians
dist = r*(radians(phi))#convert a degree to radians
print (dist)

#list vs numpy array 
l1_hgt = [5.5,5.3,6.1,5.9,6.0]
l2_wgt = [69,56,78,59,65]
#instead use the array 
#Numeric Python 
hgt = numpy.array(l1_hgt)
wgt = numpy.array(l2_wgt)
print (hgt)
print (wgt)
Bmi = hgt/wgt * 100
print (Bmi) #corresponding value 
#numpy array should contain only one data type

print (l1_hgt+l2_wgt) #concatenate list
print (hgt + wgt) #addition of corresponding value 

print (Bmi[2])
print (Bmi>7)
print (Bmi[Bmi>9]) #subseeting only the array elements greater than 9
print(type(wgt))#ndarray-n dimensional array

#2D Array 
np_array = array([[58,96,46,45,26],
                 [89,56,12,39,75]])
print (np_array)
print (np_array[0])
print (np_array[0][2]); print (np_array[1][1])
print (np_array[0,2])# [row, column]
print (np_array[:,2])#column 3 for all row is printed 
#np.mean(arrayname[:,])
#np.median(arrayname[:,])
#np.std()
#np.column_stack(array, array)#paste two data as columns together
#np.corrcoef(array[:,0],array[:,1])#finding correlation between 2 columns of a array
