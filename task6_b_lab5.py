n = int(input("enter a number:"))
n += 1
for i in range(1, n + 1):
  for j in range(1, n - i + 1):
    print(i, end=" ")
  print("\r")