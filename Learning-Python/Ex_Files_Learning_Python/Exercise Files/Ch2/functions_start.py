#
# Example file for working with functions
#

# define a basic function
def f1():
  print("This is a basic function")


# function that takes arguments
def f2(x,y):
  print("{}*{} = {}".format(x,y,x*y))

# function that returns a value
def f3(x,y,z):
  return x*y**z

# function with default value for an argument
def f4(x,y,z=5):
  return x*y**z

#function with variable number of arguments
def f5(*args):
  result = 0
  for x in args:
    result = result + x
  return result

# Test functions
f1()
f2(5,3)
print(f3(3,4,2))
print(f4(2,3))
print(f5(1,2))
print(f5(1,2,3,4,5))
