#!/usr/local/bin/python3
from vec import Vec
from mat import Mat
from GF2 import one
from matutil import *
from vecutil import *
from solver import solve
from math import pi
import hw4
import hw5
import hw6
from image_mat_util import *
from geometry_lab import *
from perspective_lab import *
from triangular import triangular_solve_n

def MySolve(M,v):
	print("Matrix: %s\nVec: %s\n solution:%s\ns*M=%s\nCheck:%s" % (M,v,solve(M,v),M*solve(M,v),M*solve(M,v)-v))


# HW4 - Problem 4

# M = listlist2mat([[one,one,0,0,0,0,0,0],[0,one,one,0,0,0,0,0],[one,0,0,one,0,0,0,0],
# [0,one,0,0,one,0,0,0],[0,0,one,0,one,0,0,0],[0,0,0,one,one,0,0,0],[0,0,0,0,0,one,0,one],
# [0,0,0,0,0,0,one,one]])
# a = list2vec([0,0,one,one,0,0,0,0])
# b = list2vec([0,0,0,0,0,one,one,0])
# c = list2vec([one,0,0,0,one,0,0,0])
# d = list2vec([0,one,0,one,0,0,0,0])
# M=M.transpose()
# print(M.transpose())
# print("A:")
# MySolve(M,a)
# print("B:")
# MySolve(M,b)
# print("C:")
# MySolve(M,c)
# print("D:")
# MySolve(M,d)

# HW4 - P6

# print("a:\n")
# M=listlist2mat([[1,2,3],[4,5,6]])
# M=M.transpose()
# z=list2vec([1,1,1])
# MySolve(M,z)
# 
# print("b:\n")
# M=listlist2mat([[0,-1,0,-1],[pi,pi,pi,pi]])
# M=M.transpose()
# sq=2**0.5
# z=list2vec([-sq,sq,-sq,sq])
# ans=solve(M,z)
# print(ans[0],ans[1])
# print(-2*sq, -sq/pi)
# MySolve(M,z)
# 
# print("c:\n")
# M=listlist2mat([[1,-1,0,0,0],[0,1,-1,0,0],[0,0,1,-1,0],[0,0,0,1,-1]])
# M=M.transpose()
# z=list2vec([-1,0,0,0,1])
# MySolve(M,z)

# HW 4 - P7

# u = [3,9,6,5,5] 
# v = [4,10,6,6,8]
# w = [1,1,0,1,3]
# 
# M = listlist2mat([u,v])
# M=M.transpose()
# MySolve(M,list2vec(w))


# HW4 - P8

# a=list2vec([1,0,0])
# b=list2vec([0,1,0])
# c=list2vec([0,0,1])
# d=list2vec([1,1,1])
# print(repr(a))

# HW4 - P9

# print("a:\n")
# M=listlist2mat([[one,one,one,one],[one,0,one,0],[0,one,one,0]])
# M=M.transpose()
# z=list2vec([0,one,0,one])
# MySolve(M,z)
# 
# print("b:\n")
# M=listlist2mat([[0,0,0,one],[0,0,one,0],[one,one,0,one]])
# M=M.transpose()
# z=list2vec([one,one,one,one])
# MySolve(M,z)
# 
# print("c:\n")
# M=listlist2mat([[one,one,0,one,one],[0,0,one,0,0],[0,0,one,one,one],[one,0,one,one,one]])
# M=M.transpose()
# z=list2vec([one,one,one,one,one])
# MySolve(M,z)

# HW4 - P10

