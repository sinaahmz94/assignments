a = float(input("first side of triangle: "))
b = float(input("second side of triangle: "))
c = float(input("third side of triangle: "))

if a + b > c and a + c > b and b + c > a:
    print("you can make a triangle")
else:
    print("*oops* you cant make a triangle")2
    
