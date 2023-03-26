n = int(input("Enter the number: "))
fact=n
while n!=1:
    fact = fact*(n-1)
    n = n-1
print("Factorial is: ",fact)
