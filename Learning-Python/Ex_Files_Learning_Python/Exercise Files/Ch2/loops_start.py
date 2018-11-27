#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while (x<5):
    print(x)
    x+=1


  # define a for loop
  for i in range(5):
    x -= 1
    print(x)


  # use a for loop over a collection
  days = ["Mon","Tue","Wed",\
          "Thurs","Fri","Sat","Sun"]
  for day in days:
    print(day)
    
 
  # use the break and continue statements
  for day in days:
    if day == "Wed":
      continue
    if day == "Fri":
      break
    print(day)


  #using the enumerate() function to get index 
  for index,day in enumerate(days):
    print("Day #{} = {}".format(index,day))


if __name__ == "__main__":
  main()
