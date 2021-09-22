sideA=float(input("Enter the lenght of first side of triangle: "))
sideB=float(input("Enter the lenght of second side of triangle: "))
sideC=float(input("Enter the lenght of third side of triangle: "))
if sideA==sideB and sideB==sideC:
    print("Triangle is Equilateral")
elif sideA==sideB or sideB==sideC or sideA==sideC:
    print("Triangle is Isosceles")
else:
    print("Triangle is Scalane")