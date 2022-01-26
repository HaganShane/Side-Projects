# Author: Shane Hagan
# Date: 01/26/2021
# Purpose: Practice coding on coderbyte.com

# Main function, takes in the number as input
def FirstFactorial(num):
  # Declare the factorial value to start at 1
  factorial = 1

  # while loop to keep track of our input number, stop when it reaches 0
  while num > 0:
    # factorial (which starts at 1) will multiply by our number and store it as our factorial value
    factorial *= num
    # subtract 1 off the number so the while loop tracks properly and the factorial will multiply by the next number
    num -= 1
    
  # after the loop is done, return our factorial value  
  return factorial

# keep this function call here 
print(FirstFactorial(input()))