# (v1,v2,v3,v4,v5,v6,v7,v8)= ([one,one,0,0,0,0,0,0],[0,one,one,0,0,0,0,0],[one,0,0,one,0,0,0,0],[0,one,0,0,one,0,0,0],[0,0,one,0,one,0,0,0],[0,0,0,one,one,0,0,0],[0,0,0,0,0,one,0,one], [0,0,0,0,0,0,one,one])
# 
# print("a:\n")
# M=listlist2mat([v2,v3,v4,v5])
# M=M.transpose()
# z=list2vec(v1)
# MySolve(M,z)
# 
# print("b:\n")
# M=listlist2mat([v2,v3,v4,v5,v7,v8])
# M=M.transpose()
# z=list2vec(v1)
# MySolve(M,z)
# 
# print("c:\n")
# M=listlist2mat([v2,v3,v4,v6])
# M=M.transpose()
# z=list2vec(v1)
# MySolve(M,z)
# 
# print("d:\n")
# M=listlist2mat([v2,v3,v5,v6,v7,v8])
# M=M.transpose()
# z=list2vec(v1)
# MySolve(M,z)

# HW4 - P11

# a0 = Vec({'a','b','c','d'}, {'a':1})
# a1 = Vec({'a','b','c','d'}, {'b':1})
# a2 = Vec({'a','b','c','d'}, {'c':1})
# 
# M = coldict2mat([a0,a1,a2])
# print(M)
# u=Vec({0,1,2}, {0:2, 1:4, 2:6})
# print(M*u)
# print(hw4.rep2vec(Vec({0,1,2}, {0:2, 1:4, 2:6}), [a0,a1,a2]) == Vec({'a', 'c', 'b', 'd'},{'a': 2, 'c': 6, 'b': 4, 'd': 0}))

# HW4 - P12

# a0 = Vec({'a','b','c','d'}, {'a':1})
# a1 = Vec({'a','b','c','d'}, {'b':1})
# a2 = Vec({'a','b','c','d'}, {'c':1})
# print(hw4.vec2rep([a0,a1,a2], Vec({'a','b','c','d'}, {'a':3, 'c':-2})) == Vec({0, 1, 2},{0: 3.0, 1: 0.0, 2: -2.0}))

# HW4 - P13

# a0 = Vec({'a','b','c','d'}, {'a':1})
# a1 = Vec({'a','b','c','d'}, {'b':1})
# a2 = Vec({'a','b','c','d'}, {'c':1})
# a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
# print(hw4.is_superfluous([a0], 0)==False)
# print(hw4.is_superfluous([a0,a1,a2,a3], 3)==True)
# print(hw4.is_superfluous([a0,a1,a2,a3], 0)==True)
# print(hw4.is_superfluous([a0,a1,a2,a3], 1)==False)

# HW4 - P14

# vlist = [Vec({0, 1, 2},{0: 1, 1: 0, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 0, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 0})]
# for v in vlist[2:6]:
# 	print(v)
# print(hw4.is_independent(vlist)==False)
# print(hw4.is_independent(vlist[:3])==True)
# print(hw4.is_independent(vlist[:2])==True)
# print(hw4.is_independent(vlist[1:4])==True)
# print(hw4.is_independent(vlist[2:5])==True)
# print(hw4.is_independent(vlist[2:6])==False)
# print(hw4.is_independent(vlist[1:3])==True)
# print(hw4.is_independent(vlist[5:])==True)
# print(hw4.is_superfluous(vlist[2:6],3))

# HW4 - P17

# a0 = Vec({'a','b','c','d'}, {'a':1})
# a1 = Vec({'a','b','c','d'}, {'b':1})
# a2 = Vec({'a','b','c','d'}, {'c':1})
# a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
# print(hw4.superset_basis([a0, a3], [a0, a1, a2]))

# HW4 - P18

# S = [list2vec(v) for v in [[0,0,5,3],[2,0,1,3],[0,0,1,0],[1,2,3,4]]]
# A = [list2vec(v) for v in [[0,0,5,3],[2,0,1,3]]]
# z = list2vec([0,2,1,1])
# print(hw4.exchange(S, A, z)==Vec({0, 1, 2, 3},{0: 0, 1: 0, 2: 1, 3: 0}))

