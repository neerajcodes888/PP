a = int(input("enter num1: "))
b = int(input("enter num2: "))
c = int(input("enter num3: "))
if a>b and a>c:
    print("largest number is ",a)
elif b>a and b>c:
    print("largest number is ",b)
else:
    print("largest number is ",c)
