# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 12:53:51 2022

@author: Home
"""
#Python Basics
#Variable declaration
i = 10
print(i)

tp ="The type of the i is:" + str(type(i))
print (tp)

k=3+4j
print(type(k))
if (type(k)==complex):
    print ("the K is complex number")
else:
    pass

"""This is a multiple line str""" #multiple line comment

#conditional statement 
if (i>=10):
    print("i is greater than 10")
else:
    print("i is less than 10")
    
#elseif statemnt 
if (i>10):
    print("i is greater than 10")
elif(i==10):
    print("i is equal to 10")
else:
    print("i is less than 10")
    
#to find the index of the variable 
print("The index of the variable is : " + str(id(i)))

#creating of a list (either way can be used) a=[], b=list()
a=["typo", 56, "56.0", "hello", 56.2]
print (type(a[0]))
print(a)
print(a[0:3:2])#starting index, ending index, interval

#printing only the string in the list 
for j in a:
    if (type(j)==str):
        print (j)
        
b=list()  #creating a list to append      
for j in a:
    if (type(j)==str):
        b.append(j)
print(b)

#find the difference        
c=list("sudo")
d=list(["sudo", "spt"])
print(c)
print(d)

#reverse of a string 
e="styur"
print("the reverse of the string is " + e[::-1])
#same does for the list 

#use of 'append' to add the given at the end 
f=[]
f.append("str")
f.append("join")
print (f)

#use of 'insert' to insertt a data anywhere in the list 
f.insert(0, (["str", "true", 56]))
print(f) #list inside the list 
f.insert(-1, "tyopo")#doubt in this#
print(f)
print(f[0][::-1])#access the list inside the list and reverse it 
print(f[0][0][::-1])#access the element of the list insided the list and reverse it 

#to access the list which is inside the list 
print(f[0])
print(f[0][0])

#concatenate a string and list
print ("str" + "fyk")
print (d + f) #find the difference between concatenate and appending a list here

#Manipulation of list 
e=["sir", "Ghosh", 56, 78]
f=e+["56", "Ele"] #insertion of new elements of list
print (f)
del(f[4]) #deletion of a list element 
print (f)