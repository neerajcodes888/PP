n = int(input("Enter the number: "))
i=2
while i<n:
    if n%i==0:
        print("Non prime")
        break
    i+=1
else:
    print("Prime")
