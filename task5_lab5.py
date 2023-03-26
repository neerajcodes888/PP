start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
result = [(x, x**2) for x in range(start, end + 1)]
print(result)
