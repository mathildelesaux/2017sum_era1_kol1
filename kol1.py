#Write a library that contains a class that can represent any 2𝑥2 real matrice. 
#Include two functions to calculate the sum and product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
#Examples:
#
# matrix_1 = Matrix(4,5,6,7)
# matrix_2 = Matrix(2,2,2,1)
#
# matrix_3 = matrix_2.add(matrix_1)
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#(If you want you can expand implementation to NxN matrix.)
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#When you are done upload this code to your github repository. 
#The whole repository MUST be a fork from https://github.com/mwmajew/2017sum_era1_kol1
#
#Delete these comments before commit!
#Good luck.

import numpy as np

A=[(4,5),(6,7)]
B=[(2,2),(2,1)]

#Transpose

print(np.transpose(A))

#Déterminant

print(np.linalg.det(A))

#Inversion

print(np.linalg.inv(A))

#Addition of 2 matrix

def sum_2matrix (A,B):
    C = []
    for list1, list2 in zip(A,B):
        C.append([list1[i]+list2[i] for i in range(len(list1))])
    return C

print(sum_2matrix (A,B))

#Soustraction of 2 matrix

def sous_2matrix (A,B):
    C=[]
    for list1, list2 in zip(A,B):
        C.append([list1[i]-list2[i] for i in range(len(list1))])
    return C

print(sous_2matrix (A,B))

#Multiplication of 2 matrix

def multiply_2matrix (A,B):
    C=[]
    for list1, list2 in zip(A,B):
        C.append([list1[i]*list2[i] for i in range(len(list1))])
    return C

print(multiply_2matrix (A,B))

#Divid 2 matrix

def divid_2matrix (A,B):
    C=[]
    for list1, list2 in zip(A,B):
        C.append([list1[i]/list2[i] for i in range(len(list1))])
    return C

print(divid_2matrix (A,B))

#

def add_line (A,B):
    C=[]
    for list1, list2 in zip(A,B):
        C.append([list1[i] for i in range(len(list1))])
    return C

print(add_line (A,B))

#Product Matrix

def mat_product (A, B):
    C=np.dot(A,B)
    return C

print(mat_product(A,B))

#Addition line by line

def sum_line(A):
    sum=np.sum(A,axis=1)
    return sum
print (sum_line (A))

#Addition col by col

def sum_col (A):
    sum=np.sum(A,axis=0)
    return sum
print(sum_col(A))

#Mean by line

def mean_line(A):
    return np.mean(A,axis=0)
print(mean_line(A))

#Mean by col

def mean_col(A):
    return np.mean(A,axis=1)
print(mean_col(A))


A=np.array([(4,5),(6,7)])

#Min 

def min (A):
    return A.min()
print(min(A))

#Max

def max (A):
    return A.max()
print(max(A))
