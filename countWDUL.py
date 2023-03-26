s = input("Enter a string ")
w=1
d=0
u=0
l=0
i=0
for i in s:
    if (i.islower()):
        l+=1
    elif (i.isupper()):
        u+=1
w = len(s.split())      
d+=len(s)-(u+l+w)

print("Word ",w)
print("Digits ",d)
print("Uppercase ",u)
print("Lowercase",l)
