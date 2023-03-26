d = { }
while True :
      name = input("Enter employee name :-")
      sal = int(input("Enter salary :-"))
      d[ name] = sal
      exit = input("Do you want to quit then enter y,otherwise press enter :-")
      if exit == "y" :
            break
print(d)      
