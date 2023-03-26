a=[]
b=[]
for i in range(5):
     x=int(input("Enter a Num:"))
      a.append(x)
for i in a:
       s+=i
       avg=s/len(a)
      if i>0:
         s1+=i
      if i<0:
         s2+=i
      if i>avg:
          b.append(i)
            
print("Sum of Nums":,s)
print("Negative Nums":,s1) 
print("Positive Nums":,s2)            
