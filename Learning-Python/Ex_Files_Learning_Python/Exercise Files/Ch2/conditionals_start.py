#
# Example file for working with conditional statements
#

def main():
  x, y = 10, 100
  
  # conditional flow uses if, elif, else  
  if x<y:
    print("x is less than y")
  elif x>y:
    print("x is more than y")
  else:
    print("x is equal to y")

  # conditional statements let you use "a if C else b"
  print("x is less than y" if (x<y) else "x is more than y")
  

if __name__ == "__main__":
  main()
