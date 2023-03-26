num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = 1
i=2
while i<=num1 and i<=num2 :
    if num1%i==0 and num2%i==0 :
        result = i
    i += 1
print("GCD is ",result)