# Geometry Lab
# (pos,col)=file2mat('Tux-small.png')
# trans=translation(100,100)
# scal=scale(2,2)
# rot=rotation(pi/2)
# rot2=rotate_about(20,20,pi/2)
# refy=reflect_y()
# refx=reflect_x()
# print(rot)
# pos=Vec({'x','y','u'}, {'x':1,'y':1,'u':1})
# print(pos)
# print(trans)
# print(trans*pos)

# mat2display(pos,col)
# mat2display(trans*pos,col)
# mat2display(trans*scal*pos,col)
# mat2display(trans*rot*pos,col)
# mat2display(trans*rot2*pos,col)
# mat2display(trans*refy*pos,col)
# mat2display(trans*refx*pos,col)


# HW5 - P1

# w0 = list2vec([1,0,0])
# w1 = list2vec([0,1,0])
# w2 = list2vec([0,0,1])
# 
# v0 = list2vec([1,2,3])
# v1 = list2vec([1,3,3])
# v2 = list2vec([0,3,3])
# 
# exchange_S0 = [w0, w1, w2]
# print(exchange_S0)
# ejection1 = hw4.exchange(exchange_S0+[v0], [v0, v1, v2], v0)
# print(ejection1)
# exchange_S1 = [w1,w2,v0]
# ejection2 = hw4.exchange(exchange_S1+[v1], [v0, v1, v2], v1)
# print(ejection2)
# exchange_S2 = [w2,v0,v1]
# ejection3 = hw4.exchange(exchange_S2+[v2], [v0, v1, v2], v2)
# print(ejection3)
# exchange_S3 = [v0, v1, v2]

# HW5 - P2

# w0 = list2vec([0,one,0])
# w1 = list2vec([0,0,one])
# w2 = list2vec([one,one,one])
# 
# v0 = list2vec([one,0,one])
# v1 = list2vec([one,0,0])
# v2 = list2vec([one,one,0])
# 
# exchange_S0 = [w0, w1, w2]
# print(exchange_S0)
# ejection1 = hw4.exchange(exchange_S0+[v0], [v0, v1, v2], v0)
# print(ejection1)
# exchange_S1 = [w1,w2,v0]
# ejection2 = hw4.exchange(exchange_S1+[v1], [v0, v1, v2], v1)
# print(ejection2)
# exchange_S2 = [w2,v0,v1]
# ejection3 = hw4.exchange(exchange_S2+[v2], [v0, v1, v2], v2)
# print(ejection3)
# exchange_S3 = [v0, v1, v2]

# HW5 - P3

# S = [list2vec(v) for v in [[1,0,0],[0,1,0],[0,0,1]]]
# print(S)
# B = [list2vec(v) for v in [[1,1,0],[0,1,1],[1,0,1]]]
# print(hw5.morph(S, B)==[(Vec({0, 1, 2},{0: 1, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 1, 1: 0, 2: 0})), (Vec({0, 1, 2},{0: 0, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 0})), (Vec({0, 1, 2},{0: 1, 1: 0, 2: 1}), Vec({0, 1, 2},{0: 0, 1: 0, 2: 1}))])

def findbasis(V):
	while not hw4.is_independent(V):
		for i in range(len(V)):
			if hw4.is_superfluous(V,i):
				V.remove(V[i])
				break
	return V

# HW5 - P4

# [print(repr(v)) for v in findbasis([list2vec(v) for v in [[1,2,0],[0,2,1]]])]
# [print(repr(v)) for v in findbasis([list2vec(v) for v in [[1,0],[2,2],[0,1]]])]

# HW5 - P5

L = [Vec({0, 1, 2},{0: 1, 1: 0, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 0, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 1})]
assert hw5.my_is_independent(L)==False
assert hw5.my_is_independent(L[:2])==True
assert hw5.my_is_independent(L[:3])==True
assert hw5.my_is_independent(L[1:4])==True
assert hw5.my_is_independent(L[0:4])==False
assert hw5.my_is_independent(L[2:])==False
assert hw5.my_is_independent(L[2:5])==False

