side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))

if side1**2 + side2**2  == side3**2:
    print("Triangle is Right angle triangle")
elif side1**2 + side3**2  == side2**2:
    print("Triangle is Right angle triangle")
elif side3**2 + side2**2  == side1**2:
    print("Triangle is Right angle triangle")
else:
    print("Triangle is Not Right angle triangle")
