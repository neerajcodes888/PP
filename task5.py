s1=input(' enter string : ' )
d={}
p=""
for i in s1:
    if i!=' ':
       s1+=i
    else:
       if len(p) in d:
          d[len(s1)]+=1
       else :
          d[len(s1)]=1
       p=""
if len(s1) in d:
   d[len(s1)]+=1
else :
   d[len(s1)]=1
print(d)