# HW5 - P7

assert hw5.my_rank([list2vec(v) for v in [[1,2,3],[4,5,6],[1.1,1.1,1.1]]])==2

# HW5 - P9

U_basis = [Vec({0, 1, 2, 3, 4, 5},{0: 2, 1: 1, 2: 0, 3: 0, 4: 6, 5: 0}), Vec({0, 1, 2, 3, 4, 5},{0: 11, 1: 5, 2: 0, 3: 0, 4: 1, 5: 0}), Vec({0, 1, 2, 3, 4, 5},{0: 3, 1: 1.5, 2: 0, 3: 0, 4: 7.5, 5: 0})]
V_basis = [Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 7, 3: 0, 4: 0, 5: 1}), Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 15, 3: 0, 4: 0, 5: 2})]
w = Vec({0, 1, 2, 3, 4, 5},{0: 2, 1: 5, 2: 0, 3: 0, 4: 1, 5: 0})
assert hw5.direct_sum_decompose(U_basis, V_basis, w) == (Vec({0, 1, 2, 3, 4, 5},{0: 2.0, 1: 4.999999999999972, 2: 0.0, 3: 0.0, 4: 1.0, 5: 0.0}), Vec({0, 1, 2, 3, 4, 5},{0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}))

# HW5 - P10

M = Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): 0, (1, 2): 1, (3, 2): 0, (0, 0): 1, (3, 3): 4, (3, 0): 0, (3, 1): 0, (1, 1): 2, (2, 1): 0, (0, 2): 1, (2, 0): 0, (1, 3): 0, (2, 3): 1, (2, 2): 3, (1, 0): 0, (0, 3): 0})
assert hw5.is_invertible(M)==True

# Hw5 - P11

M = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): one, (1, 2): 0, (0, 0): 0, (2, 0): 0, (1, 0): one, (2, 2): one, (0, 2): 0, (2, 1): 0, (1, 1): 0})
assert hw5.find_matrix_inverse(M) == Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): one, (2, 0): 0, (0, 0): 0, (2, 2): one, (1, 0): one, (1, 2): 0, (1, 1): 0, (2, 1): 0, (0, 2): 0})

#HW5 - P12

A = listlist2mat([[1, .5, .2, 4],[0, 1, .3, .9],[0,0,1,.1],[0,0,0,1]])
assert hw5.find_triangular_matrix_inverse(A) == Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): -0.5, (1, 2): -0.3, (3, 2): 0.0, (0, 0): 1.0, (3, 3): 1.0, (3, 0): 0.0, (3, 1): 0.0, (2, 1): 0.0, (0, 2): -0.05000000000000002, (2, 0): 0.0, (1, 3): -0.87, (2, 3): -0.1, (2, 2): 1.0, (1, 0): 0.0, (0, 3): -3.545, (1, 1): 1.0})

# Perspective Lab

# (X_pts, colors) = file2mat('board.png', ('x1','x2','x3'))
# Y_pts = H * X_pts
# Y_board=mat_move2board(Y_pts)
# mat2display(Y_board, colors, ('y1', 'y2', 'y3'),scale=100, xmin=None, ymin=None)

#HW6 - P2

assert hw6.is_echelon([[1,1,1],[0,1,1],[0,0,1]])==True
assert hw6.is_echelon([[0,1,1],[0,1,0],[0,0,1]])==False
assert hw6.is_echelon([[2,1,0],[0,-4,0],[0,0,1]])==True
assert hw6.is_echelon([[2,1,0],[-4,0,0],[0,0,1]])==False
assert hw6.is_echelon([[2,1,0],[0,3,0],[1,0,1]])==False
assert hw6.is_echelon([[1,1,1,1,1],[0,2,0,1,3],[0,0,0,5,3]])==True
assert hw6.is_echelon([[0,0,0],[0,0,0],[0,0,0]])==True
assert hw6.is_echelon([[1,0,0],[0,1,0],[0,1,0]])==False
assert hw6.is_echelon([[0]*4,[1]*4])==False
assert hw6.is_echelon([[1,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1],[0,0,1,1,1,0,1,0],[0,0,0,0,0,1,1,0]])==True
assert hw6.is_echelon([[1]])==True
assert hw6.is_echelon([[0]])==True

