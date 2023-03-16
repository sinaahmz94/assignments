a = float(input("weight(kg): "))
b = float(input("height(meter): "))

bmi = a / b ** 2
print("your bmi is: " , bmi )
if bmi < 18.5:
    print("underweight")
elif 18.5 < bmi < 24.9:
    print("normal weight")
elif 25 < bmi < 29.9:
    print("overwight")
elif 30 < bmi < 34.9:  
    print("obesity") 
elif 35 < bmi < 39.9:
    print("Extreme Obesity") 
