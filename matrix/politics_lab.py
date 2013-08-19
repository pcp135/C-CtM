voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
		"""
		Input: None (use voting_data above)
		Output: A dictionary that maps the last name of a senator
						to a list of numbers representing the senator's voting
						record.
		Example: 
				>>> create_voting_dict()['Clinton']
				[-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

		This procedure should return a dictionary that maps the last name
		of a senator to a list of numbers representing that senator's
		voting record, using the list of strings from the dump file (strlist). You
		will need to use the built-in procedure int() to convert a string
		representation of an integer (e.g. '1') to the actual integer
		(e.g. 1).

		You can use the split() procedure to split each line of the
		strlist into a list; the first element of the list will be the senator's
		name, the second will be his/her party affiliation (R or D), the
		third will be his/her home state, and the remaining elements of
		the list will be that senator's voting record on a collection of bills.
		A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

		The lists for each senator should preserve the order listed in voting data. 
		"""
		voting_records={}
		for line in voting_data:
			line = line.split()
			voting_records[line[0]]=[int(x) for x in line[3:]]
		return voting_records

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
		"""
		Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
					 names to lists representing their voting records.
		Output: the dot-product (as a number) representing the degree of similarity
						between two senators' voting policies
		Example:
				>>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
				>>> policy_compare('Fox-Epstein','Ravella', voting_dict)
				-2
		"""
		
		return sum([a*b for (a,b) in zip(voting_dict[sen_a], voting_dict[sen_b])])


## Task 3

def most_similar(sen, voting_dict):
		"""
		Input: the last name of a senator, and a dictionary mapping senator names
					 to lists representing their voting records.
		Output: the last name of the senator whose political mindset is most
						like the input senator (excluding, of course, the input senator
						him/herself). Resolve ties arbitrarily.
		Example:
				>>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
				>>> most_similar('Klein', vd)
				'Fox-Epstein'

		Note that you can (and are encouraged to) re-use you policy_compare procedure.
		"""
		high_score,highest=0,"None"
		for senator in voting_dict.keys():
			similarity=policy_compare(sen,senator,voting_dict)
			if sen!=senator and similarity>high_score:
				high_score,highest=similarity,senator
		return highest
		

## Task 4

def least_similar(sen, voting_dict):
		"""
		Input: the last name of a senator, and a dictionary mapping senator names
					 to lists representing their voting records.
		Output: the last name of the senator whose political mindset is least like the input
						senator.
		Example:
				>>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
				>>> least_similar('Klein', vd)
				'Ravella'
		"""
		low_score,lowest=10,"None"
		for senator in voting_dict.keys():
			similarity=policy_compare(sen,senator,voting_dict)
			if sen!=senator and similarity<low_score:
				low_score,lowest=similarity,senator
		return lowest
		
		

## Task 5
votes=create_voting_dict()
most_like_chafee		= most_similar('Chafee',votes)
least_like_santorum = least_similar('Santorum',votes) 

# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
		"""
		Input: the name of a senator, a set of senator names, and a voting dictionary.
		Output: the average dot-product between sen and those in sen_set.
		Example:
				>>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
				>>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
				-0.5
		"""
		sims = [policy_compare(sen,senator,voting_dict) for senator in sen_set]
		return sum(sims)/len(sims)

democrats=set()
for line in voting_data:
	line=line.split()
	if line[1]=='D':
		democrats.add(line[0])
		
demo_sims={dem: find_average_similarity(dem, democrats,votes) for dem in democrats}
		
most_average_Democrat = max(demo_sims.keys(), key=(lambda key: demo_sims[key]))
 # give the last name (or code that computes the last name)


# Task 7

def find_average_record(sen_set, voting_dict):
		"""
		Input: a set of last names, a voting dictionary
		Output: a vector containing the average components of the voting records
						of the senators in the input set
		Example: 
				>>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
				>>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
				[-0.5, -0.5, 0.0]
		"""
		return [sum(x)/len(sen_set) for x in zip(*[voting_dict[x] for x in sen_set])]

average_Democrat_record = find_average_record(democrats,votes)
# (give the vector)


# Task 8

def bitter_rivals(voting_dict):
		"""
		Input: a dictionary mapping senator names to lists representing
					 their voting records
		Output: a tuple containing the two senators who most strongly
						disagree with one another.
		Example: 
				>>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
				>>> bitter_rivals(voting_dict)
				('Fox-Epstein', 'Ravella')
		"""
		sen_a,sen_b,agreement='None','None',100
		for i in voting_dict.keys():
			for j in voting_dict.keys():
				if policy_compare(i,j,voting_dict)<agreement:
					sen_a,sen_b,agreement=i,j,policy_compare(i,j,voting_dict)
		return (sen_a, sen_b)

