s = input("Enter the string: ")
left=0
right=len(s)-1

while left<right:
    if s[left]==s[right]:
        left += 1
        right -= 1
    else: 
        print("Not palindrome")
        break
else:
    print("Palindrome")
