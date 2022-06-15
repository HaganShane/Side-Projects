# Shane Hagan
# CodeChef Chairs Requirement Problem
# Date: 06/14/2022

# Read the number of test cases.
testCases = int(raw_input())

for i in range(testCases):
	# Read integers s, c (s for students, c for chairs)
	(s, c) = map(int, raw_input().split(' '))
	
	if (s > c):
	    print(s-c)
	elif (s <= c):
	    print("0")
	    
# ran with test cases successfully 
'''
4
20 14
41 41
35 0
50 100
'''
