num = int(input("Enter the number: "))
i=1
# for even number
numOdd = int((num+1)/2)
numEven = int(num/2)
print(numEven,numOdd)
d = 2
# for even number
a = 2
sumEven = int(numEven*(2*a+(numEven-1)*d)/2)
a = 1
sumOdd = int(numOdd*(2*a+(numOdd-1)*d)/2)

print("Sum of even digits: ",sumEven)
print("Sum of odd digits: ",sumOdd)
