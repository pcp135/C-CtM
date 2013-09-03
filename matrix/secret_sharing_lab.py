# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import *
from matutil import *
from vec import Vec
from itertools import combinations
from independence import rank



## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,	 0, one,	 0, one])
b0 = list2vec([one, one,	 0,		0,	 0, one])

def choose_secret_vector(s,t):
	while 1:
		test = random_vector()
		if test*a0 == s and test*b0 == t:
			return test

def random_vector():
	return list2vec([randGF2() for _ in range(6)])
	
def independent_vectors():
	while 1:
		vectors = [(a0,b0)] + [(random_vector(),random_vector()) for _ in range(4)]
		if is_independent_set(vectors):
			return vectors				
			
def is_independent_set(v):
	for i in combinations(v,3):
		a,b=zip(*i)
		M=list(a)+list(b)
		if len(M) != rank(M):
			return False
	return True

in_vecs=independent_vectors()
print(in_vecs)

## Problem 2
# Give each vector as a Vec instance
secret_a0 = in_vecs[0][0]
secret_b0 = in_vecs[0][1]
secret_a1 = in_vecs[1][0]
secret_b1 = in_vecs[1][1]
secret_a2 = in_vecs[2][0]
secret_b2 = in_vecs[2][1]
secret_a3 = in_vecs[3][0]
secret_b3 = in_vecs[3][1]
secret_a4 = in_vecs[4][0]
secret_b4 = in_vecs[4][1]

