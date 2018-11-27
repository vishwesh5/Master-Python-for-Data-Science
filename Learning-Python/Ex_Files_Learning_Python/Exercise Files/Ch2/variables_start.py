# 
# Example file for variables
#

# Declare a variable and initialize it
var = 1

print(var)

# # re-declaring the variable works
var = "start"

print(var)

# # ERROR: variables of different types cannot be combined
#var = "start"+1 # error
var = "start"+str(1)
print(var)

# Global vs. local variables in functions
# Global
testval = "test"

def f1():
  # Local variable
  testval = 100
  print(testval)

f1()
print(testval)

def f2():
  # Global variable
  global testval
  testval = 100
  print(testval)

f2()
print(testval)
