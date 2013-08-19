import politics_lab as p
from hw2 import *
from vec import Vec

votes=p.create_voting_dict()
print(votes['Obama'])

print(set(votes.keys()))

most=p.most_similar('Obama',votes)
print(most)
print(p.policy_compare('Obama',most,votes))

least=p.least_similar('Obama',votes)
print(least)
print(p.policy_compare('Obama',least,votes))

print(p.most_like_chafee)
print(p.least_like_santorum)

print(p.democrats)

for democrat in p.democrats:
	print("Senator: %s = %s" % (democrat,p.find_average_similarity(democrat, p.democrats,votes)))

print(p.most_average_Democrat)

print(p.average_Democrat_record)
votes['Average']=p.average_Democrat_record

print(p.most_similar('Average',votes))

votes=p.create_voting_dict()
rivals=p.bitter_rivals(votes)
print(rivals)

for senator in rivals:
	print(votes[senator])
	
D = {'a','b','c'}
v1 = Vec(D, {'a': 1})
v2 = Vec(D, {'a': 0, 'b': 1})
v3 = Vec(D, {				 'b': 2})
v4 = Vec(D, {'a': 10, 'b': 10})

assert vec_select([v1, v2, v3, v4], 'a') == [Vec(D,{'b': 1}), Vec(D,{'b': 2})]

assert vec_sum([v1, v2, v3, v4], D) == Vec(D, {'b': 13, 'a': 11})
assert vec_sum([],D) == Vec(D,{})

assert vec_select_sum([v1, v2, v3, v4], 'a', D) == Vec(D, {'b': 3})

v1 = Vec({1,2,3}, {2: 9})
v2 = Vec({1,2,4}, {1: 1, 2: 2, 4: 8})
assert scale_vecs({3: v1, 5: v2}) == [Vec({1,2,3},{2: 3.0}), Vec({1,2,4},{1: 0.2, 2: 0.4, 4: 1.6})]

from GF2 import one
D = {'a', 'b', 'c'}
L = [Vec(D, {'a': one, 'c': one}), Vec(D, {'b': one})]
print(GF2_span(D, L))
assert len(GF2_span(D, L)) == 4
assert Vec(D, {}) in GF2_span(D, L)
assert Vec(D, {'b': one}) in GF2_span(D, L)
assert Vec(D, {'a':one, 'c':one}) in GF2_span(D, L)
assert Vec(D, {x:one for x in D}) in GF2_span(D, L)






