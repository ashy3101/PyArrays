#Example of accepting values from users and creating array from those

#importing array
from array import *

#syntax of defining an empty integer array in python
arr=array('i',[])
print(arr)

#ask users total number of values he want
x= int(input("Enter total number of values "))

#taking each value and using append to store that value in array (using for loop)
for i in range(x):
    x=int(input("Enter next value "))
    arr.append(x)

#priting newly created array
print(arr)

#write your queries at--> ashy3101@gmail.com