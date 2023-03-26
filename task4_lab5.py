my_tuple = ("apple", "banana", "cherry", "date", "elderberry")
item = input("Enter an item to search for in the tuple: ")
if item in my_tuple:
  print(item + " is in the tuple.")
else:
  print(item + " is not in the tuple.")
