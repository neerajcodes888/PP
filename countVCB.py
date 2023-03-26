s = input("Enter the string: ")
i=0
v=0
c=0
b=0
while i<len(s):
    if s[i]=='a'or s[i]=='e'or s[i]=='i'or s[i]=='o'or s[i]=='u':
        v +=1
    elif s[i]==' ':
        b += 1
    else:
        c += 1
    i += 1
print("Count vowels ",v)
print("Count consonants ",c)
print("Count Blank ",b)
