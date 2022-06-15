# Shane Hagan
# CodeChef Age Limit Problem
# Date: 06/14/2022

# Read the number of test cases.
testCases = int(raw_input())
for i in range(testCases):
	# Read integers x, y, and a respectively
	(x, y, a) = map(int, raw_input().split(' '))
	
	
	# Set our conditions and outputs
	if (a >= x) & (a < y):
	    print("Yes")
	
	else:
	    print("No")
	    
	    
	    
# ran successfully with the test cases and outputs:
'''
Input
5
21 34 30
25 31 31
22 29 25
20 40 15
28 29 28

Output
YES
NO
YES
NO
YES
'''
	    

