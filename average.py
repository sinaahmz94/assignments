name = input("your name is: ")
family = input("your family name is: ")
print("please enter your grades: ")

a = float(input("first grade: "))
b = float(input("second grade: "))
c = float(input("third grade: "))

average = (a + b + c) / 3
print("your average is: " , average )
if average >= 17:
    print(name , family , "your average is great")
elif 17 > average >= 12:    
    print(name , family , "your average is normal")
elif average < 12:
    print(name , family , "you are failed")