#HW6 - P3

# print(triangular_solve_n([list2vec([10,-3]),list2vec([0,1])], [1,3]))
# print(listlist2mat([[10,2,-3,53],[0,0,1,2013]])*list2vec([1,0,3,0]))

# print(triangular_solve_n([list2vec([2,1,3]),list2vec([0,5,3]),list2vec([0,0,1])], [1,-1,3]))
# print(listlist2mat([[2,0,1,3],[0,0,5,3],[0,0,0,1]])*list2vec([-3,0,-2,3]))

# print(triangular_solve_n([list2vec([2,4,2]),list2vec([0,-1,1]),list2vec([0,0,5])], [2,0,10]))
# print(listlist2mat([[2,2,4,3,2],[0,0,-1,11,1],[0,0,0,0,5]])*list2vec([-5,0,2,0,2]))

#HW6 - P4

# print(triangular_solve_n([list2vec([1,-2]),list2vec([0,2])], [5,3]))
# print(listlist2mat([[1,3,-2,1,0],[0,0,2,-3,0],[0,0,0,0,0]])*list2vec([8,0,1.5,0,0]))
# 
# print(triangular_solve_n([list2vec([1,-8]),list2vec([0,2])], [5,4]))
# print(listlist2mat([[1,2,-8,-4,0],[0,0,2,12,0],[0,0,0,0,0],[0,0,0,0,0]])*list2vec([21,0,2,0,0]))

#HW6 - P5
D = {'A','B','C','D','E'}
U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})] 
b_list = [one,0,one]
cols = ['A', 'B', 'C', 'D', 'E']
assert hw6.echelon_solve(U_rows, cols, b_list)==Vec(D,{'B': 0, 'C': one, 'A': one})

#HW6 - P7
# A = listlist2mat([[0,0,0,one,0],[0,0,0,one,one],[one,0,0,one,0],[one,0,0,0,one],[one,0,0,0,0]])
# M = listlist2mat([[0,0,one,0,0],[one,0,0,0,0],[one,one,0,0,0],[0,one,one,one,0],[one,0,one,0,one]])
# rows=mat2rowdict(M)
# for k,row in rows.items():
# 	print("Row %s"%k)
# 	print(repr(row))
# 	print(row*A)

#HW6 - P8
# A = listlist2mat([[0,0,0,one,0],[0,0,0,one,one],[one,0,0,one,0],[one,one,one,0,one],[one,0,0,one,0]])
# M = listlist2mat([[0,0,one,0,0],[0,0,one,one,0],[one,0,0,0,0],[one,one,0,0,0],[0,0,one,0,one]])
# rows=mat2rowdict(M)
# for k,row in rows.items():
# 	print("Row %s"%k)
# 	print(repr(row))
# 	print(row*A)
	
#HW6 - P9
def project_along(b, a): 
	return ((b*a)/(a*a) if a*a != 0 else 0)*a

def project_orthogonal(b, a): 
	return b - project_along(b, a)
	
A = list2vec([1,2])
B = list2vec([2,3])
print(project_along(B,A))
print(((A*B)/(A*A))*A)

A = list2vec([0,1,0])
B = list2vec([1.414,1,1.732])
print(project_along(B,A))
print(((A*B)/(A*A))*A)

A = list2vec([-3,-2,-1,4])
B = list2vec([7,2,5,0])
print(project_along(B,A))
print(((A*B)/(A*A))*A)




