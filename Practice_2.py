#Manipulation of list 
#Assigning a variable with other list and modifying the list 
x = ["John", 56, "Julie", 89, "Thomas", 96]
y = x
print (x)
y[2]="Haris"
print (y)
print (x) #x is also changed 

a = ["James", 89, "Tovino", 26, "Yule", 41]
print (a)
b = list(a) #assigning like this and modifying wont change the reference
c=a[:]
b[2]="Harris"
print (b)
print (a)
print (c)


#functions 
d = [56,89,96,23,41]
hightest = max(d) #max()
print (hightest)

r = round(56.892, 2) #round(float, decimal to which roundoff must be done)
print(r)
ro = round(56.856)
print (ro)

length_of_list = len(d) #len()
print (length_of_list)

sorted_list = sorted(d) #sorted()
print (sorted_list)#prints list in ascending order
sorted_list1 = sorted(d, reverse = True)
print (sorted_list1)#prints in the reverse order descending order

#Methods 
#each object of the class is associated with a method which is called by using the '.'
s = "lisa"
st = s.capitalize()
print (st)
sr = s.replace("l", "m")
print (sr)

i = d.index(89)
print(i)
f = d.count(96)
print (f)

rev = d[::-1] #if d.reverse() is used, it gives None as the output 
print(rev)
