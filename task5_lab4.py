names = ["Neeraj", "Arya", "Harsha", "David", "Varsha"]
for i in range(len(names) - 1):
  for j in range(i + 1, len(names)):
    if names[i] > names[j]:
      names[i], names[j] = names[j], names[i]
print("Sorted names:")
for name in names:
  print(name)
