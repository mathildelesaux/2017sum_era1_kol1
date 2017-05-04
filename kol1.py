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

#addition de deux matrices / entre colones / entre lignes
#soustraction " / "
#multiplication " / "
#division " / "

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


