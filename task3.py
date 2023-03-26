l=[1,2,3,4,5]

print ("Original list : " + str(l))
flag = 0
i = 1
while i < len(l):
    if(l[i] < l[i - 1]):
        flag = 1
    i += 1
if (not flag) :
    print ("List is sorted.")
else :
    print ("List is not sorted.")
    
