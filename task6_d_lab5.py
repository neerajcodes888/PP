n = int(input("enter a number:"))
asc = 65
for i in range(0, n):
  for j in range(0, n):
    ch = chr(asc)
    print(ch, end=" ")
  asc += 1
  print("\r")