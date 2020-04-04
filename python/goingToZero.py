print("This program ask the user to enter an integer. The code will output integers until reaching 0. \nIf the integer is positive, it will output numbers in decreasing order. \nIf the input is negative, it will output numbers in incriments of 1\n")

x  = int(input("Enter an integer: "))

if x < 0:
  while x < 0:
    print(x, end= " > ")
    x += 1
  print(0)
else:
  while x > 0:
    print(x, end= " -> ")
    x -= 1
  print(0)
