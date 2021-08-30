# BMI Calc
height = float(input("Please enter Height in foot : "))
height_in_meter = height * 12/39.37

weight = int(input("Please enter Weight in Kg : "))
BMI = weight/pow(height_in_meter, 2)

print("The BMI : - ", BMI)

if BMI > 25:
    print("it's Overweight")
elif BMI < 18:
    print("it's Underweight")
else:
    print("Fit")
