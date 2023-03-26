num = int(input("Enter the number: "))
t1=0
t2=1
print("Fibonacci is: ",t1," ",t2,end='')
i=1 
new=0
while i<num-1:
    new = t1+t2
    t1 = t2
    t2 = new
    print(" ",new,end='')
    i = i+1
print("\n")

