#
# Example file for working with date information
#

from datetime import date, time, datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("Today's date is ", today)


  # print out the date's individual components
  print("Date components: ", today.day, today.month, today.year)

  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Today's weekday # is: ", today.weekday())
  weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  print("Today's day is: ", weekdays[today.weekday()])

  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print("Today is: ",today)


  # Get the current time
  t = datetime.time(datetime.now())
  print("Time is ", t)


  
if __name__ == "__main__":
  main();
  
