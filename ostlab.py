# -*- coding: utf-8 -*-
"""OST_LAB_1918111.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jVwKrR2ROPp7UEf51OgHYwzpXVlcrf0M

#Exp no:1 a) Simple Calculator
"""

a = int(input("Enter a num1  "))
b = int(input("Enter a num2  "))

i=1
while i==1:
 print("1 for addition   2 for Subtraction  3 for Subtraction   4 for Integer Divison  5 for floor Division")
 c = int(input("Enter choice  "  ))

 if c==1:
  print("Addition is ",a+b)
 elif c==2:
  print("Subtraction is",a-b)
 elif c==3:
  print("multiplication is ",a*b)
 elif c==4:
  print("integerDivision is",a//b)
 elif c==5:
  print("floor division is",a/b)
 else:
  print("enter correct choice  ")
 i= int(input("press 1 to continue  "))

"""#b) Stack Implementation"""

stack=[]
a = 1
while a==1:
  print("choose ")
  print("1.Push  2.Pop  3.Top")
  c=int(input("Enter your choice  :"))
  if c==1:
    v = int(input("Enter a value to push   :"))
    stack.append(v)
  elif c==2:
    if len(stack) ==0:
      print("Stack is empty") 
    else:
      v= stack.pop()
      print("Deleted value is   :",v)
  elif c==3:
    if len(stack) ==0:
      print("Stack is empty") 
    else:
      top=stack[-1]
      print("top value is   :",top)
  else:
    print("wrong choice")
    break
  a=int(input("enter 1 to continue : "))

"""**1.c)Python program to convert celcius to farenheit**"""

celcius = int(input("Enter the Celcius value\:  "))
f = (celcius*1.8)+32
print("Farenheit for",celcius,"degree Celcius is",f,"Farenheit")

"""#Exp no:2

**2. a) Write a python program to find the largest among three numbers.**
"""

a = int(input("enter first number:  ")) 
b = int(input("enter Second  number:  ")) 
c = int(input("enter third number:  ")) 
if a >=b and a >= c:
  print("Largeest Number is ", a)
elif b >= a and b >=c:
  print("Largest Number ", b)
else:
  print("Largeest Number is ",c)

a = int(input("enter first number:  ")) 
b = int(input("enter Second  number:  ")) 
c = int(input("enter third number:  ")) 
largest = max(a,b,c)
print("largest number is",largest)

"""**2. b) Write a python program to print the Fibonacci sequence.**"""

len =int(input("Enter no of terms  :"))
n1,n2 = 0,1
if len<=0:
  print(" Enter the positive integer!!!")
else:
  print("Fibonacci Sequence")
i=0
while i < len :
    print(n1)
    n = n1+n2
    n1 = n2
    n2 = n
    i=i+1

"""**2. c) Write a python program to reverse the given number.**

"""

num = int(input("enter a number to be reverse   :"))
rem=0
res =0
while num>0:
  rem= num%10
  res = (res*10)+rem
  num=num//10
print("Reversed Number is :",res)

num = input("enter a number to be reverse   :")
res = num[::-1]
print("reversed number is",res)

"""# Exp no:3

**3 a. Write a python script to sort n numbers using lists without using built-in functions.**

without using builtin functions
"""

list =[]
length = int(input("Enter the no of elements in list  "))
print("Enter",length,"elements")
for i in range(0,length):
  value = int(input())
  list.append(value)
print("List before Sorting")
for i in list:
  print(i ,end = " ")
for i in range(length):
  for j in range(i,length):
    if list[i]>list[j]:
      list[i],list[j]=list[j],list[i]
print("")
print("List after Sorting in Ascending order is")
for i in list:
  print(i ,end = " ")

"""using Builtin funtion"""

list =[]
length = int(input("Enter the no of elements in list  "))
print("Enter",length,"elements")
for i in range(0,length):
  value = input()
  list.append(value)
print("List before Sorting")
for i in list:
  print(i ,end = " ")
print(" ")
list.sort()
print("List after Sorting in Ascending order is")
for i in list:
  print(i ,end = " ")

"""**3 b. Write a python script to accept a list with different datatypes - int, string and float(heterogeneous) and partition it into 3 lists each of which contains same data types(homogeneous)**"""

list =["Hello",77,89.98,66,111.107,"hii"]
float_list =[]
int_list =[]
str_list =[]
for i in list:
  if  isinstance(i,int):#if str(i)==i:
    int_list.append(i)
  elif isinstance(i,float):#if int(i)==i:
    float_list.append(i)
  elif isinstance(i,str):# if float(i)==i
    str_list.append(i)
print("List is: ")
print(list)
print("Integer list is:")
print(int_list)
print("Float list is:")
print(float_list)
print("String list is:")
print(str_list)

""".
**3 c. Write a python script to create a dictionary of minimum five key/value pairs. Implement search, modification and removal of elements from the dictionary**
"""

dict= {}
a = int(input("Enter the no of key value pairs: "))
while(a>0):
  key = input("Enter the  key: ")
  value = input("Enter the value: ")
  dict[key] = value
  a=a-1
print(dict)  
a=1
while a==1:
  print("1 for Update , 2 for Search, 3 for Deletion")
  ch = int(input("Enter Your Choice: "))
  if ch ==1:
    k = input("Enter Key: ")
    v = input("Enter pair: ")
    dict[k]=v
  elif ch==2:
    k = input("Enter Key: ")
    if k in dict:
      print(k, "is found")
      print(k,":",value)
    else:
      print("No key value pairs found: ")
  elif ch ==3:
     k = input("Enter Key: ")
     if k in dict:
      del dict[k]
     else:
       print(k,"is not found in dict")
     print(dict)
  a = int(input("Press 1 to Continue: "))

"""**3 d. Write a python script to create a tuple containing both odd and even numbers. Divide the tuple into two each of which contains odd numbers and even numbers.**"""

def splitevenodd(Tuple): 
   evenlist = [] 
   oddlist = [] 
   for i in Tuple: 
      if (i % 2 == 0): 
         evenlist.append(i) 
      else: 
         oddlist.append(i) 
   tupleOdd = tuple(oddlist)
   tupleEven = tuple(evenlist)
   print("Even lists:", tupleEven) 
   print("Odd lists:", tupleOdd) 
  
A=list()
Tuple = tuple()
n=int(input("Enter the size "))
print("Enter the Element ")
for i in range(int(n)):
   k=int(input(""))
   A.append(k)
Tuple = tuple(A)
print("Tuple Elements : ", Tuple)
splitevenodd(Tuple)

"""**4 a. Write a Python program to count the occurrences of each word in a given sentence.**"""

string = input("Enter the Sentence: ")
str_list = string.split(" ")
print(str_list)
unique_words = set(str_list)
for i in unique_words:
  print("the Frequency of",i,"is:",str_list.count(i))

"""**4 b. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to  except the first char itself. (Sample String : 'restart'
Expected Result : 'resta$t')**


"""

string = input("Enter the Sentence: ")
firstLetter = string[0]
opString = string[1:].replace(firstLetter,'$')
print(firstLetter+opString)

"""**4 c. Write a Python program to count the number of lines in a text file**"""

file = open("file.txt",'r')
count =0
content = file.read()
list1= content.split("\n")
print(list1)
print("The number of lines in file is:", len(list1))
# for i in list1:
#   count+=1
# print(count)

"""**4 d. Write a Python program to copy the contents of a file to another file**"""

import shutil
shutil.copyfile('firstfile.txt','secondfile.txt')
print("file copied sucessfully")

# with open('firstfile.txt','r') as firstfile, open('secondfile.txt','a') as secondfile:
#   for line in firstfile:
#      secondfile.write(line)

"""#Expno:5

**5)a)Write a python program to create an exception for getting age of a person**
"""

try:
  age = int(input("Enter the Age: "))
  if(age<0):
   raise ValueError
  if(age>18 and age<150):
   print("you are eligible for voting")
  if(age>150):
   raise ValueError
except ValueError :
  print("Value Error:Invalid age ")

"""# Exp no:10

**Write a NumPy program to compute sum of two arrays, sum of all array elements, square root of two arrays, sum of each column and each row of two arrays and transpose of two arrays.**
"""

import numpy as np
a=np.array([10,20,30,40,50])
b=np.array([10,20,30,40,50])
c=np.add(a,b)
print("The sum of 2 Arrays =",c)
d=np.sum(a)
print("The Sum of Elements of Arrays =",d)
print("The Sqrt of Array A elements = ",np.sqrt(a))
print("The Sqrt of Array B elements = ",np.sqrt(b))
e=np.array([a,b,c,b,a])
print(e)
print("Sum of Columns:",e.sum(axis=1))
print("Sum of Rows:",e.sum(axis=0))
print("The Transpose of Array = ",e.transpose())

"""#Exp no:11

**11(a)
Write a NumPy program to compute the x and y coordinates for points on a sine curve and plot the points using matplotlib.**
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,3*np.pi,0.2)
y=np.sin(x)
print("Plot the points using matplotlib:")
plt.plot(x,y)
plt.show()

"""**11 (b)
Import python statistical packages and illustrate the calculation of mean of a sample with 10 data points**
"""

import statistics as st
l1 =[]
n=int(input("Enter the no.of.elements:"))
print("Enter the Elements:")
for i in range(n):
  l1.append(int(input()))
print("The mean is ",st.mean(l1))