def linear(a, k):
 
    for i in a:
        if a[i] == k:
            return True
    return False
 
 
a= [1, 2, 3 , 4 , 5 , 6,-2]
 
k = int(input("Enter Key:"))
 
if linear(a, k):
    print("Element Found")
else:
    print("Element Not Found")
