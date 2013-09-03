# version code 988
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one
from vecutil import *
import echelon
from solver import solve
from math import sqrt


## Problem 1
# Write each matrix as a list of row lists

echelon_form_1 = [[1,2,0,2,0],
									[0,1,0,3,4],
									[0,0,2,3,4],
									[0,0,0,2,0],
									[0,0,0,0,4]]

echelon_form_2 = [[0,4,3,4,4],
									[0,0,4,2,0],
									[0,0,0,0,1],
									[0,0,0,0,0]]

echelon_form_3 = [[1,0,0,1],
									[0,0,0,1],
									[0,0,0,0]]

echelon_form_4 = [[1,0,0,0],
									[0,1,0,0],
									[0,0,0,0],
									[0,0,0,0]]



## Problem 2
def is_echelon(A):
		'''
		Input:
				- A: a list of row lists
		Output:
				- True if A is in echelon form
				- False otherwise
		Examples:
				>>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
				True
				>>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
				False
		'''
		longest,B = 0,A[:]
		B.reverse()
		for row in B:
			if longest!=0 and location_first_non_zero(row) <= longest:
				return False
			longest=location_first_non_zero(row)
		return True

def location_first_non_zero(x):
	y,ans=x[:],len(x)
	while ans>0 and y[0]==0:
		ans-=1
		y.pop(0)
	return ans
	
## Problem 3
# Give each answer as a list

echelon_form_vec_a = [1,0,3,0]
echelon_form_vec_b = [-3,0,-2,3]
echelon_form_vec_c = [-5,0,2,0,2]



## Problem 4
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None".

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21,0,2,0,0]



## Problem 5
def echelon_solve(rowlist, label_list, b):
		'''
		Input:
				- rowlist: a list of Vecs
				- label_list: a list of labels establishing an order on the domain of
											Vecs in rowlist
				- b: a vector (represented as a list)
		Output:
				- Vec x such that rowlist * x is b
		>>> D = {'A','B','C','D','E'}
		>>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})] 
		>>> b_list = [one,0,one]>>> cols = ['A', 'B', 'C', 'D', 'E']
		>>> echelon_solve(U_rows, cols, b_list)
		Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
		'''
		D = rowlist[0].D
		x = zero_vec(D)
		for j in reversed(range(len(b))):
			row = rowlist[j]
			first_nz=first_non_zero(row,label_list)
			if first_nz:
				x[first_nz] = (b[j] - x*row)/row[first_nz]
		return x

def first_non_zero(row,label_list):
	for e in label_list:
		if row[e]!=0:
			return e
	# else:
	# 	return False


## Problem 6
def echsolve(A, b):
    M = echelon.transformation(A)
    U = M*A
    col_label_list = sorted(A.D[1])
    U_rows_dict = mat2rowdict(U)
    rowlist = [U_rows_dict[i] for i in U_rows_dict]
    return echelon_solve(rowlist,col_label_list, M*b)

A=Mat(({'a','b','c','d'},{'A','B','C','D'}),{('a',"A"):one,('a',"B"):one,('a',"D"):one,('b',"A"):one,('b',"D"):one,('c',"A"):one,('c',"B"):one,('c',"C"):one,('c',"D"):one,('d',"C"):one,('d',"D"):one })
M = Mat(({0,1,2,3},{'a','b','c','d'}),{(0,"a"):one,(1,"a"):one,(1,"b"):one,(2,"a"):one,(2,"c"):one,(3,"a"):one,(3,"c"):one,(3,"d"):one})
U = M*A
label_list = sorted(A.D[1])
U_rows_dict = mat2rowdict(U)
rowlist = [U_rows_dict[i] for i in U_rows_dict]
D={"A","B","C","D"}
g=Vec({'a','b','c','d'},{"A":one,"C":one})
# b=zero_vec({'a','b','c','d'})
b=M*Vec({'a','b','c','d'},{"a":one,"c":one})
b=[one,one,0,0]
#print(echsolve(A,g))

## Problem 7
null_space_rows_a = {3,4} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {4}

def project_along(b, a): 
	return ((b*a)/(a*a) if a*a != 0 else 0)*a

def project_orthogonal(b, a): 
	return b - project_along(b, a)


## Problem 9
# Write each vector as a list
closest_vector_1 = [1.6,3.2]
closest_vector_2 = [0,1,0]
closest_vector_3 = [3,2,1,-4]



## Problem 10
# Write each vector as a list


A = list2vec([3,0])
B = list2vec([2,1])
project_onto_1 = list(project_along(B,A).f.values())
projection_orthogonal_1 = list(project_orthogonal(B,A).f.values())

A = list2vec([1,2,-1])
B = list2vec([1,1,4])
project_onto_2 = list(project_along(B,A).f.values())
projection_orthogonal_2 = list(project_orthogonal(B,A).f.values())

A = list2vec([3,3,12])
B = list2vec([1,1,4])
project_onto_3 = list(project_along(B,A).f.values())
projection_orthogonal_3 = list(project_orthogonal(B,A).f.values())



## Problem 11
v = list2vec([2,2,1])
norm1 = sqrt(v*v)
v = list2vec([sqrt(2),sqrt(3),sqrt(5),sqrt(6)])
norm2 = sqrt(v*v)
norm3 = 1

