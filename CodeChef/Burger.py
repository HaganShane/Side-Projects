# Shane Hagan
# CodeChef Burgers Problem
# Date: 06/17/2022

# Read the number of test cases.
testCases = int(raw_input())
for i in range(testCases):
	# Read integers x, y
	(x, y) = map(int, raw_input().split(' '))
	
	# print the min number of either burgers or buns
	print(min(x,y))
	    
	    
	    
# ran successfully with the test cases and outputs:
'''
Input
4
2 2
2 3
3 2
23 17

Output
2
2
2
17
'''
