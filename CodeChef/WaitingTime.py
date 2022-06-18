# Shane Hagan
# CodeChef Waiting Time Problem
# Date: 06/18/2022

# Read the number of test cases.
testCases = int(raw_input())
for i in range(testCases):
	# Read integers x, y
	(x, y) = map(int, raw_input().split(' '))
	
	totalDays = x * 7
	remainingDays = totalDays - y
	
	print(remainingDays)
	
	
	
'''
Input 
4
1 5
1 6
1 1
2 2

Output
2
1
6
12
'''
