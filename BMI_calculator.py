weight = input("enter your weight in Kilo Gram(KG)\n")
height = input("enter your height in meters\n")
float_height = float(height)
BMI = float(weight)/(float_height ** float_height)
BMI = int(BMI)
print("your BMI is", BMI)
if 0 <= BMI <= 18.5:
    print("you are underweight")
elif 18.6 <= BMI <= 25:
    print("you are normal weight")
elif 25.1 <= BMI <= 30:
    print("you are overweight")
else:
    print("you are too much, you will die of obesity")
