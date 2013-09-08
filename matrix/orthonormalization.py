from orthogonalization import *
from math import sqrt
from vec import Vec

def orthonormalize(L):
		'''
		Input: a list L of linearly independent Vecs
		Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
						Span L[:i] == Span T[:i]
		'''
		L = orthogonalize(L)
		return [v/sqrt(v*v) for v in L]


def aug_orthonormalize(L):
		'''
		Input:
				- L: a list of Vecs
		Output:
				- A pair Qlist, Rlist such that:
						* coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
						* Qlist = orthonormalize(L)
		'''
		Qlist,Rlist = aug_orthogonalize(L)
		norms = [sqrt(v*v) for v in Qlist]
		Qlist = [v/sqrt(v*v) for v in Qlist]
		Rlist = [adjust(v,norms) for v in Rlist]
		return (Qlist,Rlist)
		

def adjust(v, multipliers):
	return Vec(v.D, {k:v.f[k]*multipliers[i] for (i,k) in enumerate(v.f.keys())})