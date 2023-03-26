n = int(input("enter a number:"))
n += 1
k = n - 1
for i in range(0, n):
  for j in range(0, k):
    print(end=" ")
  k -= 1
  for j in range(1, i + 1):
    print(j, end=" ")
  print("\r")